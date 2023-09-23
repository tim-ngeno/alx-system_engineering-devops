# Configuration Management (CM)

**Configuration Management (CM)** refers to the systematic approach to maintaining computer systems, servers, and software in a desired and consistent state. It's a discipline applied across both administrative and technical domains to ensure that systems are set up and run consistently over time, across different environments, and even as they evolve. Here's a comprehensive breakdown:

1. **Definition and Purpose:**  
   Configuration Management ensures that the performance, functional, and physical attributes of a system and its components are consistent with the requirements, design, and operational information throughout its lifecycle.

2. **Key Components:**  
   - **Configuration Identification:** Selecting and marking the components to be managed.
   - **Configuration Control:** Implementing a set of management controls (like version control) to make sure changes are made systematically and with the approval of specified authorities.
   - **Configuration Status Accounting:** Keeping a record of the state of the system and changes that have been made over time.
   - **Configuration Auditing:** Regularly checking the system to ensure it's functioning as intended and according to its specifications and requirements.
   - **Configuration Reporting:** Keeping stakeholders informed about the state of the system, any changes made, and the reasons for those changes.

3. **Benefits:**  
   - **Consistency:** Ensures that systems function and perform consistently, irrespective of changes, upgrades, or modifications.
   - **Reproducibility:** Makes it possible to revert systems to previous states or replicate configurations across multiple systems.
   - **Efficiency:** Reduces manual efforts and errors by automating repetitive tasks and ensuring that configurations are correct from the outset.
   - **Accountability:** Tracks changes systematically, making it easier to identify when issues started and who made changes.
   - **Compliance:** Ensures systems adhere to regulatory and organizational standards.

4. **Tools and Software:**  
   Modern Configuration Management often employs software tools to automate many of the processes involved. These tools include:
   - Configuration Management Databases (CMDBs)
   - Infrastructure as Code (IaC) tools like Puppet, Chef, Ansible, and Terraform.

5. **Applications:**  
   While traditionally associated with IT operations, Configuration Management principles are also applied in:
   - Software Development (version control systems like Git)
   - Manufacturing (ensuring products are produced consistently)
   - Any scenario where consistency and control over changes are crucial.


## CM Using Puppet

### Puppet Resource Type: file

To manage files using Puppet, you can use the `file` resource type. Here's an example:

```puppet
file { '/tmp/example':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'root',
  group   => 'root',
  content => 'Hello, Puppet!',
}
```

More resource types in the [official documentation](https://puppet.com/docs/puppet/latest/type.html).

### Puppet's Declarative Language

Puppet uses a declarative language which focuses on modeling the desired state of a system rather than scripting the steps to reach that state. This allows for idempotent and consistent configuration management.

```puppet
# This is a declarative way to ensure a service is running
service { 'nginx':
  ensure => 'running',
}
```

### Puppet lint

Puppet lint is a tool to check your Puppet code for stylistic and structural correctness. To use it, run:

```bash
puppet-lint /path/to/your/manifest.pp
```

### Puppet emacs mode

For those using the Emacs text editor, there's a Puppet mode to aid in writing and editing Puppet manifests. Once installed, Puppet code will be highlighted and properly indented, making it easier to read and write.

```emacs-lisp
;; To enable puppet mode in emacs
(require 'puppet-mode)
(add-to-list 'auto-mode-alist '("\\.pp\\'" . puppet-mode))
```


### Advanced Puppet Techniques

#### Puppet Templating with EPP and ERB

Puppet allows you to use templates to dynamically generate file content. These templates can be written in ERB (Embedded Ruby) or EPP (Embedded Puppet). Here's a basic example of each:

**ERB Example:**
```erb
<% if @hostname == 'webserver' %>
Welcome to the web server!
<% else %>
Welcome to <%= @hostname %>!
<% end %>
```

**EPP Example:**
```epp
<% if $hostname == 'webserver' { %>
Welcome to the web server!
<% } else { %>
Welcome to <%= $hostname %>!
<% } %>
```

#### Puppet Modules

Modules are self-contained bundles of code and data. They help in organizing your Puppet code and making it reusable. Here's how you can structure a basic module:

```plaintext
/my_module/
|-- manifests/
|   |-- init.pp
|-- files/
|-- templates/
|-- metadata.json
```


#### Puppet Debugging and Troubleshooting

When working with Puppet, it's inevitable to run into issues. The `--debug` flag can provide detailed information about the Puppet run:

```bash
puppet apply --debug /path/to/manifest.pp
```

#### Puppet Forge

[Puppet Forge](https://forge.puppet.com/) is a repository of modules written by the community. It's a great resource to find ready-to-use modules for various tasks.

```bash
# Example: Installing a module from Puppet Forge
puppet module install author-module_name
```


In conclusion, Configuration Management is about ensuring stability, consistency, and systematic change control in systems or products, enabling organizations to operate more efficiently and mitigate risks associated with changes.
