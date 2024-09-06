<script> 
import router from '../router/index.js';

//Ex: https://www.target.com/
export const highlightLinkText = (text) => {
  const urlPattern = /(\b(https?|ftp|file):\/\/|www\.)[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]/ig;

  return text.replace(urlPattern, (url) => 
    {
      const realURL = !url.startsWith("http") ? `https://${url}` : url;

      return `<a href="${realURL}" target="_blank" 
                style="color: #007AFF; text-decoration: none;" 
                onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
                onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
              >${url}</a>`;
    }
  );
};

//[The link](https://www.target.com/)
export const createHyperLink = (text) => {
  const markdownLinkPattern = /\[([^\]]+)\]\((https?:\/\/[^\s]+)\)/g;
  
  return text.replace(markdownLinkPattern, (match, label, url) => 
    `<a href="${url}" target="_blank"
        style="color: #007AFF; text-decoration: none;" 
        onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
        onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
      >${label}</a>`
  );
};

//(Router link)[/LinkedIn/LinkedinTips]. Note the seemingly unused "match" parameter is necessary.
export const createRouterLink = (text) => {
  const customLinkPattern = /\(([^\)]+)\)\[([^\s]+)\]/g;
  return text.replace(customLinkPattern, (match, label, path) => {
    return `<a href="javascript:void(0);" onclick="navigateToPath('${path}')"
               style="color: #007AFF; text-decoration: none;" 
               onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
               onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
            >${label}</a>`;
  });
};

window.navigateToPath = (path) => {
  router.push(path);
};

//@Image View@[{ 'name': 'ImageView', 'params': { 'Name': 'NSA Pic', 'Description': 'This is the NSA pic', 'Pic': 'seahawk.png'} }]
//If you want to include a " character in the actual string add the following \\\\\\\". See ClassRecommendations.json for example. Search \\\\\\\"
//If you want to include a ' character in the actual string add the following &&&&. See ClassRecommendations.json for example. Search &&&&
export const createRouterLinkWithProps = (text) => {
  const markdownPattern = /@([^@]+)@\[\s*({.*?})\s*\]/g;

  return text.replace(markdownPattern, (match, label, jsonString) => {
    let toProp;

    try {
      jsonString = jsonString.replace(/'/g, '"')
      toProp = JSON.parse(jsonString);
    } catch (e) {
      console.error('Error parsing JSON string:', e);
      return match;
    }
    
    return `<a href="javascript:void(0);" onclick="navigateToVuePath('${JSON.stringify(toProp).replace(/"/g, "&quot;")}')"
               style="color: #007AFF; text-decoration: none;"
               onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
               onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
            >
            ${label}</a>`;
  });
};

window.navigateToVuePath = (toPropString) => {
  const toProp = JSON.parse(toPropString.replace(/&quot;/g, "\""));

  // The .then will scroll to the top.
  router.push(toProp).then(() => {
    window.scrollTo(0, 0); 
  });
  
};


//&DownloadLink&(/download/practice.docx)
export const createDownloadLink = (text) => {
  // const markdownLinkPattern = /\&([^\]]+)\&\((https?:\/\/[^\s]+)\)/g;

  const markdownLinkPattern = /\&([^\&]+)\&\((\/download[^\s]+)\)/g;

  const style = document.createElement('style');
  document.head.appendChild(style);

  style.textContent = `
    .custom-tooltip {
      position: absolute;
      visibility: hidden;
      background-color: #C7C7C7;
      color: black; 
      text-align: center;
      border-radius: 2px; 
      padding: 2px 4px;
      font-size: 13px;
      z-index: 1000;
      opacity: 0;
      transition: opacity 0.5s;
      bottom: -23px;
      left: 50%;
      transform: translateX(-50%);
    }
    .custom-link {
      color: #007AFF;
      text-decoration: none;
    }
    .custom-link:hover {
      color: blue;
    }
    .custom-link:hover + .custom-tooltip {
      visibility: visible;
      opacity: 1;
    }
  `;

  return text.replace(markdownLinkPattern, (match, label, downloadLink) => 
    `<div style="position: relative; display: inline-block;">
        <a href="${downloadLink}" download class="custom-link">
          ${label}
        </a>
        <div class="custom-tooltip">
          Download
        </div>
      </div>`
  );
};

</script>