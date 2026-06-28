/*
===========================================
BuildHub Embedded Analytics SDK v2.0
===========================================
*/

(function () {

    "use strict";

    const BuildHub = {

        version: "2.0",

        init: function (config) {

            if (!config) {

                console.error("❌ BuildHub: Missing configuration.");

                return;

            }

            if (!config.apiKey) {

                console.error("❌ BuildHub: apiKey is required.");

                return;

            }

            const container =
                document.getElementById("buildhub-dashboard");

            if (!container) {

                console.error(
                    "❌ BuildHub: Container '#buildhub-dashboard' not found."
                );

                return;

            }

            // Base URL
            const BASE_URL =
                config.baseUrl || "http://127.0.0.1:5000";

            // Clear previous iframe
            container.innerHTML = "";

            // Create iframe
            const iframe =
                document.createElement("iframe");

            iframe.src =
                `${BASE_URL}/embed/${config.apiKey}`;

            iframe.width =
                config.width || "100%";

            iframe.height =
                config.height || "700px";

            iframe.loading = "lazy";

            iframe.allowFullscreen = true;

            iframe.style.border =
                config.border || "none";

            iframe.style.borderRadius =
                config.borderRadius || "12px";

            iframe.style.background =
                config.background || "#ffffff";

            iframe.style.boxShadow =
                config.boxShadow ||
                "0 8px 24px rgba(0,0,0,.12)";

            iframe.style.overflow = "hidden";

            iframe.style.display = "block";

            iframe.style.transition = "0.3s";

            container.appendChild(iframe);

            console.log(
                "✅ BuildHub Dashboard Embedded Successfully"
            );

        },

        destroy: function () {

            const container =
                document.getElementById("buildhub-dashboard");

            if (container) {

                container.innerHTML = "";

            }

            console.log("🗑 BuildHub Dashboard Removed");

        },

        reload: function (config) {

            this.destroy();

            this.init(config);

        }

    };

    window.BuildHub = BuildHub;

})();