// document.addEventListener('DOMContentLoaded', function() {
//     // Step navigation
//     const nextButtons = document.querySelectorAll('.next-step');
//     const prevButtons = document.querySelectorAll('.prev-step');
//     const steps = document.querySelectorAll('.payment-step-content');

//     nextButtons.forEach(button => {
//         button.addEventListener('click', () => {
//             const currentStep = button.closest('.payment-step-content');
//             const nextStep = document.getElementById(`step${button.dataset.step}`);
//             currentStep.classList.remove('active');
//             nextStep.classList.add('active');
//             updateStepIndicators(button.dataset.step);
//         });
//     });

//     prevButtons.forEach(button => {
//         button.addEventListener('click', () => {
//             const currentStep = button.closest('.payment-step-content');
//             const prevStep = document.getElementById(`step${button.dataset.step}`);
//             currentStep.classList.remove('active');
//             prevStep.classList.add('active');
//             updateStepIndicators(button.dataset.step);
//         });
//     });

//     function updateStepIndicators(currentStep) {
//         const indicators = document.querySelectorAll('.step');
//         indicators.forEach((indicator, index) => {
//             if (index + 1 < currentStep) {
//                 indicator.classList.add('completed');
//                 indicator.classList.remove('active');
//             } else if (index + 1 == currentStep) {
//                 indicator.classList.add('active');
//                 indicator.classList.remove('completed');
//             } else {
//                 indicator.classList.remove('active', 'completed');
//             }
//         });
//     }

//     // File upload
//     const uploadArea = document.getElementById('uploadArea');
//     const fileInput = document.getElementById('fileUpload');
//     const fileList = document.getElementById('fileList');

//     uploadArea.addEventListener('click', () => fileInput.click());

//     uploadArea.addEventListener('dragover', (e) => {
//         e.preventDefault();
//         uploadArea.classList.add('dragover');
//     });

//     uploadArea.addEventListener('dragleave', () => {
//         uploadArea.classList.remove('dragover');
//     });

//     uploadArea.addEventListener('drop', (e) => {
//         e.preventDefault();
//         uploadArea.classList.remove('dragover');
//         handleFiles(e.dataTransfer.files);
//     });

//     fileInput.addEventListener('change', () => {
//         handleFiles(fileInput.files);
//     });

//     function handleFiles(files) {
//         for (let file of files) {
//             const fileItem = document.createElement('li');
//             fileItem.innerHTML = `
//                 <div class="file-info">
//                     <i class="fas fa-file file-icon"></i>
//                     <div>
//                         <div class="file-name">${file.name}</div>
//                         <div class="file-size">${formatFileSize(file.size)}</div>
//                     </div>
//                 </div>
//                 <div class="file-actions">
//                     <button class="remove-file"><i class="fas fa-times"></i></button>
//                 </div>
//             `;
//             fileList.appendChild(fileItem);

//             fileItem.querySelector('.remove-file').addEventListener('click', () => {
//                 fileItem.remove();
//             });
//         }
//     }

//     function formatFileSize(bytes) {
//         if (bytes < 1024) return bytes + ' bytes';
//         else if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
//         else return (bytes / 1048576).toFixed(1) + ' MB';
//     }

//     // Payment tabs
//     const paymentTabs = document.querySelectorAll('.payment-tab');
//     const paymentContents = document.querySelectorAll('.payment-tab-content');

//     paymentTabs.forEach(tab => {
//         tab.addEventListener('click', () => {
//             paymentTabs.forEach(t => t.classList.remove('active'));
//             paymentContents.forEach(c => c.classList.remove('active'));
//             tab.classList.add('active');
//             document.getElementById(`${tab.dataset.tab}-tab`).classList.add('active');
//         });
//     });
// });




document.addEventListener('DOMContentLoaded', function() {
    // Step navigation
    const nextButtons = document.querySelectorAll('.next-step');
    const prevButtons = document.querySelectorAll('.prev-step');
    const steps = document.querySelectorAll('.payment-step-content');

    if (nextButtons && prevButtons && steps) {
        nextButtons.forEach(button => {
            button.addEventListener('click', () => {
                const currentStep = button.closest('.payment-step-content');
                const nextStep = document.getElementById(`step${button.dataset.step}`);
                if (currentStep && nextStep) {
                    currentStep.classList.remove('active');
                    nextStep.classList.add('active');
                    updateStepIndicators(button.dataset.step);
                }
            });
        });

        prevButtons.forEach(button => {
            button.addEventListener('click', () => {
                const currentStep = button.closest('.payment-step-content');
                const prevStep = document.getElementById(`step${button.dataset.step}`);
                if (currentStep && prevStep) {
                    currentStep.classList.remove('active');
                    prevStep.classList.add('active');
                    updateStepIndicators(button.dataset.step);
                }
            });
        });
    }

    function updateStepIndicators(currentStep) {
        const indicators = document.querySelectorAll('.step');
        indicators.forEach((indicator, index) => {
            if (index + 1 < currentStep) {
                indicator.classList.add('completed');
                indicator.classList.remove('active');
            } else if (index + 1 == currentStep) {
                indicator.classList.add('active');
                indicator.classList.remove('completed');
            } else {
                indicator.classList.remove('active', 'completed');
            }
        });
    }

    // File upload
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileUpload');
    const fileList = document.getElementById('fileList');

    if (uploadArea && fileInput && fileList) {
        uploadArea.addEventListener('click', () => fileInput.click());

        uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', () => {
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
            handleFiles(e.dataTransfer.files);
        });

        fileInput.addEventListener('change', () => {
            handleFiles(fileInput.files);
        });

        function handleFiles(files) {
            for (let file of files) {
                const fileItem = document.createElement('li');
                fileItem.innerHTML = `
                    <div class="file-info">
                        <i class="fas fa-file file-icon"></i>
                        <div>
                            <div class="file-name">${file.name}</div>
                            <div class="file-size">${formatFileSize(file.size)}</div>
                        </div>
                    </div>
                    <div class="file-actions">
                        <button class="remove-file"><i class="fas fa-times"></i></button>
                    </div>
                `;
                fileList.appendChild(fileItem);

                fileItem.querySelector('.remove-file').addEventListener('click', () => {
                    fileItem.remove();
                });
            }
        }
    }

    function formatFileSize(bytes) {
        if (bytes < 1024) return bytes + ' bytes';
        else if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
        else return (bytes / 1048576).toFixed(1) + ' MB';
    }

    // Payment tabs
    const paymentTabs = document.querySelectorAll('.payment-tab');
    const paymentContents = document.querySelectorAll('.payment-tab-content');

    if (paymentTabs && paymentContents) {
        paymentTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                paymentTabs.forEach(t => t.classList.remove('active'));
                paymentContents.forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                const activeTab = document.getElementById(`${tab.dataset.tab}-tab`);
                if (activeTab) activeTab.classList.add('active');
            });
        });
    }
});
