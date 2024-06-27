(function() {
    function findScratchVm() {
        const possiblePaths = [
            'window.vm',
            'window.scratchVm',
            'window.Scratch.vm',
            'window.ScratchJr.vm',
            'window.vmManager.vm',
            'window.vmManager.scratchVm',
            'window.VM797'
        ];

        // Try common paths first
        for (const path of possiblePaths) {
            const vm = path.split('.').reduce((obj, prop) => obj && obj[prop], window);
            if (vm && vm.runtime) {
                return vm;
            }
        }

        // Fall back to scanning window properties
        for (const key in window) {
            if (window.hasOwnProperty(key) && window[key] && window[key].runtime) {
                return window[key];
            }
        }

        return null;
    }

    const vm = findScratchVm();

    if (!vm) {
        console.error("Scratch VM instance not found. Ensure you're on a Scratch project page and try again.");
        return;
    }

    // Function to get a variable by name
    function getVariable(name) {
        const target = vm.runtime.targets.find(t => t.isStage);
        if (!target) {
            console.error("Stage target not found.");
            return null;
        }
        const variable = Object.values(target.variables).find(v => v.name === name);
        return variable ? variable.value : null;
    }

    // Function to set a variable by name
    function setVariable(name, value) {
        const target = vm.runtime.targets.find(t => t.isStage);
        if (!target) {
            console.error("Stage target not found.");
            return;
        }
        const variable = Object.values(target.variables).find(v => v.name === name);
        if (variable) {
            variable.value = value;
            vm.runtime.requestRedraw();
        } else {
            console.error(`Variable "${name}" not found.`);
        }
    }

    // Example usage
    setVariable("ScrollX", 0);
})();
