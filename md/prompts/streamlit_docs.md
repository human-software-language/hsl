Structure:
[develop]

- \_index.md
  [tutorials]
  - \_index.md
    [multipage-apps]
    - custom-navigation.md
    - \_index.md
      [databases]
    - tigergraph.md
    - mssql.md
    - bigquery.md
    - tableau.md
    - gcs.md
    - public-gsheet.md
    - detabase.md
    - snowflake.md
    - tidb.md
    - \_index.md
    - mysql.md
    - private-gsheet.md
    - aws-s3.md
    - postgresql.md
    - supabase.md
    - mongodb.md
      [execution-flow]
    - \_index.md
      [fragments]
      - create-a-multiple-container-fragment.md
      - trigger-a-full-script-rerun-from-a-fragment.md
      - start-and-stop-fragment-auto-reruns.md
        [llms]
    - conversational-apps.md
    - \_index.md
    - llm-quickstart.md
      [quick-references]
  - prerelease-features.md
  - api-cheat-sheet.md
  - \_index.md
  - changelog.md
    [api-reference]
  - \_index.md
    [command-line]
    - run.md
    - \_index.md
      [control-flow]
    - form_submit_button.md
    - experimental_rerun.md
    - rerun.md
    - fragment.md
    - \_index.md
    - form.md
    - stop.md
      [widgets]
    - button.md
    - select_slider.md
    - radio.md
    - selectbox.md
    - slider.md
    - page_link.md
    - text_input.md
    - download_button.md
    - camera_input.md
    - link_button.md
    - multiselect.md
    - toggle.md
    - number_input.md
    - color_picker.md
    - text_area.md
    - checkbox.md
    - \_index.md
    - date_input.md
    - time_input.md
    - file_uploader.md
      [text]
    - echo.md
    - markdown.md
    - caption.md
    - header.md
    - subheader.md
    - divider.md
    - \_index.md
    - latex.md
    - text.md
    - title.md
    - code.md
      [chat]
    - chat-input.md
    - chat-message.md
    - \_index.md
      [connections]
    - connections-sql.md
    - connections-snowflake.md
    - secrets-toml.md
    - secrets.md
    - connections-baseconnection.md
    - connections-snowpark.md
    - connections-experimentalbaseconnection.md
    - connection.md
    - experimental-connection.md
    - \_index.md
      [write-magic]
    - write_stream.md
    - write.md
    - magic.md
    - \_index.md
      [status]
    - warning.md
    - progress.md
    - snow.md
    - exception.md
    - error.md
    - spinner.md
    - success.md
    - toast.md
    - \_index.md
    - info.md
    - status.md
    - balloons.md
      [navigation]
    - \_index.md
    - switch_page.md
      [media]
    - video.md
    - audio.md
    - \_index.md
    - image.md
      [data]
    - experimental_data_editor.md
    - table.md
    - dataframe.md
    - \_index.md
    - data_editor.md
    - metric.md
    - json.md
      [column_config]
      - barchartcolumn.md
      - checkboxcolumn.md
      - selectboxcolumn.md
      - linechartcolumn.md
      - column.md
      - datecolumn.md
      - textcolumn.md
      - datetimecolumn.md
      - areachartcolumn.md
      - linkcolumn.md
      - numbercolumn.md
      - listcolumn.md
      - \_index.md
      - timecolumn.md
      - progresscolumn.md
      - imagecolumn.md
        [utilities]
    - experimental-user.md
    - \_index.md
    - html.md
    - help.md
      [charts]
    - line_chart.md
    - scatter_chart.md
    - graphviz_chart.md
    - altair_chart.md
    - bokeh_chart.md
    - pyplot.md
    - plotly_chart.md
    - area_chart.md
    - bar_chart.md
    - map.md
    - pydeck_chart.md
    - \_index.md
    - vega_lite_chart.md
      [configuration]
    - config-toml.md
    - \_index.md
    - set_page_config.md
      [caching-and-state]
    - experimental_get_query_params.md
    - cache-data.md
    - cache.md
    - query_params.md
    - experimental-singleton.md
    - cache-resource.md
    - experimental-memo.md
    - \_index.md
    - session_state.md
    - experimental_set_query_params.md
      [custom-components]
    - iframe.md
    - declare_component.md
    - \_index.md
    - html.md
      [concepts]
  - \_index.md
    [multipage-apps]
    - \_index.md
    - page_directory.md
      [connections]
    - secrets-management.md
    - \_index.md
    - connecting-to-data.md
    - security-reminders.md
      [architecture]
    - app-chrome.md
    - old_caching.md
    - fragments.md
    - caching.md
    - old_cache_primitives.md
    - run-your-app.md
    - session-state.md
    - architecture.md
    - forms.md
    - \_index.md
    - widget-behavior.md
      [app-design]
    - animate-elements.md
    - custom-classes.md
    - button-behavior-and-examples.md
    - timezone-handling.md
    - \_index.md
    - dataframes.md
      [configuration]
    - options.md
    - theming.md
    - static-file-serving.md
    - https.md
    - \_index.md
      [custom-components]
    - limitations.md
    - \_index.md
    - create-component.md
    - publish-component.md
    - components-api.md

Files:
File: \_index.md

```
---
title: Develop
slug: /develop
---

# Develop

Get all the information you need to build beautiful, performant web apps with Streamlit!

<InlineCalloutContainer>
    <InlineCallout
        color="indigo-70"
        icon="book"
        bold="Concepts."
        href="/develop/concepts"
    >Learn how Streamlit works with in-depth guides to our execution model and features.</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="list"
        bold="API reference."
        href="/develop/api-reference"
    >Learn about our API with function definitions and examples.</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="auto_awesome"
        bold="Tutorials."
        href="/develop/tutorials"
    >Follow step-by-step instructions to build example apps and useful snippets.</InlineCallout>
    <InlineCallout
        color="indigo-70"
        icon="bolt"
        bold="Quick references."
        href="/develop/quick-reference"
    >Check out our quick references for easy access to convenient information like our changelog, cheat sheet, pre-release features, and roadmap.</InlineCallout>
</InlineCalloutContainer>

```

File: tutorials/\_index.md

```
---
title: Tutorials
slug: /develop/tutorials
---

# Tutorials

Our tutorials include step-by-step examples of building different types of apps in Streamlit.

<TileContainer layout="list">

<RefCard href="/develop/tutorials/execution-flow">

<h5>Use core features to work with Streamlit's execution model</h5>

Build simple apps and walk through examples to learn about Streamlit's core features and execution model.

</RefCard>

<RefCard href="/develop/tutorials/databases">

<h5>Connect to data sources</h5>

Connect to popular datasources.

</RefCard>

<RefCard href="/develop/tutorials/multipage">

<h5>Create multipage apps</h5>

Create multipage apps, navigation, and flows.

</RefCard>

<RefCard href="/develop/tutorials/llms">

<h5>Chat apps and LLMs</h5>

Work with LLMs and create chat apps.

</RefCard>

</TileContainer>

When you're done developing your app, see our [deployment tutorials](/deploy/tutorials), too!

```

File: tutorials/multipage-apps/custom-navigation.md

```
---
title: Build a custom navigation menu with `st.page_link`
slug: /develop/tutorials/multipage/st.page_link-nav
description: Streamlit makes it easy to build a custom navigation menu in your multipage app.
---

# Build a custom navigation menu with `st.page_link`

Streamlit lets you build custom navigation menus and elements with `st.page_link`. Introduced in Streamlit version 1.31.0, `st.page_link` can link to other pages in your multipage app or to external sites. When linked to another page in your app, `st.page_link` will show a highlight effect to indicate the current page. When combined with the [`client.showSidebarNavigation`](/develop/concepts/configuration#client) configuration option, you can build sleek, dynamic navigation in your app.

## Prerequisites

Create a new working directory in your development environment. We'll call this directory `your-repository`.

## Summary

In this example, we'll build a dynamic navigation menu for a multipage app that depends on the current user's role. We've abstracted away the use of username and creditials to simplify the example. Instead, we'll use a selectbox on the main page of the app to switch between roles. Session State will carry this selection between pages. The app will have a main page (`app.py`) which serves as the abstracted log-in page. There will be three additional pages which will be hidden or accessible, depending on the current role. The file structure will be as follows:

```

your-repository/
Γö£ΓöÇΓöÇ .streamlit/
Γöé ΓööΓöÇΓöÇ config.toml
Γö£ΓöÇΓöÇ pages/
Γöé Γö£ΓöÇΓöÇ admin.py
Γöé Γö£ΓöÇΓöÇ super-admin.py
Γöé ΓööΓöÇΓöÇ user.py
Γö£ΓöÇΓöÇ menu.py
ΓööΓöÇΓöÇ app.py

````

Here's a look at what we'll build:

<Cloud src="https://doc-custom-navigation.streamlit.app/?embed=true" height="400" />

## Build the example

### Hide the default sidebar navigation

When creating a custom navigation menu, you need to hide the default sidebar navigation using `client.showSidebarNavigation`. Add the following `.streamlit/config.toml` file to your working directory:

```toml
[client]
showSidebarNavigation = false
````

### Create a menu function

You can write different menu logic for different pages or you can create a single menu function to call on multiple pages. In this example, we'll use the same menu logic on all pages, including a redirect to the main page when a user isn't logged in. We'll build a few helper functions to do this.

- `menu_with_redirect()` checks if a user is logged in, then either redirects them to the main page or renders the menu.
- `menu()` will call the correct helper function to render the menu based on whether the user is logged in or not.
- `authenticated_menu()` will display a menu based on an authenticated user's role.
- `unauthenticated_menu()` will display a menu for unauthenticated users.

We'll call `menu()` on the main page and call `menu_with_redirect()` on the other pages. `st.session_state.role` will store the current selected role. If this value does not exist or is set to `None`, then the user is not logged in. Otherwise, it will hold the user's role as a string: `"user"`, `"admin"`, or `"super-admin"`.

Add the following `menu.py` file to your working directory. (We'll describe the functions in more detail below.)

```python
import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
```

Let's take a closer look at `authenticated_menu()`. When this function is called, `st.session_state.role` exists and has a value other than `None`.

```python
def authenticated_menu():
    # Show a navigation menu for authenticated users
```

The first two pages in the navigation menu are available to all users. Since we know a user is logged in when this function is called, we'll use the label "Switch accounts" for the main page. (If you don't use the `label` parameter, the page name will be derived from the file name like it is with the default sidebar navigation.)

```python
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
```

We only want to show the next two pages to admins. Furthermore, we've chosen to disable&mdash;but not hide&mdash;the super-admin page when the admin user is not a super-admin. We do this using the `disabled` parameter. (`disabled=True` when the role is not `"super-admin"`.)

```
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )
```

It's that simple! `unauthenticated_menu()` will only show a link to the main page of the app with the label "Log in." `menu()` does a simple inspection of `st.session_state.role` to switch between the two menu-rendering functions. Finally, `menu_with_redirect()` extends `menu()` to redirect users to `app.py` if they aren't logged in.

<Tip>

If you want to include emojis in your page labels, you can use the `icon` parameter. There's no need to include emojis in your file name or the `label` parameter.

</Tip>

### Create the main file of your app

The main `app.py` file will serve as a pseudo-login page. The user can choose a role from the `st.selectbox` widget. A few bits of logic will save that role into Session State to preserve it while navigating between pages&mdash;even when returning to `app.py`.

Add the following `app.py` file to your working directory:

```python
import streamlit as st
from menu import menu

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)
menu() # Render the dynamic menu!
```

### Add other pages to your app

Add the following `pages/user.py` file:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

Session State resets if a user manually navigates to a page by URL. Therefore, if a user tries to access an admin page in this example, Session State will be cleared, and they will be redirected to the main page as an unauthenicated user. However, it's still good practice to include a check of the role at the top of each restricted page. You can use `st.stop` to halt an app if a role is not whitelisted.

`pages/admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

`pages/super-admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to super-admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

As noted above, the redirect in `menu_with_redirect()` will prevent a user from ever seeing the warning messages on the admin pages. If you want to see the warning, just add another `st.page_link("pages/admin.py")` button at the bottom of `app.py` so you can navigate to the admin page after selecting the "user" role. ≡ƒÿë

```

File: tutorials/multipage-apps/_index.md
```

---

title: Build multipage apps
slug: /develop/tutorials/multipage

---

# Build multipage apps

<TileContainer layout="list">

<RefCard href="/develop/tutorials/multipage/st.page_link-nav">

<h5>Build a custom navigation menu with `st.page_link`</h5>

Create a dynamic, user-dependant navigation menu to replace the default sidebar navigation.

</RefCard>

</TileContainer>

```

File: tutorials/databases/tigergraph.md
```

---

title: Connect Streamlit to TigerGraph
slug: /develop/tutorials/databases/tigergraph

---

# Connect Streamlit to TigerGraph

## Introduction

This guide explains how to securely access a TigerGraph database from Streamlit Community Cloud. It uses the [pyTigerGraph](https://pytigergraph.github.io/pyTigerGraph/GettingStarted/) library and Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create a TigerGraph Cloud Database

First, follow the official tutorials to create a TigerGraph instance in TigerGraph Cloud, either as a [blog](https://www.tigergraph.com/blog/getting-started-with-tigergraph-3-0/) or a [video](https://www.youtube.com/watch?v=NtNW2e8MfCQ). Note your username, password, and subdomain.

For this tutorial, we will be using the COVID-19 starter kit. When setting up your solution, select the ΓÇ£COVID-19 Analysis" option.

![TG_Cloud_COVID19](/images/databases/tigergraph-1.png)

Once it is started, ensure your data is downloaded and queries are installed.

![TG_Cloud_Schema](/images/databases/tigergraph-2.png)

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your appΓÇÖs root directory. Create this file if it doesnΓÇÖt exist yet and add your TigerGraph Cloud instance username, password, graph name, and subdomain as shown below:

```toml
# .streamlit/secrets.toml

[tigergraph]
host = "https://xxx.i.tgcloud.io/"
username = "xxx"
password = "xxx"
graphname = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on Edit Secrets. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add PyTigerGraph to your requirements file

Add the pyTigerGraph package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
pyTigerGraph==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your graph and query.

```python
# streamlit_app.py

import streamlit as st
import pyTigerGraph as tg

# Initialize connection.
conn = tg.TigerGraphConnection(**st.secrets["tigergraph"])
conn.apiToken = conn.getToken(conn.createSecret())

# Pull data from the graph by running the "mostDirectInfections" query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    most_infections = conn.runInstalledQuery("mostDirectInfections")[0]["Answer"][0]
    return most_infections["v_id"], most_infections["attributes"]

items = get_data()

# Print results.
st.title(f"Patient {items[0]} has the most direct infections")
for key, val in items[1].items():
    st.write(f"Patient {items[0]}'s {key} is {val}.")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example data we created above), your app should look like this:

![Final_App](/images/databases/tigergraph-3.png)

```

File: tutorials/databases/mssql.md
```

---

title: Connect Streamlit to Microsoft SQL Server
slug: /develop/tutorials/databases/mssql

---

# Connect Streamlit to Microsoft SQL Server

## Introduction

This guide explains how to securely access a **_remote_** Microsoft SQL Server database from Streamlit Community Cloud. It uses the [pyodbc](https://github.com/mkleehammer/pyodbc/wiki) library and Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create an SQL Server database

<Note>

If you already have a remote database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow the Microsoft documentation to install [SQL Server](https://docs.microsoft.com/en-gb/sql/sql-server/?view=sql-server-ver15) and the `sqlcmd` [Utility](https://docs.microsoft.com/en-gb/sql/tools/sqlcmd-utility?view=sql-server-ver15). They have detailed installation guides on how to:

- [Install SQL Server on Windows](https://docs.microsoft.com/en-gb/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver15)
- [Install on Red Hat Enterprise Linux](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-red-hat?view=sql-server-ver15)
- [Install on SUSE Linux Enterprise Server](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-suse?view=sql-server-ver15)
- [Install on Ubuntu](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15)
- [Run on Docker](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15)
- [Provision a SQL VM in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sql/provision-sql-server-linux-virtual-machine?toc=/sql/toc/toc.json)

Once you have SQL Server installed, note down your SQL Server name, username, and password during setup.

## Connect locally

If you are connecting locally, use `sqlcmd` to connect to your new local SQL Server instance.

1. In your terminal, run the following command:

   ```bash
   sqlcmd -S localhost -U SA -P '<YourPassword>'
   ```

   As you are connecting locally, the SQL Server name is `localhost`, the username is `SA`, and the password is the one you provided during the SA account setup.

2. You should see a **sqlcmd** command prompt `1>`, if successful.

3. If you run into a connection failure, review Microsoft's connection troubleshooting recommendations for your OS ([Linux](https://docs.microsoft.com/en-gb/sql/linux/sql-server-linux-troubleshooting-guide?view=sql-server-ver15#connection) & [Windows](https://docs.microsoft.com/en-gb/sql/linux/sql-server-linux-troubleshooting-guide?view=sql-server-ver15#connection)).

<Tip>

When connecting remotely, the SQL Server name is the machine name or IP address. You might also need to open the SQL Server TCP port (default 1433) on your firewall.

</Tip>

### Create a SQL Server database

By now, you have SQL Server running and have connected to it with `sqlcmd`! ≡ƒÑ│ Let's put it to use by creating a database containing a table with some example values.

1. From the `sqlcmd` command prompt, run the following Transact-SQL command to create a test database `mydb`:

   ```sql
   CREATE DATABASE mydb
   ```

2. To execute the above command, type `GO` on a new line:

   ```sql
   GO
   ```

### Insert some data

Next create a new table, `mytable`, in the `mydb` database with three columns and two rows.

1. Switch to the new `mydb` database:

   ```sql
   USE mydb
   ```

2. Create a new table with the following schema:

   ```sql
   CREATE TABLE mytable (name varchar(80), pet varchar(80))
   ```

3. Insert some data into the table:

   ```sql
   INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird')
   ```

4. Type `GO` to execute the above commands:

   ```sql
   GO
   ```

To end your **sqlcmd** session, type `QUIT` on a new line.

### Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the SQL Server name, database name, username, and password as shown below:

```toml
# .streamlit/secrets.toml

server = "localhost"
database = "mydb"
username = "SA"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **server**, **database**, **username**, and **password** with those of your _remote_ SQL Server!

And add this file to `.gitignore` and don't commit it to your GitHub repo.

</Important>

## Copy your app secrets to Streamlit Community Cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add pyodbc to your requirements file

To connect to SQL Server _locally_ with Streamlit, you need to `pip install pyodbc`, in addition to the Microsoft ODBC driver you installed during the SQL Server installation.

On _Streamlit Cloud_, we have built-in support for SQL Server. On popular demand, we directly added SQL Server tools including the ODBC drivers and the executables `sqlcmd` and `bcp` to the container image for Cloud apps, so you don't need to install them.

All you need to do is add the [`pyodbc`](https://github.com/mkleehammer/pyodbc) Python package to your `requirements.txt` file, and you're ready to go! ≡ƒÄê

```bash
# requirements.txt
pyodbc==x.x.x
```

Replace `x.x.x` Γÿ¥∩╕Å with the version of pyodbc you want installed on Cloud.

<Note>

At this time, Streamlit Community Cloud does not support Azure Active Directory authentication. We will update this tutorial when we add support for Azure Active Directory.

</Note>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
import streamlit as st
import pyodbc

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

```

File: tutorials/databases/bigquery.md
```

---

title: Connect Streamlit to Google BigQuery
slug: /develop/tutorials/databases/bigquery

---

# Connect Streamlit to Google BigQuery

## Introduction

This guide explains how to securely access a BigQuery database from Streamlit Community Cloud. It uses the
[google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) library and
Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create a BigQuery database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#enable-the-bigquery-api).

</Note>

For this example, we will use one of the [sample datasets](https://cloud.google.com/bigquery/public-data#sample_tables) from BigQuery (namely the `shakespeare` table). If you want to create a new dataset instead, follow [Google's quickstart guide](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui).

## Enable the BigQuery API

Programmatic access to BigQuery is controlled through [Google Cloud Platform](https://cloud.google.com). Create an account or sign in and head over to the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). As shown below, search for the BigQuery API and enable it:

<Flex>
<Image alt="Bigquery screenshot 1" src="/images/databases/big-query-1.png" />
<Image alt="Bigquery screenshot 2" src="/images/databases/big-query-2.png" />
<Image alt="Bigquery screenshot 3" src="/images/databases/big-query-3.png" />
</Flex>

## Create a service account & key file

To use the BigQuery API from Streamlit Community Cloud, you need a Google Cloud Platform service account (a special account type for programmatic data access). Go to the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page and create an account with the **Viewer** permission (this will let the account access data but not change it):

<Flex>
<Image alt="Bigquery screenshot 4" src="/images/databases/big-query-4.png" />
<Image alt="Bigquery screenshot 5" src="/images/databases/big-query-5.png" />
<Image alt="Bigquery screenshot 6" src="/images/databases/big-query-6.png" />
</Flex>

<Note>

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

</Note>

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

<Flex>
<Image alt="Bigquery screenshot 7" src="/images/databases/big-query-7.png" />
<Image alt="Bigquery screenshot 8" src="/images/databases/big-query-8.png" />
<Image alt="Bigquery screenshot 9" src="/images/databases/big-query-9.png" />
</Flex>

## Add the key file to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root
directory. Create this file if it doesn't exist yet and add the content of the key file you just
downloaded to it as shown below:

```toml
# .streamlit/secrets.toml

[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add google-cloud-bigquery to your requirements file

Add the [google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version want installed):

```bash
# requirements.txt
google-cloud-bigquery==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the query if you don't use the sample table.

```python
# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

# Print results.
st.write("Some wise words from Shakespeare:")
for row in rows:
    st.write("Γ£ì∩╕Å " + row['word'])
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

Alternatively, you can use pandas to read from BigQuery right into a dataframe! Follow all the above steps, install the [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/index.html) library (don't forget to add it to `requirements.txt`!), and call `pandas.read_gbq(query, credentials=credentials)`. More info [in the pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.read_gbq.html).

If everything worked out (and you used the sample table), your app should look like this:

![Final app screenshot](/images/databases/big-query-10.png)

```

File: tutorials/databases/tableau.md
```

---

title: Connect Streamlit to Tableau
slug: /develop/tutorials/databases/tableau

---

# Connect Streamlit to Tableau

## Introduction

This guide explains how to securely access data on Tableau from Streamlit Community Cloud. It uses the [tableauserverclient](https://tableau.github.io/server-client-python/#) library and Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create a Tableau site

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#create-personal-access-tokens).

</Note>

For simplicity, we are using the cloud version of Tableau here but this guide works equally well for self-hosted deployments. First, sign up for [Tableau Online](https://www.tableau.com/products/cloud-bi) or log in. Create a workbook or run one of the example workbooks under "Dashboard Starters".

![Tableau screenshot 1](/images/databases/tableau-1.png)

## Create personal access tokens

While the Tableau API allows authentication via username and password, you should use [personal access tokens](https://help.tableau.com/current/server/en-us/security_personal_access_tokens.htm) for a production app.

Go to your [Tableau Online homepage](https://online.tableau.com/), create an access token and note down the token name and secret.

<Flex>
<Image alt="Tableau screenshot 2" src="/images/databases/tableau-2.png" />
<Image alt="Tableau screenshot 3" src="/images/databases/tableau-3.png" />
</Flex>

<Note>

Personal access tokens will expire if not used after 15 consecutive days.

</Note>

## Add token to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add your token, the site name you created during setup, and the URL of your Tableau server like below:

```toml
# .streamlit/secrets.toml

[tableau]
token_name = "xxx"
token_secret = "xxx"
server_url = "https://abc01.online.tableau.com/"
site_id = "streamlitexample"  # in your site's URL behind the server_url
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add tableauserverclient to your requirements file

Add the [tableauserverclient](https://tableau.github.io/server-client-python/#) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
tableauserverclient==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Note that this code just shows a few options of data you can get ΓÇô explore the [tableauserverclient](https://tableau.github.io/server-client-python/#) library to find more!

```python
# streamlit_app.py

import streamlit as st
import tableauserverclient as TSC


# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["token_name"],
    st.secrets["tableau"]["personal_access_token"],
    st.secrets["tableau"]["site_id"],
)
server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)


# Get various data.
# Explore the tableauserverclient library for more options.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query():
    with server.auth.sign_in(tableau_auth):

        # Get all workbooks.
        workbooks, pagination_item = server.workbooks.get()
        workbooks_names = [w.name for w in workbooks]

        # Get views for first workbook.
        server.workbooks.populate_views(workbooks[0])
        views_names = [v.name for v in workbooks[0].views]

        # Get image & CSV for first view of first workbook.
        view_item = workbooks[0].views[0]
        server.views.populate_image(view_item)
        server.views.populate_csv(view_item)
        view_name = view_item.name
        view_image = view_item.image
        # `view_item.csv` is a list of binary objects, convert to str.
        view_csv = b"".join(view_item.csv).decode("utf-8")

        return workbooks_names, views_names, view_name, view_image, view_csv

workbooks_names, views_names, view_name, view_image, view_csv = run_query()


# Print results.
st.subheader("≡ƒôô Workbooks")
st.write("Found the following workbooks:", ", ".join(workbooks_names))

st.subheader("≡ƒæü∩╕Å Views")
st.write(
    f"Workbook *{workbooks_names[0]}* has the following views:",
    ", ".join(views_names),
)

st.subheader("≡ƒû╝∩╕Å Image")
st.write(f"Here's what view *{view_name}* looks like:")
st.image(view_image, width=300)

st.subheader("≡ƒôè Data")
st.write(f"And here's the data for view *{view_name}*:")
st.write(pd.read_csv(StringIO(view_csv)))
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out, your app should look like this (can differ based on your workbooks):

![Tableau screenshot 4](/images/databases/tableau-4.png)

```

File: tutorials/databases/gcs.md
```

---

title: Connect Streamlit to Google Cloud Storage
slug: /develop/tutorials/databases/gcs

---

# Connect Streamlit to Google Cloud Storage

## Introduction

This guide explains how to securely access files on Google Cloud Storage from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [gcsfs](https://github.com/fsspec/gcsfs) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create a Google Cloud Storage bucket and add a file

<Note>

If you already have a bucket that you want to use, feel free
to [skip to the next step](#enable-the-google-cloud-storage-api).

</Note>

First, [sign up for Google Cloud Platform](https://console.cloud.google.com/) or log in. Go to the [Google Cloud Storage console](https://console.cloud.google.com/storage/) and create a new bucket.

<Flex>
<Image alt="GCS screenshot 1" src="/images/databases/gcs-1.png" />
<Image alt="GCS screenshot 2" src="/images/databases/gcs-2.png" />
</Flex>

Navigate to the upload section of your new bucket:

<Flex>
<Image alt="GCS screenshot 3" src="/images/databases/gcs-3.png" />
<Image alt="GCS screenshot 4" src="/images/databases/gcs-4.png" />
</Flex>

And upload the following CSV file, which contains some example data:

<Download href="/images/databases/myfile.csv">myfile.csv</Download>

## Enable the Google Cloud Storage API

The Google Cloud Storage API is [enabled by default](https://cloud.google.com/service-usage/docs/enabled-service#default) when you create a project through the Google Cloud Console or CLI. Feel free to [skip to the next step](#create-a-service-account-and-key-file).

If you do need to enable the API for programmatic access in your project, head over to the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). Search for the Cloud Storage API and enable it. The screenshot below has a blue "Manage" button and indicates the "API is enabled" which means no further action needs to be taken. This is very likely what you have since the API is enabled by default. However, if that is not what you see and you have an "Enable" button, you'll need to enable the API:

<Flex>
<Image alt="GCS screenshot 5" src="/images/databases/gcs-5.png" />
<Image alt="GCS screenshot 6" src="/images/databases/gcs-6.png" />
<Image alt="GCS screenshot 7" src="/images/databases/gcs-7.png" />
</Flex>

## Create a service account and key file

To use the Google Cloud Storage API from Streamlit, you need a Google Cloud Platform service account (a special type for programmatic data access). Go to the Service Accounts page and create an account with <b>Viewer</b> permission.

<Flex>
<Image alt="GCS screenshot 8" src="/images/databases/gcs-8.png" />
<Image alt="GCS screenshot 9" src="/images/databases/gcs-9.png" />
<Image alt="GCS screenshot 10" src="/images/databases/gcs-10.png" />
</Flex>

<Note>

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

</Note>

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

<Flex>
<Image alt="GCS screenshot 11" src="/images/databases/gcs-11.png" />
<Image alt="GCS screenshot 12" src="/images/databases/gcs-12.png" />
<Image alt="GCS screenshot 13" src="/images/databases/gcs-13.png" />
</Flex>

## Add the key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the access key to it as shown below:

```toml
# .streamlit/secrets.toml

[connections.gcs]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add FilesConnection and gcsfs to your requirements file

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [gcsfs](https://github.com/fsspec/gcsfs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
gcsfs==x.x.x
st-files-connection
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables.

```python
# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('gcs', type=FilesConnection)
df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

```

File: tutorials/databases/public-gsheet.md
```

---

title: Connect Streamlit to a public Google Sheet
slug: /develop/tutorials/databases/public-gsheet

---

# Connect Streamlit to a public Google Sheet

## Introduction

This guide explains how to securely access a public Google Sheet from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

This method requires you to enable link sharing for your Google Sheet. While the sharing link will not appear in your code (and actually acts as sort of a password!), someone with the link can get all the data in the Sheet. If you don't want this, follow the (more complicated) guide to [Connect Streamlit to a private Google Sheet](private-gsheet).

### Prerequisites

This tutorial requires `streamlit>=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet and turn on link sharing

If you already have a Sheet that you want to access, feel free to [skip to the next step](#add-the-sheets-url-to-your-local-app-secrets). See Google's documentation on how to [share spreadsheets](https://support.google.com/docs/answer/9331169?hl=en#6.1) for more information.

Create a spreadsheet with this example data and create a share link. The link should have "Anyone with the link" set as a "Viewer."

<div style={{ maxWidth: '200px', margin: 'auto' }}>

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

<Flex>
<Image alt="screenshot 1" src="/images/databases/public-gsheet-1.png" />
<Image alt="screenshot 1" src="/images/databases/public-gsheet-2.png" />
</Flex>

## Add the Sheets URL to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the share link of your Google Sheet to it as shown below:

```toml
# .streamlit/secrets.toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `.read()` results are cached without expiring. You can pass optional parameters to `.read()` to customize your connection. For example, you can specify the name of a worksheet, cache expiration time, or pass-through parameters for [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) like this:

```python
df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)
```

In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching). We've declared optional parameters `usecols=[0,1]` and `nrows=3` for `pandas` to use under the hood.

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connecting to a Google Sheet from Community Cloud

This tutorial assumes a local Streamlit app, however you can also connect to Google Sheets from apps hosted in Community Cloud. The main additional steps are:

- [Include information about dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) using a `requirements.txt` file with `st-gsheets-connection` and any other dependencies.
- [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#deploy-an-app-and-set-up-secrets) to your Community Cloud app.

```

File: tutorials/databases/detabase.md
```

---

title: Connect Streamlit to Deta Base
slug: /develop/tutorials/databases/deta-base

---

# Connect Streamlit to Deta Base

## Introduction

This guide explains how to securely access and write to a [Deta Base](https://deta.space/docs/en/reference/base/about) database from Streamlit Community Cloud. Deta Base is a fully-managed and fast NoSQL database with a focus on end-user simplicity. The data is stored in your own "personal cloud" on [Deta Space](https://deta.space/developers). This guide uses the [Deta Python SDK](https://github.com/deta/deta-python) for Deta Base and Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create an account and sign in to Deta Space

First, you need to [create a Deta Space account](https://deta.space/signup?dev_mode=true) for using Deta Base. Make sure the "Developer Mode" option is enabled when signing up. Once you have an account, sign in to Deta Space. After signing in, open the Collections app by clicking on it.

[Deta Collections](https://deta.space/manual/features/collections#what-are-collections) is a pre-installed app on Space that stores different types of data that can be connected to other apps or services.
<Image alt="Deta Space Canvas" src="/images/databases/deta-1.png" caption="Deta Space Canvas" />

Now click on the **Get Started** button and then click on the **Create Collection** button after giving your Collection a name.
<Image alt="Create a New Collection" src="/images/databases/deta-2.png" caption="Create a New Collection" />

After that, click on the **Collection Settings** option in the top corner, which will show the modal for creating a **Data Key**. Click on the **Create New Data Key** button, then give your key a name, and click the **Generate** button. Copy the key shown to your clipboard by clicking on the copy button.

[Data Keys](https://deta.space/docs/en/basics/extending_apps#data-keys) allow you to read and manipulate data within your Collections.
<Image alt="Generate Data Key" src="/images/databases/deta-3.png" caption="Generate Data Key" />

Be sure to store your **Data Key** securely. It is shown only once, and you will need it to connect to your Deta Base.

## Add Data Key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the **Data Key** (from the previous step) of your Deta Base as shown below:

```toml
# .streamlit/secrets.toml
data_key = "xxx"
```

Replace `xxx` above Γÿ¥∩╕Å with your **Data Key** from the previous step.

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add deta to your requirements file

Add the [deta](https://github.com/deta/deta-python) Python SDK for Deta Base to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
deta==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. The example app below writes data from a Streamlit form to a Deta Base database `example-db`.

```python
import streamlit as st
from deta import Deta

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("example-db")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)
```

If everything worked out (and you used the example we created above), your app should look like this:

![Finished app GIF](/images/databases/deta_app.gif)

```

File: tutorials/databases/snowflake.md
```

---

title: Connect Streamlit to Snowflake
slug: /develop/tutorials/databases/snowflake

---

# Connect Streamlit to Snowflake

## Introduction

This guide explains how to securely access a Snowflake database from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), the [Snowpark library](https://docs.snowflake.com/en/developer-guide/snowpark/python/index) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code **will only work on Streamlit version >= 1.28**, when `st.connection` was added.

## Create a Snowflake database

<Note>

If you already have a database that you want to use, feel free to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, [sign up for Snowflake](https://signup.snowflake.com/) and log into the [Snowflake web interface](https://docs.snowflake.com/en/user-guide/connecting.html#logging-in-using-the-web-interface) (note down your username, password, and [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html)!):

![](/images/databases/snowflake-1.png)

Enter the following queries into the SQL editor in the Worksheets page to create a database and a table with some example values:

```sql
CREATE DATABASE PETS;

CREATE TABLE MYTABLE (
    NAME            varchar(80),
    PET             varchar(80)
);

INSERT INTO MYTABLE VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');

SELECT * FROM MYTABLE;
```

Before you execute the queries, first determine which Snowflake UI / web interface you're using. The examples below use [Snowsight](https://docs.snowflake.com/en/user-guide/ui-snowsight). You can also use [Classic Console Worksheets](https://docs.snowflake.com/en/user-guide/ui-worksheet) or any other means of running Snowflake SQL statements.

### Execute queries in a Worksheet

To execute the queries in a Worksheet, highlight or select all the queries with your mouse, and click the play button in the top right corner.

<Image alt="AWS screenshot 1" src="/images/databases/snowflake-4.png" />

<Important>

Be sure to highlight or select **all** the queries (lines 1-10) before clicking the play button.

</Important>

Once you have executed the queries, you should see a preview of the table in the **Results** panel at the bottom of the page. Additionally, you should see your newly created database and schema by expanding the accordion on the left side of the page. Lastly, the warehouse name is displayed on the button to the left of the **Share** button.

<Image alt="AWS screenshot 2" src="/images/databases/snowflake-5.png" />

Make sure to note down the name of your warehouse, database, and schema. Γÿ¥∩╕Å

## Install snowflake-snowpark-python

You can find the instructions and prerequisites for installing `snowflake-snowpark-python` in the [Snowflake Developer Guide](https://docs.snowflake.com/en/developer-guide/snowpark/python/setup#installation-instructions).

```bash
pip install snowflake-snowpark-python
```

## Add connection parameters to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your appΓÇÖs root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesnΓÇÖt exist yet and add your Snowflake username, password, [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html), and the name of your warehouse, database, and schema as shown below:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
account = "xxx"
user = "xxx"
password = "xxx"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
client_session_keep_alive = true
```

If you created the database from the previous step, the names of your database and schema are `PETS` and `PUBLIC`, respectively. Streamlit will also use **Snowflake config and credentials** from a [SnowSQL config file](https://docs.snowflake.com/en/user-guide/snowsql-config#snowsql-config-file) if available.

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the query to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from mytable;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/snowflake-app.png)

### Using a Snowpark Session

The same [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection) used above also provides access to the [Snowpark Session](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/session.html) for DataFrame-style operations that run natively inside Snowflake. Using this approach, you can rewrite the app above as follows:

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Load the table as a dataframe using the Snowpark Session.
@st.cache_data
def load_table():
    session = conn.session()
    return session.table("mytable").to_pandas()

df = load_table()

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
```

If everything worked out (and you used the example table we created above), your app should look the same as the screenshot from the first example above.

## Connecting to Snowflake from Community Cloud

This tutorial assumes a local Streamlit app, however you can also connect to Snowflake from apps hosted in Community Cloud. The main additional steps are:

- [Include information about dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) using a `requirements.txt` file with `snowflake-snowpark-python` and any other dependencies.
- [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#deploy-an-app-and-set-up-secrets) to your Community Cloud app.

```

File: tutorials/databases/tidb.md
```

---

title: Connect Streamlit to TiDB
slug: /develop/tutorials/databases/tidb

---

# Connect Streamlit to TiDB

## Introduction

This guide explains how to securely access a **_remote_** TiDB database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

[TiDB](https://www.pingcap.com/tidb/) is an open-source, MySQL-compatible database that supports Hybrid Transactional and Analytical Processing (HTAP) workloads. [TiDB Cloud](https://tidb.cloud/) is a fully managed cloud database service that simplifies the deployment and management of TiDB databases for developers.

## Sign in to TiDB Cloud and create a cluster

First, head over to [TiDB Cloud](https://tidbcloud.com/free-trial) and sign up for a free account, using either Google, GitHub, Microsoft or E-mail:

![Sign up TiDB Cloud](/images/databases/tidb-1.png)

Once you've signed in, you will already have a TiDB cluster:

![List clusters](/images/databases/tidb-2.png)

You can create more clusters if you want to. Click the cluster name to enter cluster overview page:

![Cluster overview](/images/databases/tidb-3.png)

Then click **Connect** to easily get the connection arguments to access the cluster. On the popup, click **Generate password** to set the password.

![Get connection arguments](/images/databases/tidb-4.png)

<Important>

Make sure to note down the password. It won't be available on TiDB Cloud after this step.

</Important>

## Create a TiDB database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

Once your TiDB cluster is up and running, connect to it with the `mysql` client(or with **Chat2Query** tab on the console) and enter the following commands to create a database and a table with some example values:

```sql
CREATE DATABASE pets;

USE pets;

CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add host, username and password of your TiDB cluster as shown below:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **username** and **password** with those of your _remote_ TiDB cluster!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('tidb', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connect with PyMySQL

Other than [mysqlclient](https://github.com/PyMySQL/mysqlclient), [PyMySQL](https://github.com/PyMySQL/PyMySQL) is another popular MySQL Python client. To use PyMySQL, first you need to adapt your requirements file:

```bash
# requirements.txt
PyMySQL==x.x.x
SQLAlchemy==x.x.x
```

Then adapt your secrets file:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
driver = "pymysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
create_engine_kwargs = { connect_args = { ssl = { ca = "<path_to_CA_store>" }}}
```

```

File: tutorials/databases/_index.md
```

---

title: Connect to data sources
slug: /develop/tutorials/databases

---

# Connect Streamlit to data sources

These step-by-step guides demonstrate how to connect Streamlit apps to various databases & APIs.
They use Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) and
[caching](/develop/concepts/architecture/caching) to provide secure and fast data access.

<DataSourcesContainer>
<DataSourcesCard href="/develop/tutorials/databases/aws-s3">

<Image pure alt="screenshot" src="/images/databases/s3.png" />

<h5>AWS S3</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/bigquery">

<Image pure alt="screenshot" src="/images/databases/bigquery.png" />

<h5>BigQuery</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/deta-base">

<Image pure alt="screenshot" src="/images/databases/deta-base.png" />

<h5>Deta Base</h5>

</DataSourcesCard>

<DataSourcesCard href="https://blog.streamlit.io/streamlit-firestore/">

<Image pure alt="screenshot" src="/images/databases/firestore.png" />

<h5>Firestore (blog)</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/gcs">

<Image pure alt="screenshot" src="/images/databases/gcs.png" />

<h5>Google Cloud Storage</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/mssql">

<Image pure alt="screenshot" src="/images/databases/mssql.png" />

<h5>Microsoft SQL Server</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/mongodb">

<Image pure alt="screenshot" src="/images/databases/mongodb.png" />

<h5>MongoDB</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/mysql">

<Image pure alt="screenshot" src="/images/databases/mysql.png" />

<h5>MySQL</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/postgresql">

<Image pure alt="screenshot" src="/images/databases/postgresql.png" />

<h5>PostgreSQL</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/private-gsheet">

<Image pure alt="screenshot" src="/images/databases/gsheet.png" />

<h5>Private Google Sheet</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/public-gsheet">

<Image pure alt="screenshot" src="/images/databases/gsheet.png" />

<h5>Public Google Sheet</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/snowflake">

<Image pure alt="screenshot" src="/images/databases/snowflake.png" />

<h5>Snowflake</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/supabase">

<Image pure alt="screenshot" src="/images/databases/supabase.png" />

<h5>Supabase</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/tableau">

<Image pure alt="screenshot" src="/images/databases/tableau.png" />

<h5>Tableau</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/tidb">

<Image pure alt="screenshot" src="/images/databases/tidb.png" />

<h5>TiDB</h5>

</DataSourcesCard>

<DataSourcesCard href="/develop/tutorials/databases/tigergraph">

<Image pure alt="screenshot" src="/images/databases/tigergraph.png" />

<h5>TigerGraph</h5>

</DataSourcesCard>
</DataSourcesContainer>

```

File: tutorials/databases/mysql.md
```

---

title: Connect Streamlit to MySQL
slug: /develop/tutorials/databases/mysql

---

# Connect Streamlit to MySQL

## Introduction

This guide explains how to securely access a **_remote_** MySQL database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

## Create a MySQL database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow [this tutorial](https://dev.mysql.com/doc/mysql-getting-started/en/) to install MySQL and start the MySQL server (note down the username and password!). Once your MySQL server is up and running, connect to it with the `mysql` client and enter the following commands to create a database and a table with some example values:

```sql
CREATE DATABASE pets;

USE pets;

CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add the database name, user, and password of your MySQL server as shown below:

```toml
# .streamlit/secrets.toml

[connections.mysql]
dialect = "mysql"
host = "localhost"
port = 3306
database = "xxx"
username = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **database**, **username**, and **password** with those of your _remote_ MySQL database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

```

File: tutorials/databases/private-gsheet.md
```

---

title: Connect Streamlit to a private Google Sheet
slug: /develop/tutorials/databases/private-gsheet

---

# Connect Streamlit to a private Google Sheet

## Introduction

This guide explains how to securely access a private Google Sheet from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

If you are fine with enabling link sharing for your Google Sheet (i.e. everyone with the link can view it), the guide [Connect Streamlit to a public Google Sheet](/develop/tutorials/databases/public-gsheet) shows a simpler method of doing this. If your Sheet contains sensitive information and you cannot enable link sharing, keep on reading.

### Prerequisites

This tutorial requires `streamlit>=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet

If you already have a Sheet that you want to use, feel free to [skip to the next step](#enable-the-sheets-api).

Create a spreadsheet with this example data.

<div style={{ maxWidth: '200px', margin: 'auto' }}>

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

![Google sheet screenshot](/images/databases/private-gsheet-1.png)

## Enable the Sheets API

Programmatic access to Google Sheets is controlled through [Google Cloud Platform](https://cloud.google.com/). Create an account or sign in and head over to the [**APIs & Services** dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). As shown below, search for the Sheets API and enable it:

<Flex>
<Image alt="GCP screenshot 1" src="/images/databases/private-gsheet-2.png" />
<Image alt="GCP screenshot 2" src="/images/databases/private-gsheet-3.png" />
<Image alt="GCP screenshot 3" src="/images/databases/private-gsheet-4.png" />
</Flex>

## Create a service account & key file

To use the Sheets API from Streamlit Community Cloud, you need a Google Cloud Platform service account (a special account type for programmatic data access). Go to the [**Service Accounts** page](https://console.cloud.google.com/iam-admin/serviceaccounts) and create an account with the **Viewer** permission (this will let the account access data but not change it):

<Flex>
<Image alt="GCP screenshot 5" src="/images/databases/private-gsheet-5.png" />
<Image alt="GCP screenshot 6" src="/images/databases/private-gsheet-6.png" />
<Image alt="GCP screenshot 7" src="/images/databases/private-gsheet-7.png" />
</Flex>

<Note>

The button "**CREATE SERVICE ACCOUNT**" is gray, you don't have the correct permissions. Ask the admin of your Google Cloud project for help.

</Note>

After clicking "**DONE**", you should be back on the service accounts overview. First, note down the email address of the account you just created (**important for next step!**). Then, create a JSON key file for the new account and download it:

<Flex>
<Image alt="GCP screenshot 8" src="/images/databases/private-gsheet-8.png" />
<Image alt="GCP screenshot 9" src="/images/databases/private-gsheet-9.png" />
<Image alt="GCP screenshot 10" src="/images/databases/private-gsheet-10.png" />
</Flex>

## Share the Google Sheet with the service account

By default, the service account you just created cannot access your Google Sheet. To give it access, click on the "**Share**" button in the Google Sheet, add the email of the service account (noted down in step 2), and choose the correct permission (if you just want to read the data, "**Viewer**" is enough):

<Flex>
<Image alt="GCP screenshot 11" src="/images/databases/private-gsheet-11.png" />
<Image alt="GCP screenshot 12" src="/images/databases/private-gsheet-12.png" />
</Flex>

## Add the key file to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the URL of your Google Sheet plus the content of the key file you downloaded to it as shown below:

```toml
# .streamlit/secrets.toml

[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/xxxxxxx/edit#gid=0"

# From your JSON key file
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `.read()` results are cached without expiring. You can pass optional parameters to `.read()` to customize your connection. For example, you can specify the name of a worksheet, cache expiration time, or pass-through parameters for [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) like this:

```python
df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)
```

In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching). We've declared optional parameters `usecols=[0,1]` and `nrows=3` for `pandas` to use under the hood.

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connecting to a Google Sheet from Community Cloud

This tutorial assumes a local Streamlit app, however you can also connect to Google Sheets from apps hosted in Community Cloud. The main additional steps are:

- [Include information about dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) using a `requirements.txt` file with `st-gsheets-connection` and any other dependencies.
- [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#deploy-an-app-and-set-up-secrets) to your Community Cloud app.

```

File: tutorials/databases/aws-s3.md
```

---

title: Connect Streamlit to AWS S3
slug: /develop/tutorials/databases/aws-s3

---

# Connect Streamlit to AWS S3

## Introduction

This guide explains how to securely access files on AWS S3 from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [s3fs](https://github.com/dask/s3fs) library and optionally Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create an S3 bucket and add a file

<Note>

If you already have a bucket that you want to use, feel free
to [skip to the next step](#create-access-keys).

</Note>

First, [sign up for AWS](https://aws.amazon.com/) or log in. Go to the [S3 console](https://s3.console.aws.amazon.com/s3/home) and create a new bucket:

<Flex>
<Image alt="AWS screenshot 1" src="/images/databases/aws-1.png" />
<Image alt="AWS screenshot 2" src="/images/databases/aws-2.png" />
</Flex>

Navigate to the upload section of your new bucket:

<Flex>
<Image alt="AWS screenshot 3" src="/images/databases/aws-3.png" />
<Image alt="AWS screenshot 4" src="/images/databases/aws-4.png" />
</Flex>

And note down the "AWS Region" for later. In this example, it's `us-east-1`, but it may differ for you.

Next, upload the following CSV file, which contains some example data:

<Download href="/images/databases/myfile.csv">myfile.csv</Download>

## Create access keys

Go to the [AWS console](https://console.aws.amazon.com/), create access keys as shown below and copy the "Access Key ID" and "Secret Access Key":

<Flex>
<Image alt="AWS screenshot 5" src="/images/databases/aws-5.png" />
<Image alt="AWS screenshot 6" src="/images/databases/aws-6.png" />
</Flex>

<Tip>

Access keys created as a root user have wide-ranging permissions. In order to make your AWS account
more secure, you should consider creating an IAM account with restricted permissions and using its
access keys. More information [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).

</Tip>

## Set up your AWS credentials locally

Streamlit FilesConnection and s3fs will read and use your existing [AWS credentials and configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) if available - such as from an `~/.aws/credentials` file or environment variables.

If you don't already have this set up, or plan to host the app on Streamlit Community Cloud, you should specify the credentials from a file `.streamlit/secrets.toml` in your app's root directory or your home directory. Create this file if it doesn't exist yet and add to it the access key ID, access key secret, and the AWS default region you noted down earlier, as shown below:

```toml
# .streamlit/secrets.toml
AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"
AWS_DEFAULT_REGION = "xxx"
```

<Important>

Be sure to replace `xxx` above with the values you noted down earlier, and add this file to `.gitignore` so you don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

To host your app on Streamlit Community Cloud, you will need to pass your credentials to your deployed app via secrets. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` above into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add FilesConnection and s3fs to your requirements file

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [s3fs](https://github.com/dask/s3fs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
s3fs==x.x.x
st-files-connection
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables, where `s3fs` searches for them by default.

```python
# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("testbucket-jrieke/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

```

File: tutorials/databases/postgresql.md
```

---

title: Connect Streamlit to PostgreSQL
slug: /develop/tutorials/databases/postgresql

---

# Connect Streamlit to PostgreSQL

## Introduction

This guide explains how to securely access a **_remote_** PostgreSQL database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

## Create a PostgreSQL database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow [this tutorial](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm) to install PostgreSQL and create a database (note down the database name, username, and password!). Open the SQL Shell (`psql`) and enter the following two commands to create a table with some example values:

```sql
CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the name, user, and password of your database as shown below:

```toml
# .streamlit/secrets.toml

[connections.postgresql]
dialect = "postgresql"
host = "localhost"
port = "5432"
database = "xxx"
username = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **database**, **username**, and **password** with those of your _remote_ PostgreSQL database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [psycopg2-binary](https://www.psycopg.org/) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
psycopg2-binary==x.x.x
sqlalchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM mytable;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

```

File: tutorials/databases/supabase.md
```

---

title: Connect Streamlit to Supabase
slug: /develop/tutorials/databases/supabase

---

# Connect Streamlit to Supabase

## Introduction

This guide explains how to securely access a Supabase instance from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main) (a community-built connection developed by [@SiddhantSadangi](https://github.com/SiddhantSadangi)) and Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management). Supabase is the open source Firebase alternative and is based on PostgreSQL.

<Note>

Community-built connections, such as the [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main), extend and build on the `st.connection` interface and make it easier than ever to build Streamlit apps with a wide variety of data sources. These type of connections work exactly the same as [the ones built into Streamlit](/develop/api-reference/connections) and have access to all the same capabilities.

</Note>

## Sign in to Supabase and create a project

First, head over to [Supabase](https://app.supabase.io/) and sign up for a free account using your GitHub.

<Flex>
<Image caption="Sign in with GitHub" src="/images/databases/supabase-1.png" />
<Image caption="Authorize Supabase" src="/images/databases/supabase-2.png" />
</Flex>

Once you're signed in, you can create a project.

<Flex>
<Image caption="Your Supabase account" src="/images/databases/supabase-3.png" />
<Image caption="Create a new project" src="/images/databases/supabase-4.png" />
</Flex>

Your screen should look like this once your project has been created:

<Image src="/images/databases/supabase-5.png" />

<Important>

Make sure to note down your Project API Key and Project URL highlighted in the above screenshot. Γÿ¥∩╕Å

You will need these to connect to your Supabase instance from Streamlit.

</Important>

## Create a Supabase database

Now that you have a project, you can create a database and populate it with some sample data. To do so, click on the **SQL editor** button on the same project page, followed by the **New query** button in the SQL editor.

<Flex>
<Image caption="Open the SQL editor" src="/images/databases/supabase-6.png" />
<Image caption="Create a new query" src="/images/databases/supabase-7.png" />
</Flex>

In the SQL editor, enter the following queries to create a database and a table with some example values:

```sql
CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

Click **Run** to execute the queries. To verify that the queries were executed successfully, click on the **Table Editor** button on the left menu, followed by your newly created table `mytable`.

<Flex>
<Image caption="Write and run your queries" src="/images/databases/supabase-8.png" />
<Image caption="View your table in the Table Editor" src="/images/databases/supabase-9.png" />
</Flex>

With your Supabase database created, you can now connect to it from Streamlit!

### Add Supabase Project URL and API key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `SUPABASE_URL` and `SUPABASE_KEY` here:

```toml
# .streamlit/secrets.toml

[connections.supabase]
SUPABASE_URL = "xxxx"
SUPABASE_KEY = "xxxx"
```

Replace `xxxx` above with your Project URL and API key from [Step 1](/develop/tutorials/databases/supabase#sign-in-to-supabase-and-create-a-project).

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add st-supabase-connection to your requirements file

Add the [`st-supabase-connection`](https://pypi.org/project/st-supabase-connection/) community-built connection library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
st-supabase-connection==x.x.x
```

<Tip>

We've used the `st-supabase-connection` library here in combination with `st.connection` to benefit from the ease of setting up the data connection, managing your credentials, and Streamlit's caching capabilities that native and community-built connections provide.

You can however still directly use the [Supabase Python Client Library](https://pypi.org/project/supabase/) library if you prefer, but you'll need to write more code to set up the connection and cache the results. See [Using the Supabase Python Client Library](/develop/tutorials/databases/supabase#using-the-supabase-python-client-library) below for an example.

</Tip>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")

```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/supabase-10.png)

As Supabase uses PostgresSQL under the hood, you can also connect to Supabase by using the connection string Supabase provides under Settings > Databases. From there, you can refer to the [PostgresSQL tutorial](/develop/tutorials/databases/postgresql) to connect to your database.

## Using the Supabase Python Client Library

If you prefer to use the [Supabase Python Client Library](https://pypi.org/project/supabase/) directly, you can do so by following the steps below.

1. Add your Supabase Project URL and API key to your local app secrets:

   Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the SUPABASE_URL and SUPABASE_KEY here:

   ```toml
   # .streamlit/secrets.toml

   SUPABASE_URL = "xxxx"
   SUPABASE_KEY = "xxxx"
   ```

2. Add `supabase` to your requirements file:

   Add the [`supabase`](https://github.com/supabase-community/supabase-py) Python Client Library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

   ```bash
   # requirements.txt
   supabase==x.x.x
   ```

3. Write your Streamlit app:

   Copy the code below to your Streamlit app and run it.

   ```python
   # streamlit_app.py

   import streamlit as st
   from supabase import create_client, Client

   # Initialize connection.
   # Uses st.cache_resource to only run once.
   @st.cache_resource
   def init_connection():
       url = st.secrets["SUPABASE_URL"]
       key = st.secrets["SUPABASE_KEY"]
       return create_client(url, key)

   supabase = init_connection()

   # Perform query.
   # Uses st.cache_data to only rerun when the query changes or after 10 min.
   @st.cache_data(ttl=600)
   def run_query():
       return supabase.table("mytable").select("*").execute()

   rows = run_query()

   # Print results.
   for row in rows.data:
       st.write(f"{row['name']} has a :{row['pet']}:")
   ```

   See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

```

File: tutorials/databases/mongodb.md
```

---

title: Connect Streamlit to MongoDB
slug: /develop/tutorials/databases/mongodb

---

# Connect Streamlit to MongoDB

## Introduction

This guide explains how to securely access a **_remote_** MongoDB database from Streamlit Community Cloud. It uses the [PyMongo](https://github.com/mongodb/mongo-python-driver) library and Streamlit's [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

## Create a MongoDB Database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow the official tutorials to [install MongoDB](https://docs.mongodb.com/guides/server/install/), [set up authentication](https://docs.mongodb.com/guides/server/auth/) (note down the username and password!), and [connect to the MongoDB instance](https://docs.mongodb.com/guides/server/drivers/). Once you are connected, open the `mongo` shell and enter the following two commands to create a collection with some example values:

```sql
use mydb
db.mycollection.insertMany([{"name" : "Mary", "pet": "dog"}, {"name" : "John", "pet": "cat"}, {"name" : "Robert", "pet": "bird"}])
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the database information as shown below:

```toml
# .streamlit/secrets.toml

[mongo]
host = "localhost"
port = 27017
username = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **username**, and **password** with those of your _remote_ MongoDB database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add PyMongo to your requirements file

Add the [PyMongo](https://github.com/mongodb/mongo-python-driver) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
pymongo==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your database and collection.

```python
# streamlit_app.py

import streamlit as st
import pymongo

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example data we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

```

File: tutorials/execution-flow/_index.md
```

---

title: Use core features to work with Streamlit's execution model
slug: /develop/tutorials/execution-flow

---

# Use core features to work with Streamlit's execution model

## Fragments

<TileContainer layout="list">

<RefCard href="/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment">

<h5>Trigger a full-script rerun from inside a fragment</h5>

Call `st.rerun` from inside a fragment to trigger a full-script rerun when a condition is met.

</RefCard>

<RefCard href="/develop/tutorials/execution-flow/create-a-multiple-container-fragment">

<h5>Create a fragment across multiple containers</h5>

Use a fragment to write to multiple containers across your app.

</RefCard>

<RefCard href="/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns">

<h5>Start and stop a streaming fragment</h5>

Use a fragment to live-stream data. Use a button to start and stop the live-streaming.

</RefCard>

</TileContainer>

```

File: tutorials/execution-flow/fragments/create-a-multiple-container-fragment.md
```

---

title: Create a fragment across multiple containers
slug: /develop/tutorials/execution-flow/create-a-multiple-container-fragment

---

# Create a fragment across multiple containers

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. If your fragment doesn't write to outside containers, Streamlit will clear and redraw all the fragment elements with each fragment rerun. However, if your fragment _does_ write elements to outside containers, Streamlit will not clear those elements during a fragment rerun. Instead, those elements accumulate with each fragment rerun until the next full-script rerun. If you want a fragment to update multiple containers in your app, use [`st.empty()`](/develop/api-reference/layout/st.empty) containers to prevent accumulating elements.

## Applied concepts

- Use fragments to run two independent processes separately.
- Distribute a fragment across multiple containers.

## Prerequisites

**`streamlit>=1.33.0`**

- This tutorial uses fragments, which require Streamlit version 1.33.0 or later.
- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.empty()`.

## Summary

In this toy example, you'll build an app with six containers. Three containers will have orange cats. The other three containers will have black cats. You'll have three buttons in the sidebar: "**Herd the black cats**," "**Herd the orange cats**," and "**Herd all the cats**." Since herding cats is slow, you'll use fragments to help Streamlit run the associated processes efficiently. You'll create two fragments, one for the black cats and one for the orange cats. Since the buttons will be in the sidebar and the fragments will update containers in the main body, you'll use a trick with `st.empty()` to ensure you don't end up with too many cats in your app (if it's even possible to have too many cats). ≡ƒÿ╗

Here's a look at what you'll build:

<Collapse title="Complete code" expanded={false}>

```python
import streamlit as st
import time

st.title("Cats!")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
safe_grid = [card.empty() for card in grid]


def black_cats():
    time.sleep(1)
    st.title("≡ƒÉêΓÇìΓ¼¢ ≡ƒÉêΓÇìΓ¼¢")
    st.markdown("≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛")


def orange_cats():
    time.sleep(1)
    st.title("≡ƒÉê ≡ƒÉê")
    st.markdown("≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛")


@st.experimental_fragment
def herd_black_cats(card_a, card_b, card_c):
    st.button("Herd the black cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()


@st.experimental_fragment
def herd_orange_cats(card_a, card_b, card_c):
    st.button("Herd the orange cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()


with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
    herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
    st.button("Herd all the cats")
```

</Collapse>

<Cloud src="https://doc-tutorial-fragment-multiple-container.streamlit.app/?embed=true" height="650" />

## Build the example

### Initialize your app

1. In `your_repository`, create a file named `app.py`.
1. In a terminal, change directories to `your_repository` and start your app.

   ```bash
   streamlit run app.py
   ```

   Your app will be blank since you still need to add code.

1. In `app.py`, write the following:

   ```python
   import streamlit as st
   import time
   ```

   You'll use `time.sleep()` to slow things down and see the fragments working.

1. Save your `app.py` file and view your running app.
1. Click "**Always rerun**" or hit your "**A**" key in your running app.

   Your running preview will automatically update as you save changes to `app.py`. Your preview will still be blank. Return to your code.

### Frame out your app's containers

1. Add a title to your app and two rows of three containers.

   ```python
   st.title("Cats!")

   row1 = st.columns(3)
   row2 = st.columns(3)

   grid = [col.container(height=200) for col in row1 + row2]
   ```

   Save your file to see your updated preview.

1. Define a helper function to draw two black cats.

   ```python
   def black_cats():
       time.sleep(1)
       st.title("≡ƒÉêΓÇìΓ¼¢ ≡ƒÉêΓÇìΓ¼¢")
   st.markdown("≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛")
   ```

   This function represents "herding two cats" and uses `time.sleep()` to simulate a slower process. You will use this to draw two cats in one of your grid cards later on.

1. Define another helper function to draw two orange cats.

   ```python
   def orange_cats():
       time.sleep(1)
       st.title("≡ƒÉê ≡ƒÉê")
   st.markdown("≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛ ≡ƒÉ╛")
   ```

1. (Optional) Test out your functions by calling each one within a grid card.

   ```python
   with grid[0]:
       black_cats()
   with grid[1]:
       orange_cats()
   ```

   Save your `app.py` file to see the preview. Delete these four lines when finished.

### Define your fragments

Since each fragment will span across the sidebar and three additional containers, you'll use the sidebar to hold the main body of the fragment and pass the three containers as function arguments.

1. Use an [`@st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment) decorator and start your black-cat fragment definition.

   ```python
   @st.experimental_fragment
   def herd_black_cats(card_a, card_b, card_c):
   ```

1. Add a button for rerunning this fragment.

   ```python
       st.button("Herd the black cats")
   ```

1. Write to each container using your helper function.

   ```python
       with card_a:
           black_cats()
       with card_b:
           black_cats()
       with card_c:
           black_cats()
   ```

   **This code above will not behave as desired, but you'll explore and correct this in the following steps.**

1. Test out your code. Call your fragment function in the sidebar.

   ```python
   with st.sidebar:
       herd_black_cats(grid[0], grid[2], grid[4])
   ```

   Save your file and try using the button in the sidebar. More and more cats are appear in the cards with each fragment rerun! This is the expected behavior when fragments write to outside containers. To fix this, you will pass `st.empty()` containers to your fragment function.

   ![Example Streamlit app showing accumulating elements when a fragment writes to outside containers](/images/tutorials/fragment-multiple-containers-tutorial-app-duplicates.jpg)

1. Delete the lines of code from the previous two steps.

1. To prepare for using `st.empty()` containers, correct your cat-herding function as follows. After the button, define containers to place in the `st.empty()` cards you'll pass to your fragment.

   ```python
       container_a = card_a.container()
       container_b = card_b.container()
       container_c = card_c.container()
       with container_a:
           black_cats()
       with container_b:
           black_cats()
       with container_c:
           black_cats()
   ```

   In this new version, `card_a`, `card_b`, and `card_c` will be `st.empty()` containers. You create `container_a`, `container_b`, and `container_c` to allow Streamlit to draw multiple elements on each grid card.

1. Similarly define your orange-cat fragment function.

   ```python
   @st.experimental_fragment
   def herd_orange_cats(card_a, card_b, card_c):
       st.button("Herd the orange cats")
       container_a = card_a.container()
       container_b = card_b.container()
       container_c = card_c.container()
       with container_a:
           orange_cats()
       with container_b:
           orange_cats()
       with container_c:
           orange_cats()
   ```

### Put the functions together together to create an app

1. Call both of your fragments in the sidebar.

   ```python
   with st.sidebar:
       herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
       herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
   ```

   By creating `st.empty()` containers in each card and passing them to your fragments, you prevent elements from accumulating in the cards with each fragment rerun. If you create the `st.empty()` containers earlier in your app, full-script reruns will clear the orange-cat cards while (first) rendering the black-cat cards.

1. Include a button outside of your fragments. When clicked, the button will trigger a full-script rerun since you're calling its widget function outside of any fragment.

   ```python
       st.button("Herd all the cats")
   ```

1. Save your file and try out the app! When you click "**Herd the black cats**" or "**Herd the orange cats**," Streamlit will only redraw the three related cards. When you click "**Herd all the cats**," Streamlit redraws all six cards.

```

File: tutorials/execution-flow/fragments/trigger-a-full-script-rerun-from-a-fragment.md
```

---

title: Trigger a full-script rerun from inside a fragment
slug: /develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment

---

# Trigger a full-script rerun from inside a fragment

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. When a user interacts with a widget inside a fragment, only the fragment ruruns. Sometimes, you may want to trigger a full-script rerun from inside a fragment. To do this, call [`st.rerun`](/develop/api-reference/execution-flow/st.rerun) inside the fragment.

## Applied concepts

- Use a fragment rerun part or all of your app, depending on user input.

## Prerequisites

**`streamlit>=1.33.0`**

- This tutorial uses fragments, which require Streamlit version 1.33.0 or later.
- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.rerun`.

## Summary

In this example, you'll build an app to display sales data. The app has two sets of elements that depend on a date selection. One set of elements displays information for the selected day. The other set of elements displays information for the associated month. If the user changes days within a month, Streamlit only needs to update the first set of elements. If the user selects a day in a different month, Streamlit needs to update all the elements.

You'll collect the day-specific elements into a fragment to avoid rerunning the full app when a user changes days within the same month. If you want to jump ahead to the fragment function definition, see [Build a function to show daily sales data](#build-a-function-to-show-daily-sales-data).

<div style={{ maxWidth: '60%', margin: 'auto' }}>
<Image alt="Execution flow of example Streamlit app showing daily sales on the left and monthly sales on the right" src="/images/tutorials/fragment-rerun-tutorial-execution-flow.png" />
</div>

Here's a look at what you'll build:

<Collapse title="Complete code" expanded={false}>

```python
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import string
import time


@st.cache_data
def get_data():
    """Generate random sales data for Widget A through Widget Z"""

    product_names = ["Widget " + letter for letter in string.ascii_uppercase]
    average_daily_sales = np.random.normal(1_000, 300, len(product_names))
    products = dict(zip(product_names, average_daily_sales))

    data = pd.DataFrame({})
    sales_dates = np.arange(date(2023, 1, 1), date(2024, 1, 1), timedelta(days=1))
    for product, sales in products.items():
        data[product] = np.random.normal(sales, 300, len(sales_dates)).round(2)
    data.index = sales_dates
    data.index = data.index.date
    return data


@st.experimental_fragment
def show_daily_sales(data):
    time.sleep(1)
    with st.container(height=100):
        selected_date = st.date_input(
            "Pick a day ",
            value=date(2023, 1, 1),
            min_value=date(2023, 1, 1),
            max_value=date(2023, 12, 31),
            key="selected_date",
        )

    if "previous_date" not in st.session_state:
        st.session_state.previous_date = selected_date
    previous_date = st.session_state.previous_date
    st.session_state.previous_date = selected_date
    is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
    if is_new_month:
        st.rerun()

    with st.container(height=510):
        st.header(f"Best sellers, {selected_date:%m/%d/%y}")
        top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(top_ten)
        cols[1].bar_chart(top_ten)

    with st.container(height=510):
        st.header(f"Worst sellers, {selected_date:%m/%d/%y}")
        bottom_ten = data.loc[selected_date].sort_values()[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(bottom_ten)
        cols[1].bar_chart(bottom_ten)


def show_monthly_sales(data):
    time.sleep(1)
    selected_date = st.session_state.selected_date
    this_month = selected_date.replace(day=1)
    next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)

    st.container(height=100, border=False)
    with st.container(height=510):
        st.header(f"Daily sales for all products, {this_month:%B %Y}")
        monthly_sales = data[(data.index < next_month) & (data.index >= this_month)]
        st.write(monthly_sales)
    with st.container(height=510):
        st.header(f"Total sales for all products, {this_month:%B %Y}")
        st.bar_chart(monthly_sales.sum())


st.set_page_config(layout="wide")

st.title("Daily vs monthly sales, by product")
st.markdown("This app shows the 2023 daily sales for Widget A through Widget Z.")

data = get_data()
daily, monthly = st.columns(2)
with daily:
    show_daily_sales(data)
with monthly:
    show_monthly_sales(data)
```

</Collapse>

![Example Streamlit app showing daily sales on the left and monthly sales on the right](/images/tutorials/fragment-rerun-tutorial-app.jpg)

[Click here to see the example live on Community Cloud.](https://doc-tutorial-fragment-rerun.streamlit.app/)

## Build the example

### Initialize your app

1. In `your_repository`, create a file named `app.py`.
1. In a terminal, change directories to `your_repository` and start your app.

   ```bash
   streamlit run app.py
   ```

   Your app will be blank since you still need to add code.

1. In `app.py`, write the following:

   ```python
   import streamlit as st
   import pandas as pd
   import numpy as np
   from datetime import date, timedelta
   import string
   import time
   ```

   You'll be using these libraries as follows:

   - You'll work with sales data in a `pandas.DataFrame`.
   - You'll generate random sales numbers with `numpy`.
   - The data will have `datetime.date` index values.
   - The products sold will be "Widget A" through "Widget Z," so you'll use `string` for easy access to an alphabetical string.
   - (Optional) To help add emphasis at the end, you'll use `time.sleep()` to slow things down and see the fragment working.

1. Save your `app.py` file and view your running app.
1. Click "**Always rerun**" or hit your "**A**" key in your running app.

   Your running preview will automatically update as you save changes to `app.py`. Your preview will still be blank. Return to your code.

### Build a function to create random sales data

To begin with, you'll define a function to randomly generate some sales data. It's okay to skip this section if you just want to copy the function.

<Collapse title="Complete function to randomly generate sales data" expanded={false}>

```python
@st.cache_data
def get_data():
    """Generate random sales data for Widget A through Widget Z"""

    product_names = ["Widget " + letter for letter in string.ascii_uppercase]
    average_daily_sales = np.random.normal(1_000, 300, len(product_names))
    products = dict(zip(product_names, average_daily_sales))

    data = pd.DataFrame({})
    sales_dates = np.arange(date(2023, 1, 1), date(2024, 1, 1), timedelta(days=1))
    for product, sales in products.items():
        data[product] = np.random.normal(sales, 300, len(sales_dates)).round(2)
    data.index = sales_dates
    data.index = data.index.date
    return data
```

</Collapse>

1. Use an `@st.cache_data` decorator and start your function definition.

   ```python
   @st.cache_data
   def get_data():
       """Generate random sales data for Widget A through Widget Z"""
   ```

   You don't need to keep re-randomizing the data, so the caching decorator will randomly generate the data once and save it in Streamlit's cache. As your app reruns, it will use the cached value instead of recomputing new data.

1. Define the list of product names and assign an average daily sales value to each.

   ```python
       product_names = ["Widget " + letter for letter in string.ascii_uppercase]
       average_daily_sales = np.random.normal(1_000, 300, len(product_names))
       products = dict(zip(product_names, average_daily_sales))
   ```

1. For each product, use its average daily sales to randomly generate daily sales values for an entire year.

   ```python
       data = pd.DataFrame({})
       sales_dates = np.arange(date(2023, 1, 1), date(2024, 1, 1), timedelta(days=1))
       for product, sales in products.items():
           data[product] = np.random.normal(sales, 300, len(sales_dates)).round(2)
       data.index = sales_dates
       data.index = data.index.date
   ```

   In the last line, `data.index.date` strips away the timestamp, so the index will show clean dates.

1. Return the random sales data.

   ```python
       return data
   ```

1. (Optional) Test out your function by calling it and displaying the data.

   ```python
   data = get_data()
   data
   ```

   Save your `app.py` file to see the preview. Delete these two lines or keep them at the end of your app to be updated as you continue.

### Build a function to show daily sales data

Since the daily sales data updates with every new date selection, you'll turn this function into a fragment. As a fragment, it can rerun independently from the rest of your app. You'll include an `st.date_input` widget inside this fragment and watch for a date selection that changes the month. When the fragment detects a change in the selected month, it will trigger a full app rerun so everything can update.

<Collapse title="Complete function to display daily sales data" expanded={false}>

```python
@st.experimental_fragment
def show_daily_sales(data):
    time.sleep(1)
    selected_date = st.date_input(
        "Pick a day ",
        value=date(2023, 1, 1),
        min_value=date(2023, 1, 1),
        max_value=date(2023, 12, 31),
        key="selected_date",
    )

    if "previous_date" not in st.session_state:
        st.session_state.previous_date = selected_date
    previous_date = st.session_state.previous_date
    st.session_state.previous_date = selected_date
    is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
    if is_new_month:
        st.rerun()

    st.header(f"Best sellers, {selected_date:%m/%d/%y}")
    top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
    cols = st.columns([1, 4])
    cols[0].dataframe(top_ten)
    cols[1].bar_chart(top_ten)

    st.header(f"Worst sellers, {selected_date:%m/%d/%y}")
    bottom_ten = data.loc[selected_date].sort_values()[0:10]
    cols = st.columns([1, 4])
    cols[0].dataframe(bottom_ten)
    cols[1].bar_chart(bottom_ten)
```

</Collapse>

1. Use an [`@st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment) decorator and start your function definition.

   ```python
   @st.experimental_fragment
   def show_daily_sales(data):
   ```

   Since your data will not change during a fragment rerun, you can pass the data into the fragment as an argument.

1. (Optional) Add `time.sleep(1)` to slow down the function and show off how the fragment works.

   ```python
       time.sleep(1)
   ```

1. Add an `st.date_input` widget.

   ```python
       selected_date = st.date_input(
           "Pick a day ",
           value=date(2023, 1, 1),
           min_value=date(2023, 1, 1),
           max_value=date(2023, 12, 31),
           key="selected_date",
       )
   ```

   Your random data is for 2023, so set the minimun and maximum dates to match. Use a key for the widget because elements outside the fragment will need this date value. When working with a fragment, it's best to use Session State to pass information in and out of the fragment.

1. Initialize `"previous_date"` in Session State to compare each date selection.

   ```python
       if "previous_date" not in st.session_state:
           st.session_state.previous_date = selected_date
   ```

1. Save the previous date selection into a new variable and update `"previous_date"` in Session State.

   ```python
       previous_date = st.session_state.previous_date
       st.session_state.previous_date = selected_date
   ```

1. Call `st.rerun()` if the month changed.

   ```python
       is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
       if is_new_month:
           st.rerun()
   ```

1. Show the best sellers from the selected date.

   ```python
       st.header(f"Best sellers, {selected_date:%m/%d/%y}")
       top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
       cols = st.columns([1, 4])
       cols[0].dataframe(top_ten)
       cols[1].bar_chart(top_ten)
   ```

1. Show the worst sellers from the selected date.

   ```python
       st.header(f"Worst sellers, {selected_date:%m/%d/%y}")
       bottom_ten = data.loc[selected_date].sort_values()[0:10]
       cols = st.columns([1, 4])
       cols[0].dataframe(bottom_ten)
       cols[1].bar_chart(bottom_ten)
   ```

1. (Optional) Test out your function by calling it and displaying the data.

   ```python
   data = get_data()
   show_daily_sales(data)
   ```

   Save your `app.py` file to see the preview. Delete these two lines or keep them at the end of your app to be updated as you continue.

### Build a function to show monthly sales data

Finally, let's build a function to display monthly sales data. It will be similar to your `show_daily_sales` function but doesn't need to be fragment. You only need to rerun this function when the whole app is rerunning.

<Collapse title="Complete function to display daily sales data" expanded={false}>

```python
def show_monthly_sales(data):
    time.sleep(1)
    selected_date = st.session_state.selected_date
    this_month = selected_date.replace(day=1)
    next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)

    st.header(f"Daily sales for all products, {this_month:%B %Y}")
    monthly_sales = data[(data.index < next_month) & (data.index >= this_month)]
    st.write(monthly_sales)

    st.header(f"Total sales for all products, {this_month:%B %Y}")
    st.bar_chart(monthly_sales.sum())
```

</Collapse>

1. Start your function definition.

   ```python
   def show_monthly_sales(data):
   ```

1. (Optional) Add `time.sleep(1)` to slow down the function and show off how the fragment works.

   ```python
       time.sleep(1)
   ```

1. Get the selected date from Session State and compute the first days of this and next month.

   ```python
       selected_date = st.session_state.selected_date
       this_month = selected_date.replace(day=1)
       next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)
   ```

1. Show the daily sales values for all products within the selected month.

   ```python
       st.header(f"Daily sales for all products, {this_month:%B %Y}")
       monthly_sales = data[(data.index < next_month) & (data.index >= this_month)]
       st.write(monthly_sales)
   ```

1. Show the total sales of each product within the selected month.

   ```python
       st.header(f"Total sales for all products, {this_month:%B %Y}")
       st.bar_chart(monthly_sales.sum())
   ```

1. (Optional) Test out your function by calling it and displaying the data.

   ```python
   data = get_data()
   show_daily_sales(data)
   show_monthly_sales(data)
   ```

   Save your `app.py` file to see the preview. Delete these three lines when finished.

### Put the functions together together to create an app

Let's show these elements side-by-side. You'll display the daily data on the left and the monthly data on the right.

1. If you added optional lines at the end of your code to test your functions, clear them out now.

1. Give your app a wide layout.

   ```python
   st.set_page_config(layout="wide")
   ```

1. Get your data.

   ```python
   data = get_data()
   ```

1. Add a title and description for your app.

   ```python
   st.title("Daily vs monthly sales, by product")
   st.markdown("This app shows the 2023 daily sales for Widget A through Widget Z.")
   ```

1. Create columns and call the functions to display data.

   ```python
   daily, monthly = st.columns(2)
   with daily:
       show_daily_sales(data)
   with monthly:
       show_monthly_sales(data)
   ```

### Make it pretty

Now, you have a functioning app that uses a fragment to prevent unnecessarily redrawing the monthly data. However, things aren't aligned on the page, so you can insert a few containers to make it pretty. Add three containers into each of the display functions.

1. Add three containers to fix the height of elements in the `show_daily_sales` function.

   ```python
   @st.experimental_fragment
   def show_daily_sales(data):
       time.sleep(1)
       with st.container(height=100): ### ADD CONTAINER ###
           selected_date = st.date_input(
               "Pick a day ",
               value=date(2023, 1, 1),
               min_value=date(2023, 1, 1),
               max_value=date(2023, 12, 31),
               key="selected_date",
           )

       if "previous_date" not in st.session_state:
           st.session_state.previous_date = selected_date
       previous_date = st.session_state.previous_date
       previous_date = st.session_state.previous_date
       st.session_state.previous_date = selected_date
       is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
       if is_new_month:
           st.rerun()

       with st.container(height=510): ### ADD CONTAINER ###
           st.header(f"Best sellers, {selected_date:%m/%d/%y}")
           top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
           cols = st.columns([1, 4])
           cols[0].dataframe(top_ten)
           cols[1].bar_chart(top_ten)

       with st.container(height=510): ### ADD CONTAINER ###
           st.header(f"Worst sellers, {selected_date:%m/%d/%y}")
           bottom_ten = data.loc[selected_date].sort_values()[0:10]
           cols = st.columns([1, 4])
           cols[0].dataframe(bottom_ten)
           cols[1].bar_chart(bottom_ten)
   ```

1. Add three containers to fix the height of elements in the `show_monthly_sales` function.

   ```python
   def show_monthly_sales(data):
       time.sleep(1)
       selected_date = st.session_state.selected_date
       this_month = selected_date.replace(day=1)
       next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)

       st.container(height=100, border=False) ### ADD CONTAINER ###

       with st.container(height=510): ### ADD CONTAINER ###
           st.header(f"Daily sales for all products, {this_month:%B %Y}")
           monthly_sales = data[(data.index < next_month) & (data.index >= this_month)]
           st.write(monthly_sales)

       with st.container(height=510): ### ADD CONTAINER ###
           st.header(f"Total sales for all products, {this_month:%B %Y}")
           st.bar_chart(monthly_sales.sum())
   ```

   The first container creates space to coordinate with the input widget in the `show_daily_sales` function.

### Next steps

Continue beautifying the example. Try using [`st.plotly_chart`](/develop/api-reference/charts/st.plotly_chart) or [`st.altair_chart`](/develop/api-reference/charts/st.altair_chart) to add labels to your charts and adjust their height.

```

File: tutorials/execution-flow/fragments/start-and-stop-fragment-auto-reruns.md
```

---

title: Start and stop a streaming fragment
slug: /develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns

---

# Start and stop a streaming fragment

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. Additionally, you can tell Streamlit to rerun a fragment at a set time interval. This is great for streaming data or monitoring processes. You may want the user to start and stop this live streaming. To do this, programmatically set the `run_every` parameter for your fragment.

## Applied concepts

- Use a fragment to stream live data.
- Start and stop a fragment from automatically rerunning.

## Prerequisites

**`streamlit>=1.33.0`**

- This tutorial uses fragments, which require Streamlit version 1.33.0 or later.
- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments.

## Summary

In this example, you'll build an app that streams two data series in a line chart. Your app will gather recent data on the first load of a session and statically display the line chart. Two buttons in the sidebar will allow users to start and stop data streaming to update the chart in real time. You'll use a fragment to manage the frequency and scope of the live updates.

Here's a look at what you'll build:

<Collapse title="Complete code" expanded={false}>

```python
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def get_recent_data(last_timestamp):
    """Generate and return data from last timestamp to now, at most 60 seconds."""
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data


if "data" not in st.session_state:
    st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))

if "stream" not in st.session_state:
    st.session_state.stream = False


def toggle_streaming():
    st.session_state.stream = not st.session_state.stream


st.title("Data feed")
st.sidebar.slider(
    "Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
)
st.sidebar.button(
    "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
)
st.sidebar.button(
    "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
)

if st.session_state.stream is True:
    run_every = st.session_state.run_every
else:
    run_every = None


@st.experimental_fragment(run_every=run_every)
def show_latest_data():
    last_timestamp = st.session_state.data.index[-1]
    st.session_state.data = pd.concat(
        [st.session_state.data, get_recent_data(last_timestamp)]
    )
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)


show_latest_data()
```

</Collapse>

<Cloud src="https://doc-tutorial-fragment-streaming.streamlit.app/?embed=true" height="550" />

## Build the example

### Initialize your app

1. In `your_repository`, create a file named `app.py`.
1. In a terminal, change directories to `your_repository` and start your app.

   ```bash
   streamlit run app.py
   ```

   Your app will be blank since you still need to add code.

1. In `app.py`, write the following:

   ```python
    import streamlit as st
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
   ```

   You'll be using these libraries as follows:

   - You'll work with two data series in a `pandas.DataFrame`.
   - You'll generate random data with `numpy`.
   - The data will have `datetime.datetime` index values.

1. Save your `app.py` file and view your running app.
1. Click "**Always rerun**" or hit your "**A**" key in your running app.

   Your running preview will automatically update as you save changes to `app.py`. Your preview will still be blank. Return to your code.

### Build a function to generate random, recent data

To begin with, you'll define a function to randomly generate some data for two time series, which you'll call "A" and "B." It's okay to skip this section if you just want to copy the function.

<Collapse title="Complete function to randomly generate sales data" expanded={false}>

```python
def get_recent_data(last_timestamp):
    """Generate and return data from last timestamp to now, at most 60 seconds."""
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data
```

</Collapse>

1. Start your function definition.

   ```python
   def get_recent_data(last_timestamp):
       """Generate and return data from last timestamp to now, at most 60 seconds."""
   ```

   You'll pass the timestamp of your most recent datapoint to your data-generating function. Your function will use this to only return new data.

1. Get the current time and adjust the last timestamp if it is over 60 seconds ago.

   ```python
       now = datetime.now()
       if now - last_timestamp > timedelta(seconds=60):
           last_timestamp = now - timedelta(seconds=60)
   ```

   By updating the last timestamp, you'll ensure the function never returns more than 60 seconds of data.

1. Declare a new variable, `sample_time`, to define the time between datapoints. Calculate the timestamp of the first, new datapoint.

   ```python
       sample_time = timedelta(seconds=0.5)  # time between data points
       next_timestamp = last_timestamp + sample_time
   ```

1. Create a `datetime.datetime` index and generate two data series of the same length.

   ```python
       timestamps = np.arange(next_timestamp, now, sample_time)
       sample_values = np.random.randn(len(timestamps), 2)
   ```

1. Combine the data series with the index into a `pandas.DataFrame` and return the data.

   ```python
       data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
       return data
   ```

1. (Optional) Test out your function by calling it and displaying the data.

   ```python
   data = get_recent_data(datetime.now() - timedelta(seconds=60))
   data
   ```

   Save your `app.py` file to see the preview. Delete these two lines when finished.

### Initialize Session State values for your app

Since you will dynamically change the `run_every` parameter of `@st.experimental_fragment()`, you'll need to initialize the associated variables and Session State values before defining your fragment function. Your fragment function will also read and update values in Session State, so you can define those now to make the fragment function easier to understand.

1. Initialize your data for the first app load in a session.

   ```python
   if "data" not in st.session_state:
       st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))
   ```

   Your app will display this initial data in a static line chart before a user starts streaming data.

1. Initialize `"stream"` in Session State to turn streaming on and off. Set the default to off (`False`).

   ```python
   if "stream" not in st.session_state:
       st.session_state.stream = False
   ```

1. Create a callback function to toggle `"stream"` between `True` and `False`.

   ```python
   def toggle_streaming():
       st.session_state.stream = not st.session_state.stream
   ```

1. Add a title to your app.

   ```python
   st.title("Data feed")
   ```

1. Add a slider to the sidebar to set how frequently to check for data while streaming.

   ```python
   st.sidebar.slider(
       "Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
   )
   ```

1. Add buttons to the sidebar to turn streaming on and off.

   ```python
   st.sidebar.button(
       "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
   )
   st.sidebar.button(
       "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
   )
   ```

   Both functions use the same callback to toggle `"stream"` in Session State. Use the current value `"stream"` to disable one of the buttons. This ensures the buttons are always consistent with the current state; "**Start streaming**" is only clickable when streaming is off, and "**Stop streaming**" is only clickable when streaming is on. The buttons also provide status to the user by highlighting which action is available to them.

1. Create and set a new variable, `run_every`, that will determine whether or not the fragment function will rerun automatically (and how fast).

   ```python
   if st.session_state.stream is True:
       run_every = st.session_state.run_every
   else:
       run_every = None
   ```

### Build a fragment function to stream data

To allow the user to turn data streaming on and off, you must set the `run_every` parameter in the `@st.experimental_fragment()` decorator.

<Collapse title="Complete function to show and stream data" expanded={false}>

```python
@st.experimental_fragment(run_every=run_every)
def show_latest_data():
    last_timestamp = st.session_state.data.index[-1]
    st.session_state.data = pd.concat(
        [st.session_state.data, get_recent_data(last_timestamp)]
    )
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)
```

</Collapse>

1. Use an [`@st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment) decorator and start your function definition.

   ```python
    @st.experimental_fragment(run_every=run_every)
    def show_latest_data():
   ```

   Use the `run_every` variable declared above to set the parameter of the same name.

1. Retrieve the timestamp of the last datapoint in Session State.

   ```python
       last_timestamp = st.session_state.data.index[-1]
   ```

1. Update the data in Session State and trim to keep only the last 100 timestamps.

   ```python
       st.session_state.data = pd.concat(
           [st.session_state.data, get_recent_data(last_timestamp)]
       )
       st.session_state.data = st.session_state.data[-100:]
   ```

1. Show the data in a line chart.

   ```python
       st.line_chart(st.session_state.data)
   ```

   Your fragment-function definition is complete.

### Call and test out your fragment function

1. Call your function at the bottom of your code.

   ```python
   show_latest_data()
   ```

1. Test out your app by clicking "**Start streaming**." Try adjusting the frequency of updates.

### Next steps

Try adjusting the frequency of data generation or how much data is kept in Session State. Within `get_recent_data` try setting `sample_time` with a widget.

Try using [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart) or [st.altair_chart](/develop/api-reference/charts/st.altair_chart) to add labels to your chart.

```

File: tutorials/llms/conversational-apps.md
```

---

title: Build a basic LLM chat app
slug: /develop/tutorials/llms/build-conversational-apps

---

# Build a basic LLM chat app

## Introduction

The advent of large language models like GPT has revolutionized the ease of developing chat-based applications. Streamlit offers several [Chat elements](/develop/api-reference/chat), enabling you to build Graphical User Interfaces (GUIs) for conversational agents or chatbots. Leveraging [session state](/develop/concepts/architecture/session-state) along with these elements allows you to construct anything from a basic chatbot to a more advanced, ChatGPT-like experience using purely Python code.

In this tutorial, we'll start by walking through Streamlit's chat elements, `st.chat_message` and `st.chat_input`. Then we'll proceed to construct three distinct applications, each showcasing an increasing level of complexity and functionality:

1. First, we'll [Build a bot that mirrors your input](#build-a-bot-that-mirrors-your-input) to get a feel for the chat elements and how they work. We'll also introduce [session state](/develop/concepts/architecture/session-state) and how it can be used to store the chat history. This section will serve as a foundation for the rest of the tutorial.
2. Next, you'll learn how to [Build a simple chatbot GUI with streaming](#build-a-simple-chatbot-gui-with-streaming).
3. Finally, we'll [Build a ChatGPT-like app](#build-a-chatgpt-like-app) that leverages session state to remember conversational context, all within less than 50 lines of code.

Here's a sneak peek of the LLM-powered chatbot GUI with streaming we'll build in this tutorial:

<Cloud src="https://doc-chat-llm.streamlit.app/?embed=true" height="700px" />

Play around with the above demo to get a feel for what we'll build in this tutorial. A few things to note:

- There's a chat input at the bottom of the screen that's always visible. It contains some placeholder text. You can type in a message and press Enter or click the run button to send it.
- When you enter a message, it appears as a chat message in the container above. The container is scrollable, so you can scroll up to see previous messages. A default avatar is displayed to your messages' left.
- The assistant's responses are streamed to the frontend and are displayed with a different default avatar.

Before we start building, let's take a closer look at the chat elements we'll use.

## Chat elements

Streamlit offers several commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

[`st.chat_message`](/develop/api-reference/chat/st.chat_message) lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. [`st.chat_input`](/develop/api-reference/chat/st.chat_input) lets you display a chat input widget so the user can type in a message.

For an overview of the API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

<YouTube videoId="4sPnOqeUDmk" />

### st.chat_message

`st.chat_message` lets you insert a multi-element chat message container into your app. The returned container can contain any Streamlit element, including charts, tables, text, and more. To add elements to the returned container, you can use `with` notation.

`st.chat_message`'s first parameter is the `name` of the message author, which can be either `"user"` or `"assistant"` to enable preset styling and avatars, like in the demo above. You can also pass in a custom string to use as the author name. Currently, the name is not shown in the UI but is only set as an accessibility label. For accessibility reasons, you should not use an empty string.

Here's an minimal example of how to use `st.chat_message` to display a welcome message:

```python
import streamlit as st

with st.chat_message("user"):
    st.write("Hello ≡ƒæï")
```

<Image src="/images/knowledge-base/chat-message-hello.png" clean />
<br />

Notice the message is displayed with a default avatar and styling since we passed in `"user"` as the author name. You can also pass in `"assistant"` as the author name to use a different default avatar and styling, or pass in a custom name and avatar. See the [API reference](/develop/api-reference/chat/st.chat_message) for more details.

```python
import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))
```

<Cloud src="https://doc-chat-message-user1.streamlit.app/?embed=true" height="450px" />

While we've used the preferred `with` notation in the above examples, you can also just call methods directly in the returned objects. The below example is equivalent to the one above:

```python
import streamlit as st
import numpy as np

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))
```

So far, we've displayed predefined messages. But what if we want to display messages based on user input?

### st.chat_input

`st.chat_input` lets you display a chat input widget so the user can type in a message. The returned value is the user's input, which is `None` if the user hasn't sent a message yet. You can also pass in a default prompt to display in the input widget. Here's an example of how to use `st.chat_input` to display a chat input widget and show the user's input:

```python
import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
```

<Cloud src="https://doc-chat-input.streamlit.app/?embed=true" height="350px" />

Pretty straightforward, right? Now let's combine `st.chat_message` and `st.chat_input` to build a bot the mirrors or echoes your input.

## Build a bot that mirrors your input

In this section, we'll build a bot that mirrors or echoes your input. More specifically, the bot will respond to your input with the same message. We'll use `st.chat_message` to display the user's input and `st.chat_input` to accept user input. We'll also use [session state](/develop/concepts/architecture/session-state) to store the chat history so we can display it in the chat message container.

First, let's think about the different components we'll need to build our bot:

- Two chat message containers to display messages from the user and the bot, respectively.
- A chat input widget so the user can type in a message.
- A way to store the chat history so we can display it in the chat message containers. We can use a list to store the messages, and append to it every time the user or bot sends a message. Each entry in the list will be a dictionary with the following keys: `role` (the author of the message), and `content` (the message content).

```python
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

In the above snippet, we've added a title to our app and a for loop to iterate through the chat history and display each message in the chat message container (with the author role and message content). We've also added a check to see if the `messages` key is in `st.session_state`. If it's not, we initialize it to an empty list. This is because we'll be adding messages to the list later on, and we don't want to overwrite the list every time the app reruns.

Now let's accept user input with `st.chat_input`, display the user's message in the chat message container, and add it to the chat history.

```python
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
```

We used the `:=` operator to assign the user's input to the `prompt` variable and checked if it's not `None` in the same line. If the user has sent a message, we display the message in the chat message container and append it to the chat history.

All that's left to do is add the chatbot's responses within the `if` block. We'll use the same logic as before to display the bot's response (which is just the user's prompt) in the chat message container and add it to the history.

```python
response = f"Echo: {prompt}"
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response)
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
```

Putting it all together, here's the full code for our simple chatbot GUI and the result:

<Collapse title="View full code" expanded={false}>

```python
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
```

</Collapse>

<Cloud src="https://doc-chat-echo.streamlit.app/?embed=true" height="700px" />

While the above example is very simple, it's a good starting point for building more complex conversational apps. Notice how the bot responds instantly to your input. In the next section, we'll add a delay to simulate the bot "thinking" before responding.

## Build a simple chatbot GUI with streaming

In this section, we'll build a simple chatbot GUI that responds to user input with a random message from a list of pre-determind responses. In the [next section](#build-a-chatgpt-like-app), we'll convert this simple toy example into a ChatGPT-like experience using OpenAI.

Just like previously, we still require the same components to build our chatbot. Two chat message containers to display messages from the user and the bot, respectively. A chat input widget so the user can type in a message. And a way to store the chat history so we can display it in the chat message containers.

Let's just copy the code from the previous section and add a few tweaks to it.

```python
import streamlit as st
import random
import time

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
```

The only difference so far is we've changed the title of our app and added imports for `random` and `time`. We'll use `random` to randomly select a response from a list of responses and `time` to add a delay to simulate the chatbot "thinking" before responding.

All that's left to do is add the chatbot's responses within the `if` block. We'll use a list of responses and randomly select one to display. We'll also add a delay to simulate the chatbot "thinking" before responding (or stream its response). Let's make a helper function for this and insert it at the top of our app.

```python
# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
```

Back to writing the response in our chat interface, we'll use `st.write_stream` to write out the streamed response with a typewriter effect.

```python
# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
```

Above, we've added a placeholder to display the chatbot's response. We've also added a for loop to iterate through the response and display it one word at a time. We've added a delay of 0.05 seconds between each word to simulate the chatbot "thinking" before responding. Finally, we append the chatbot's response to the chat history. As you've probably guessed, this is a naive implementation of streaming. We'll see how to implement streaming with OpenAI in the [next section](#build-a-chatgpt-like-app).

Putting it all together, here's the full code for our simple chatbot GUI and the result:

<Collapse title="View full code" expanded={false}>

```python
import streamlit as st
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
```

</Collapse>

<Cloud src="https://doc-chat-simple.streamlit.app/?embed=true" height="700px" />

Play around with the above demo to get a feel for what we've built. It's a very simple chatbot GUI, but it has all the components of a more sophisticated chatbot. In the next section, we'll see how to build a ChatGPT-like app using OpenAI.

## Build a ChatGPT-like app

Now that you've understood the basics of Streamlit's chat elements, let's make a few tweaks to it to build our own ChatGPT-like app. You'll need to install the [OpenAI Python library](https://pypi.org/project/openai/) and get an [API key](https://platform.openai.com/account/api-keys) to follow along.

### Install dependencies

First let's install the dependencies we'll need for this section:

```bash
pip install openai streamlit
```

### Add OpenAI API key to Streamlit secrets

Next, let's add our OpenAI API key to [Streamlit secrets](/develop/concepts/connections/secrets-management). We do this by creating `.streamlit/secrets.toml` file in our project directory and adding the following lines to it:

```toml
# .streamlit/secrets.toml
OPENAI_API_KEY = "YOUR_API_KEY"
```

### Write the app

Now let's write the app. We'll use the same code as before, but we'll replace the list of responses with a call to the OpenAI API. We'll also add a few more tweaks to make the app more ChatGPT-like.

```python
import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
```

All that's changed is that we've added a default model to `st.session_state` and set our OpenAI API key from Streamlit secrets. Here's where it gets interesting. We can replace our emulated stream with the model's responses from OpenAI:

```python
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
```

Above, we've replaced the list of responses with a call to [`OpenAI().chat.completions.create`](https://platform.openai.com/docs/guides/text-generation/chat-completions-api). We've set `stream=True` to stream the responses to the frontend. In the API call, we pass the model name we hardcoded in session state and pass the chat history as a list of messages. We also pass the `role` and `content` of each message in the chat history. Finally, OpenAI returns a stream of responses (split into chunks of tokens), which we iterate through and display each chunk.

Putting it all together, here's the full code for our ChatGPT-like app and the result:

<Collapse title="View full code" expanded={false}>

```python
from openai import OpenAI
import streamlit as st

st.title("ChatGPT-like clone")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
```

<Image src="/images/knowledge-base/chatgpt-clone.gif" clean />

</Collapse>

<Cloud src="https://doc-chat-llm.streamlit.app/?embed=true" height="700px" />

Congratulations! You've built your own ChatGPT-like app in less than 50 lines of code.

We're very excited to see what you'll build with Streamlit's chat elements. Experiment with different models and tweak the code to build your own conversational apps. If you build something cool, let us know on the [Forum](https://discuss.streamlit.io/c/streamlit-examples/9) or check out some other [Generative AI apps](https://streamlit.io/generative-ai) for inspiration. ≡ƒÄê

```

File: tutorials/llms/_index.md
```

---

title: Build LLM apps
slug: /develop/tutorials/llms

---

# Build LLM apps

<TileContainer layout="list">

<RefCard href="/develop/tutorials/llms/build-conversational-apps">

<h5>Build a basic chat app</h5>

Build a simple OpenAI chat app to get started with Streamlit's chat elements.

</RefCard>

<RefCard href="/develop/tutorials/llms/llm-quickstart">

<h5>Build an LLM app using LangChain</h5>

Build a chat app using the LangChain framework with OpenAI.

</RefCard>

</TileContainer>

```

File: tutorials/llms/llm-quickstart.md
```

---

title: Build an LLM app using LangChain
slug: /develop/tutorials/llms/llm-quickstart

---

# Build an LLM app using LangChain

## OpenAI, LangChain, and Streamlit in 18 lines of code

In this tutorial, you will build a Streamlit LLM app that can generate text from a user-provided prompt. This Python app will use the LangChain framework and Streamlit. Optionally, you can deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud) when you're done.

_This tutorial is adapted from a blog post by Chanin Nantesanamat: [LangChain tutorial #1: Build an LLM-powered app in 18 lines of code](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/)._

<Cloud src="https://doc-tutorial-llm-18-lines-of-code.streamlit.app/?embed=true" height="600" />

## Objectives

1. Get an OpenAI key from the end user.
2. Validate the user's OpenAI key.
3. Get a text prompt from the user.
4. Authenticate OpenAI with the user's key.
5. Send the user's prompt to OpenAI's API.
6. Get a response and display it.

Bonus: Deploy the app on Streamlit Community Cloud!

## Prerequisites

- Python 3.8+
- Streamlit
- LangChain
- [OpenAI API key](https://platform.openai.com/account/api-keys?ref=blog.streamlit.io)

## Setup coding environment

In your IDE (integrated coding environment), open the terminal and install the following three Python libraries:

```python
pip install streamlit openai langchain
```

Create a `requirements.txt` file located in the root of your working directory and save these dependencies. This is necessary for deploying the app to the Streamlit Community Cloud later.

```python
streamlit
openai
langchain
```

## Building the app

The app is only 18 lines of code:

```python
import streamlit as st
from langchain.llms import OpenAI

st.title('≡ƒª£≡ƒöù Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='ΓÜá')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
```

To start, create a new Python file and save it as┬á`streamlit_app.py` in the root of your working directory.

1. Import the necessary Python libraries.

   ```python
   import streamlit as st
   from langchain.llms import OpenAI
   ```

2. Create the app's title using `st.title`.

   ```python
   st.title('≡ƒª£≡ƒöù Quickstart App')
   ```

3. Add a text input box for the user to enter their OpenAI API key.

   ```python
   openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
   ```

4. Define a function to authenticate to OpenAI API with the user's key, send a prompt, and get an AI-generated response. This function accepts the user's prompt as an argument and displays the AI-generated response in a blue box using `st.info`.

   ```python
   def generate_response(input_text):
       llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
       st.info(llm(input_text))
   ```

5. Finally, use `st.form()` to create a text box (`st.text_area()`) for user input. When the user clicks `Submit`, the `generate-response()` function is called with the user's input as an argument.

   ```python
   with st.form('my_form'):
       text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
       submitted = st.form_submit_button('Submit')
       if not openai_api_key.startswith('sk-'):
           st.warning('Please enter your OpenAI API key!', icon='ΓÜá')
       if submitted and openai_api_key.startswith('sk-'):
           generate_response(text)
   ```

6. Remember to save your file!
7. Return to your computer's terminal to run the app.

   ```bash
   streamlit run streamlit_app.py
   ```

## Deploying the app

To deploy the app to the Streamlit Cloud, follow these steps:

1. Create a GitHub repository for the app. Your repository should contain two files:

   ```
   your-repository/
   Γö£ΓöÇΓöÇ streamlit_app.py
   ΓööΓöÇΓöÇ requirements.txt
   ```

1. Go to [Streamlit Community Cloud](http://share.streamlit.io), click the┬á`New app`┬ábutton from your workspace, then specify the repository, branch, and main file path. Optionally, you can customize your app's URL by choosing a custom subdomain.
1. Click the┬á`Deploy!`┬ábutton.

Your app will now be deployed to Streamlit Community Cloud and can be accessed from around the world! ≡ƒîÄ

## Conclusion

Congratulations on building an LLM-powered Streamlit app in 18 lines of code! ≡ƒÑ│ You can use this app to generate text from any prompt that you provide. The app is limited by the capabilities of the OpenAI LLM, but it can still be used to generate some creative and interesting text.

We hope you found this tutorial helpful! Check out [more examples](https://streamlit.io/generative-ai) to see the power of Streamlit and LLM. ≡ƒÆû

Happy Streamlit-ing! ≡ƒÄê

```

File: quick-references/prerelease-features.md
```

---

title: Pre-release features
slug: /develop/quick-reference/prerelease

---

# Pre-release features

At Streamlit, we like to move quick while keeping things stable. In our latest effort to move even faster without sacrificing stability, we're offering our bold and fearless users two ways to try out Streamlit's bleeding-edge features:

1. [Experimental features](#experimental-features)
2. [Nightly releases](#nightly-releases)

## Experimental Features

Less stable Streamlit features have one naming convention: `st.experimental_`. This distinction is a prefix we attach to our command names to make sure their status is clear to everyone.

Here's a quick rundown of what you get from each naming convention:

- **st**: this is where our core features like `st.write` and `st.dataframe` live. If we ever make backward-incompatible changes to these, they will take place gradually and with months of announcements and warnings.
- **experimental**: this is where we'll put all new features that may or may not ever make it into Streamlit core. This gives you a chance to try the next big thing we're cooking up weeks or months before we're ready to stabilize its API. We don't know whether these features have a future, but we want you to have access to everything we're trying, and work with us to figure them out.

Features with the `experimental_` naming convention are things that we're still working on or trying
to understand. If these features are successful, at some point they'll become part of Streamlit
core. If unsuccessful, these features are removed without much notice. While in experimental, a feature's API and behaviors may not be stable, and it's possible they could change in ways that aren't backward-compatible.

<Warning>

Experimental features and their APIs may change or be removed at any time.

</Warning>

### The lifecycle of an experimental feature

1. A feature is added with the `experimental_` prefix.
2. The feature is potentially tweaked over time, with possible API/behavior breakages.
3. If successful, we promote the feature to Streamlit core and remove it from `experimental_`:
   - a\. The feature's API stabilizes and the feature is _cloned_ without the `experimental_` prefix, so it exists as both `st` and `experimental_`. At this point, users will see a warning when using the version of the feature with the `experimental_` prefix -- but the feature will still work.
   - b\. At some point, the code of the `experimental_`-prefixed feature is _removed_, but there will still be a stub of the function prefixed with `experimental_` that shows an error with appropriate instructions.
   - c\. Finally, at a later date the `experimental_` version is removed.
4. If unsuccessful, the feature is removed without much notice and we leave a stub in `experimental_` that shows an error with instructions.

## Nightly releases

In addition to experimental features, we offer another way to try out Streamlit's newest features: nightly releases.

At the end of each day (at night ≡ƒî¢), our bots run automated tests against the latest Streamlit code and, if everything looks good, it publishes them as the `streamlit-nightly` package. This means the nightly build includes all our latest features, bug fixes, and other enhancements on the same day they land on our codebase.

**How does this differ from official releases?**

Official Streamlit releases go not only through both automated tests but also rigorous manual testing, while nightly releases only have automated tests. It's important to keep in mind that new features introduced in nightly releases often lack polish. In our official releases, we always make double-sure all new features are ready for prime time.

**How do I use the nightly release?**

All you need to do is install the `streamlit-nightly` package:

```bash
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```

<Warning>

You should never have both `streamlit` and `streamlit-nightly` installed in the same environment!

</Warning>

**Why should I use the nightly release?**

Because you can't wait for official releases, and you want to help us find bugs early!

**Why shouldn't I use the nightly release?**

While our automated tests have high coverage, there's still a significant likelihood that there will be some bugs in the nightly code.

**Can I choose which nightly release I want to install?**

If you'd like to use a specific version, you can find the version number in our [Release history](https://pypi.org/project/streamlit-nightly/#history). Specify the desired version using `pip` as usual: `pip install streamlit-nightly==x.yy.zz-123456`.

**Can I compare changes between releases?**

If you'd like to review the changes for a nightly release, you can use the [comparison tool on GitHub](https://github.com/streamlit/streamlit/compare/0.57.3...0.57.4.dev20200412).

```

File: quick-references/api-cheat-sheet.md
```

---

title: Streamlit API cheat sheet
slug: /develop/quick-reference/cheat-sheet

---

# Streamlit API cheat sheet

This is a summary of the docs, as of [Streamlit v1.33.0](https://pypi.org/project/streamlit/1.33.0/).

<Masonry>

<CodeTile featured>

#### Install & Import

```python
pip install streamlit

streamlit run first_app.py

# Import convention
>>> import streamlit as st
```

</CodeTile>

<CodeTile featured>

#### Pre-release features

```python
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```

Learn more about [experimental features](advanced-features/prerelease#experimental-features)

</CodeTile>

<CodeTile featured>

#### Command line

```python
streamlit --help
streamlit run your_script.py
streamlit hello
streamlit config show
streamlit cache clear
streamlit docs
streamlit --version
```

</CodeTile>

</Masonry>

<Masonry>

<CodeTile>

#### Magic commands

```python
# Magic commands implicitly
# call st.write().
"_This_ is some **Markdown***"
my_variable
"dataframe:", my_data_frame

```

</CodeTile>

<CodeTile>

#### Display text

```python
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3]) # see *
st.write_stream(my_generator)
st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("_Markdown_") # see *
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
* optional kwarg unsafe_allow_html = True
```

</CodeTile>

<CodeTile>

#### Display data

```python
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)

```

</CodeTile>

<CodeTile>

#### Display media

```python
st.image("./header.png")
st.audio(data)
st.video(data)
st.video(data, subtitles="./subs.vtt")
```

</CodeTile>

<CodeTile>

#### Display charts

```python
st.area_chart(df)
st.bar_chart(df)
st.line_chart(df)
st.map(df)
st.scatter_chart(df)

st.altair_chart(chart)
st.bokeh_chart(fig)
st.graphviz_chart(fig)
st.plotly_chart(fig)
st.pydeck_chart(chart)
st.pyplot(fig)
st.vega_lite_chart(df)
```

</CodeTile>

<CodeTile>

#### Add widgets to sidebar

```python
# Just add it after st.sidebar:
>>> a = st.sidebar.radio("Select one:", [1, 2])

# Or use "with" notation:
>>> with st.sidebar:
>>>   st.radio("Select one:", [1, 2])
```

</CodeTile>

<CodeTile>

#### Columns

```python
# Two equal columns:
>>> col1, col2 = st.columns(2)
>>> col1.write("This is column 1")
>>> col2.write("This is column 2")

# Three different columns:
>>> col1, col2, col3 = st.columns([3, 1, 1])
# col1 is larger.

# You can also use "with" notation:
>>> with col1:
>>>   st.radio("Select one:", [1, 2])
```

</CodeTile>

<CodeTile>

#### Tabs

```python
# Insert containers separated into tabs:
>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
>>> tab1.write("this is tab 1")
>>> tab2.write("this is tab 2")

# You can also use "with" notation:
>>> with tab1:
>>>   st.radio("Select one:", [1, 2])
```

</CodeTile>

<CodeTile>

#### Expandable containers

```python
>>> expand = st.expander("My label")
>>> expand.write("Inside the expander.")
>>> pop = st.popover("Button label")
>>> pop.checkbox("Show all")

# You can also use "with" notation:
>>> with expand:
>>>   st.radio("Select one:", [1, 2])
```

</CodeTile>

<CodeTile>

#### Control flow

```python
# Stop execution immediately:
st.stop()
# Rerun script immediately:
st.rerun()
# Navigate to another page:
st.switch_page("pages/my_page.py")

# Group multiple widgets:
>>> with st.form(key="my_form"):
>>>   username = st.text_input("Username")
>>>   password = st.text_input("Password")
>>>   st.form_submit_button("Login")

# Define a fragment
>>> @st.experimental_fragment
>>> def fragment_function():
>>>     df = get_data()
>>>     st.line_chart(df)
>>>     st.button("Update")
>>>
>>> fragment_function()
```

</CodeTile>

<CodeTile>

#### Display interactive widgets

```python
st.button("Click me")
st.download_button("Download file", data)
st.link_button("Go to gallery", url)
st.page_link("app.py", label="Home")
st.data_editor("Edit data", data)
st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.camera_input("Take a picture")
st.color_picker("Pick a color")

# Use widgets' returned values in variables:
>>> for i in range(int(st.number_input("Num:"))):
>>>   foo()
>>> if st.sidebar.selectbox("I:",["f"]) == "f":
>>>   b()
>>> my_slider_val = st.slider("Quinn Mallory", 1, 88)
>>> st.write(slider_val)

# Disable widgets to remove interactivity:
>>> st.slider("Pick a number", 0, 100, disabled=True)
```

</CodeTile>

<CodeTile>

#### Build chat-based apps

```python
# Insert a chat message container.
>>> with st.chat_message("user"):
>>>    st.write("Hello ≡ƒæï")
>>>    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget at the bottom of the app.
>>> st.chat_input("Say something")

# Display a chat input widget inline.
>>> with st.container():
>>>     st.chat_input("Say something")
```

Learn how to [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps)

</CodeTile>

<CodeTile>

#### Mutate data

```python
# Add rows to a dataframe after
# showing it.
>>> element = st.dataframe(df1)
>>> element.add_rows(df2)

# Add rows to a chart after
# showing it.
>>> element = st.line_chart(df1)
>>> element.add_rows(df2)
```

</CodeTile>

<CodeTile>

#### Display code

```python
>>> with st.echo():
>>>   st.write("Code will be executed and printed")
```

</CodeTile>

<CodeTile>

#### Placeholders, help, and options

```python
# Replace any single element.
>>> element = st.empty()
>>> element.line_chart(...)
>>> element.text_input(...)  # Replaces previous.

# Insert out of order.
>>> elements = st.container()
>>> elements.line_chart(...)
>>> st.write("Hello")
>>> elements.text_input(...)  # Appears above "Hello".

st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout="wide")
st.query_params[key]
st.query_params.get_all(key)
st.query_params.clear()
st.html("<p>Hi!</p>")
```

</CodeTile>

<CodeTile>

#### Connect to data sources

```python
st.connection("pets_db", type="sql")
conn = st.connection("sql")
conn = st.connection("snowflake")

>>> class MyConnection(BaseConnection[myconn.MyConnection]):
>>>    def _connect(self, **kwargs) -> MyConnection:
>>>        return myconn.connect(**self._secrets, **kwargs)
>>>    def query(self, query):
>>>       return self._instance.query(query)
```

</CodeTile>

<CodeTile>

#### Optimize performance

###### Cache data objects

```python
# E.g. Dataframe computation, storing downloaded data, etc.
>>> @st.cache_data
... def foo(bar):
...   # Do something expensive and return data
...   return data
# Executes foo
>>> d1 = foo(ref1)
# Does not execute foo
# Returns cached item by value, d1 == d2
>>> d2 = foo(ref1)
# Different arg, so function foo executes
>>> d3 = foo(ref2)
# Clear all cached entries for this function
>>> foo.clear()
# Clear values from *all* in-memory or on-disk cached functions
>>> st.cache_data.clear()
```

###### Cache global resources

```python
# E.g. TensorFlow session, database connection, etc.
>>> @st.cache_resource
... def foo(bar):
...   # Create and return a non-data object
...   return session
# Executes foo
>>> s1 = foo(ref1)
# Does not execute foo
# Returns cached item by reference, s1 == s2
>>> s2 = foo(ref1)
# Different arg, so function foo executes
>>> s3 = foo(ref2)
# Clear all cached entries for this function
>>> foo.clear()
# Clear all global resources from cache
>>> st.cache_resource.clear()
```

###### Deprecated caching

```python
>>> @st.cache
... def foo(bar):
...   # Do something expensive in here...
...   return data
>>> # Executes foo
>>> d1 = foo(ref1)
>>> # Does not execute foo
>>> # Returns cached item by reference, d1 == d2
>>> d2 = foo(ref1)
>>> # Different arg, so function foo executes
>>> d3 = foo(ref2)
```

</CodeTile>

<CodeTile>

#### Display progress and status

```python
# Show a spinner during a process
>>> with st.spinner(text="In progress"):
>>>   time.sleep(3)
>>>   st.success("Done")

# Show and update progress bar
>>> bar = st.progress(50)
>>> time.sleep(3)
>>> bar.progress(100)

>>> with st.status("Authenticating...") as s:
>>>   time.sleep(2)
>>>   st.write("Some long response.")
>>>   s.update(label="Response")

st.balloons()
st.snow()
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")
st.exception(e)
```

</CodeTile>
</Masonry>

<Masonry>
<CodeTile>

#### Personalize apps for users

```python
# Show different content based on the user's email address.
>>> if st.user.email == "jane@email.com":
>>>    display_jane_content()
>>> elif st.user.email == "adam@foocorp.io":
>>>    display_adam_content()
>>> else:
>>>    st.write("Please contact us to get access!")
```

</CodeTile>
</Masonry>

```

File: quick-references/_index.md
```

---

title: Quick reference
slug: /develop/quick-reference

---

# Quick reference

<TileContainer layout="list">

<RefCard href="/develop/quick-reference/cheat-sheet">

<h5>Cheatsheet</h5>

A dense list of Streamlit commands with example syntax.

</RefCard>

<RefCard href="/develop/quick-reference/changelog">

<h5>Changelog</h5>

See how Streamlit has changed with each new version.

</RefCard>

<RefCard href="/develop/quick-reference/prerelease">

<h5>Pre-release features</h5>

Understand how we introduce new features and how you can get your hands on them sooner!

</RefCard>

<RefCard href="https://roadmap.streamlit.app/">

<h5>Roadmap</h5>

Get a sneak peek at what we have scheduled for the next year.

</RefCard>

</TileContainer>

```

File: quick-references/changelog.md
```

---

title: Changelog
slug: /develop/quick-reference/changelog

---

# Changelog

This page lists highlights, bug fixes, and known issues for official Streamlit releases. If you're looking for information about nightly releases, beta features, or experimental features, see [Try pre-release features](/develop/quick-reference/prerelease).

<Tip>

To upgrade to the latest version of Streamlit, run:

```bash
pip install --upgrade streamlit
```

</Tip>

## **Version 1.33.0**

_Release date: April 4, 2024_

**Highlights**

- ≡ƒæƒ┬áIntroducing [`st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment) to decorate functions and rerun them independently of the whole page. Check out the [docs](/develop/concepts/architecture/fragments) and give your apps a speed boost!
- ≡ƒîÉ┬áIntroducing `st.html` to insert custom HTML into your app! Check out the [docs](/develop/api-reference/utilities/st.html) for how to use it.

**Notable Changes**

- ≡ƒô║┬á[`st.audio`](/develop/api-reference/media/st.audio) and [`st.video`](/develop/api-reference/media/st.video) allow looping and setting an end time ([#8203](https://github.com/streamlit/streamlit/pull/8203), [#8348](https://github.com/streamlit/streamlit/pull/8348)).
- ≡ƒöü┬á`AppTest` allows switching pages with [`AppTest.switch_page`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestswitch_page) ([#8280](https://github.com/streamlit/streamlit/pull/8280)).
- ≡ƒº¬ `format_func` is accessible in `AppTest` for widgets that use it ([#8189](https://github.com/streamlit/streamlit/pull/8189), [#8019](https://github.com/streamlit/streamlit/issues/8019), [#7679](https://github.com/streamlit/streamlit/issues/7679)).
- ≡ƒôê Column configuration now includes [`AreaChartColumn`](/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn). [`LineChartColumn`](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn) no longer shows area ([#8237](https://github.com/streamlit/streamlit/pull/8237)).
- ≡ƒÜº Breaking change: [`st.write`](/develop/api-reference/write-magic/st.write) will no longer set `unsafe_allow_html=True` when passed an object containing a `_repr_html_` method. For more information, see PR [#8238](https://github.com/streamlit/streamlit/pull/8238).

**Other Changes**

- ≡ƒû▒∩╕ÅUsers can click on the widget label to focus on input for `st.number_input`, `st.text_input`, and `st.text_area` ([#8155](https://github.com/streamlit/streamlit/pull/8155)). Thanks, [filiptammergard](https://github.com/filiptammergard)!
- Γ¼å∩╕Å Streamlit supports `packaging` version 24.x ([#8338](https://github.com/streamlit/streamlit/pull/8338), [#8328](https://github.com/streamlit/streamlit/issues/8328)).
- ≡ƒò╕∩╕Å┬áBug fix: Streamlit now watches for changes to imported modules in addition to pages ([#8372](https://github.com/streamlit/streamlit/pull/8372)). Thanks, [zyxue](https://github.com/zyxue)!
- ≡ƒªù┬áBug fix: Overflowing toast messages are correctly truncated ([#8337](https://github.com/streamlit/streamlit/pull/8337), [#8330](https://github.com/streamlit/streamlit/issues/8330)).
- ≡ƒªé┬áBug fix: `st.status` correctly updates to complete when using LangChain's `StreamlitCallbackHandler` ([#8331](https://github.com/streamlit/streamlit/pull/8311)).
- ≡ƒªƒ Bug fix: Custom components no longer show white backgrounds in dark themes ([#8242](https://github.com/streamlit/streamlit/pull/8242), [#8156](https://github.com/streamlit/streamlit/issues/8156), [#7813](https://github.com/streamlit/streamlit/issues/7813)).
- ≡ƒªá Bug fix: Content area width is reduced when a fullscreen icon would otherwise cause horizontal overflow ([#8279](https://github.com/streamlit/streamlit/pull/8279), [#6990](https://github.com/streamlit/streamlit/issues/6990)).
- ≡ƒ¬░ Bug fix: Custom components with undefined frame heights will render with a height of 0 ([#8290](https://github.com/streamlit/streamlit/pull/8290), [#8285](https://github.com/streamlit/streamlit/issues/8285)).
- ≡ƒ¬│┬áBug fix: Restored a check for active sessions to prevent apps from needlessly running when no users are connected ([#8294](https://github.com/streamlit/streamlit/pull/8294)).
- ≡ƒò╖∩╕Å Bug fix: Custom themes have precedence over embedding options ([#8021](https://github.com/streamlit/streamlit/pull/8021), [#7118](https://github.com/streamlit/streamlit/issues/7118)).
- ≡ƒÉ₧┬áBug fix: Reverted the async timer to expire session storage cache to address computational efficiency ([#8281](https://github.com/streamlit/streamlit/pull/8281)).
- ≡ƒÉ¥┬áBug fix: When using `st.popover` with `use_container_width=True`, the popover container's minimum width will match the popover button ([#8266](https://github.com/streamlit/streamlit/pull/8266), [#8261](https://github.com/streamlit/streamlit/issues/8261)).
- ≡ƒÉ£ Bug fix: Using `st.rerun` with a triggering widget in `AppTest` no longer creates an infinite loop ([#8264](https://github.com/streamlit/streamlit/pull/8264), [#7768](https://github.com/streamlit/streamlit/issues/7768)).
- ≡ƒ¬▓┬áBug fix: URLs are correctly decoded in `LinkColumn` if regex is used or if not using fully qualified URLs ([#8258](https://github.com/streamlit/streamlit/pull/8258), [#7064](https://github.com/streamlit/streamlit/issues/7064)).
- ≡ƒÉ¢┬áBug fix: `st.query_params` only sends one `ForwardMsg` when updating multiple parameters ([#8205](https://github.com/streamlit/streamlit/pull/8205), [#8199](https://github.com/streamlit/streamlit/issues/8199)). Thanks, [Asaurus1](https://github.com/Asaurus1)!

## **Version 1.32.0**

_Release date: March 7, 2024_

**Highlights**

- ≡ƒì┐┬áIntroducing `st.popover` to create popover elements in your Streamlit apps. Check out [the docs](/develop/api-reference/layout/st.popover) to see how to use it!

**Notable Changes**

- ≡ƒô║┬áYou can now pass subtitles to [`st.video`](/develop/api-reference/media/st.video)! Check out our [feature demo](https://doc-video-subtitle-inputs.streamlit.app/).
- ΓÜù∩╕Å┬á[`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest) includes support for `st.expander` and `st.status`.
- ≡ƒº¬┬á[`AppTest.from_function`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function) accepts a function that takes arguments and/or returns a value.
- ≡ƒº⌐┬áThe timeout warning for custom components was replaced with an element skeleton to improve the UX for slow-loading components, especially in some cloud-hosted platforms ([#8179](https://github.com/streamlit/streamlit/pull/8179), [#7046](https://github.com/streamlit/streamlit/issues/7046)).
- ≡ƒôä `st.switch_page` and `st.page_link` received significant improvements to path handling, performance, and visual appearance (see below for details).
- ≡ƒªÇ┬áBug fix: Streamlit uses `glide-data-grid` version 6.0.4 to fix a variety of dataframe issues ([#7779](https://github.com/streamlit/streamlit/pull/7779), [#6900](https://github.com/streamlit/streamlit/issues/6900), [#7032](https://github.com/streamlit/streamlit/issues/7032), [#7727](https://github.com/streamlit/streamlit/issues/7727), [#6810](https://github.com/streamlit/streamlit/issues/6810), [#7930](https://github.com/streamlit/streamlit/issues/7930), [#7949](https://github.com/streamlit/streamlit/issues/7949), [#7831](https://github.com/streamlit/streamlit/issues/7831), [#8168](https://github.com/streamlit/streamlit/issues/8168)).
- ≡ƒÆª Bug fix: We've plugged a significant memory leak in the coroutine loop. Apps that generate a large number of small messages between client and server will benefit greatly ([#8068](https://github.com/streamlit/streamlit/pull/8068), [#7989](https://github.com/streamlit/streamlit/issues/7989), [#6510](https://github.com/streamlit/streamlit/issues/6510)).

**Other Changes**

- ≡ƒÆ¬ Multiple modules are now lazy-loaded to speed up Streamlit's import time ([#8150](https://github.com/streamlit/streamlit/pull/8150), [#8143](https://github.com/streamlit/streamlit/pull/8143), [#8134](https://github.com/streamlit/streamlit/pull/8134), [#8113](https://github.com/streamlit/streamlit/pull/8113), [#8125](https://github.com/streamlit/streamlit/pull/8125), [#8111](https://github.com/streamlit/streamlit/pull/8111), [#8109](https://github.com/streamlit/streamlit/pull/8109), [#6066](https://github.com/streamlit/streamlit/issues/6066)).
- ≡ƒû╝∩╕Å┬á`st.write` supports `PIL` images ([#8039](https://github.com/streamlit/streamlit/pull/8039)).
- ≡ƒöù┬á`st.radio` allows markdown links within the items passed to `options` ([#8028](https://github.com/streamlit/streamlit/pull/8028), [#7992](https://github.com/streamlit/streamlit/issues/7992)).
- ≡ƒÆÇ┬áThe┬á`deprecation.showPyplotGlobalUse` config option is deprecated and will be removed in the subsequent release ([#8133](https://github.com/streamlit/streamlit/pull/8133)).
- ≡ƒñû┬áStreamlit supports AzureOpenAI chat stream ([#8107](https://github.com/streamlit/streamlit/pull/8107), [#8084](https://github.com/streamlit/streamlit/issues/8084)).
- ≡ƒîÉ┬áThe `/healthz` endpoint supports the HTTP HEAD method ([#8145](https://github.com/streamlit/streamlit/pull/8145), [#8144](https://github.com/streamlit/streamlit/issues/8144)). Thanks, [rahulmistri1997](https://github.com/rahulmistri1997)!
- ≡ƒîÇ┬áThe `cache` parameter for┬á`st.spinner` is now private (`_cache`) since it's for internal use ([#8118](https://github.com/streamlit/streamlit/pull/8118)).
- ≡ƒÅâ┬áSession storage is checked and expired asynchronously to improve performance and efficiency of apps with lower traffic ([#8083](https://github.com/streamlit/streamlit/pull/8083)).
- ≡ƒÉ£┬á`st.write_stream` raises a descriptive `Exception` when the message cannot be parsed ([#8036](https://github.com/streamlit/streamlit/pull/8036)).
- ≡ƒôÿ┬áFixed a typo in the examples for `st.switch_page` and `st.page_link` ([#8162](https://github.com/streamlit/streamlit/pull/8162)). Thanks, [t1emp0](https://github.com/t1emp0)!
- ≡ƒæ╗┬áBug fix:┬á`st.help` correctly displays conditional members ([#8228](https://github.com/streamlit/streamlit/pull/8228)).
- ≡ƒªï┬áBug fix: App State fully clears on page change to prevent lingering stale elements ([#8208](https://github.com/streamlit/streamlit/pull/8208)).
- ≡ƒªÄ┬áBug fix: `st.info`, `st.success`, `st.warning`, and `st.error` don't overflow with long markdown strings ([#8194](https://github.com/streamlit/streamlit/pull/8194), [#6394](https://github.com/streamlit/streamlit/issues/6394)).
- ≡ƒÉî┬áBug fix: Streamlit shows a warning that port 3000 is reserved for development when the server port is set to 3000 ([#8152](https://github.com/streamlit/streamlit/pull/8152), [#8149](https://github.com/streamlit/streamlit/issues/8149)).
- ≡ƒò╕∩╕Å┬áBug fix: `st.page_link` and `st.switch_page` have improved path calculation for consistency ([#8127](https://github.com/streamlit/streamlit/pull/8127)).
- ≡ƒªù┬áBug fix: `st.page_link` shows the correct path in browser on hover ([#8086](https://github.com/streamlit/streamlit/pull/8086), [#8080](https://github.com/streamlit/streamlit/issues/8080)).
- ≡ƒªé┬áBug fix: `st.page_link` and `st.switch_page` normalize paths for correct handling in Windows ([#8103](https://github.com/streamlit/streamlit/pull/8103), [#8070](https://github.com/streamlit/streamlit/issues/8070)).
- ≡ƒªƒ┬áBug fix: Script runner uses a while loop instead of recursion to avoid stack overflows ([#8100](https://github.com/streamlit/streamlit/pull/8100)).
- ≡ƒªá Bug fix: `st.page_link` and `st.switch_page` correctly handle relative paths prefixed with `"/"` ([#8085](https://github.com/streamlit/streamlit/pull/8085), [#8081](https://github.com/streamlit/streamlit/issues/8081)).
- ≡ƒ¬░┬áBug fix: `st.image` parses paths in Windows correctly ([#8092](https://github.com/streamlit/streamlit/pull/8092), [#7271](https://github.com/streamlit/streamlit/issues/7271), [#6066](https://github.com/streamlit/streamlit/issues/6066)).
- ≡ƒ¬│┬áBug fix: `st.switch_page` no longer waits for the current page to finish running before switching pages ([#8054](https://github.com/streamlit/streamlit/pull/8054), [#7954](https://github.com/streamlit/streamlit/issues/7954)).
- ≡ƒò╖∩╕Å┬áBug fix: `st.map` and other simple charts correctly handle color when data is not indexed starting from 0 ([#8158](https://github.com/streamlit/streamlit/pull/8158), [#8079](https://github.com/streamlit/streamlit/pull/8079), [#8077](https://github.com/streamlit/streamlit/issues/8077)). Thanks, [awhazell](https://github.com/awhazell)!
- ≡ƒÉ₧┬áBug fix: `st.selectbox`, `st.multiselect`, `st.select_slider`, and `st.radio` use shallow copies of their options to prevent unexpected mutations ([#8064](https://github.com/streamlit/streamlit/pull/8064), [#7534](https://github.com/streamlit/streamlit/issues/7534)).
- ≡ƒÉ¥┬áBug fix: The selected time in `st.time_input` displays correctly in dark mode ([#8056](https://github.com/streamlit/streamlit/pull/8056), [#7436](https://github.com/streamlit/streamlit/issues/7436)).
- ≡ƒ¬▓┬áBug fix: Dataframe scrollbars display correctly in the latest version of Chrome ([#8034](https://github.com/streamlit/streamlit/pull/8034)).
- ≡ƒÉ¢┬áBug fix: Casting `st.query_params` to `str` will print the content of the query parameters instead of the class description ([#8030](https://github.com/streamlit/streamlit/pull/8030)).

## **Version 1.31.0**

_Release date: February 1, 2024_

**Release videos**

- [What's new?](https://www.youtube.com/watch?v=0TSXM-BGqHU)

**Highlights**

- ≡ƒöù┬áIntroducing `st.page_link`! Now, you can build custom navigation menus for your multipage apps. Check out [our docs](/develop/api-reference/widgets/st.page_link) to see how.
- ≡ƒÆª┬áAnnouncing `st.write_stream` to conveniently handle generators and streamed responses. Check out [our docs](/develop/api-reference/write-magic/st.write_stream) to see how making chat apps just got easier.

**Notable Changes**

- ≡ƒô¥┬á`st.chat_input` can be used inline and placed anywhere in the app. You can also have multiple `st.chat_input` widgets on a page ([#7896](https://github.com/streamlit/streamlit/pull/7896)).

**Other Changes**

- ≡ƒº╣┬áInternal refactoring and cleanup ([#7980](https://github.com/streamlit/streamlit/pull/7980)). Thanks, [whitphx](https://github.com/whitphx)!
- Γ¥ä∩╕Å┬áBug fix: Snowpark is now an optional dependency for `SnowflakeConnection` ([#7919](https://github.com/streamlit/streamlit/pull/7919)).
- ≡ƒò╖∩╕Å┬áBug fix: The watchdog suggestion is disabled when `server.fileWatcherType` is set to `none` or `poll` ([#8024](https://github.com/streamlit/streamlit/pull/8024), [#7999](https://github.com/streamlit/streamlit/issues/7999)).
- ≡ƒÉ₧┬áBug fix: Required columns can be hidden when not using `st.data_editor` with dynamic rows ([#7996](https://github.com/streamlit/streamlit/pull/7996), [#7991](https://github.com/streamlit/streamlit/issues/7991)).
- ≡ƒÉ¥┬áBug fix: New period types are supported for pandas 2.2.0 ([#7988](https://github.com/streamlit/streamlit/pull/7988)).
- ≡ƒÉ£┬áBug fix: Custom components receive only the app's origin and path to avoid reloading components when query parameters change ([#7951](https://github.com/streamlit/streamlit/pull/7951), [#7503](https://github.com/streamlit/streamlit/issues/7503)). Thanks, [eric-skydio](https://github.com/eric-skydio)!
- ≡ƒ¬▓┬áBug fix: `st.progress` won't raise an exception when given a value above 1.0 due to float precision ([#7953](https://github.com/streamlit/streamlit/pull/7953), [#5517](https://github.com/streamlit/streamlit/issues/5517)). Thanks, [notiona](https://github.com/notiona)!
- ≡ƒôÜ Streamlit supports`importlib-metadata` version 7 ([#7925](https://github.com/streamlit/streamlit/pull/7925)). Thanks, [elgalu](https://github.com/elgalu)!
- ≡ƒÉ¢┬áBug fix: `AppTest` correctly sees widgets inside containers ([#7923](https://github.com/streamlit/streamlit/pull/7923), [#7711](https://github.com/streamlit/streamlit/issues/7711)).
- ≡ƒÆ┐ Custom components no longer accumulate style elements when re-rendered for better performance ([#7914](https://github.com/streamlit/streamlit/pull/7914)). Thanks, [Tom-Julux](https://github.com/Tom-Julux)!

## **Version 1.30.0**

_Release date: January 11, 2024_

**Release videos**

- [What's new?](https://www.youtube.com/watch?v=OIQskkX_DK0)

**Highlights**

- ≡ƒöä┬áAnnouncing `st.switch_page` to programmatically switch pages in multipage apps! Check out our [docs](/develop/api-reference/navigation/st.switch_page) to learn about this highly anticipated feature!
- Γ¥ôIntroducing `st.query_params` to handle variables passed through your app's URL. Check out our [docs](/develop/api-reference/caching-and-state/st.query_params) to understand this feature and how it's been upgraded and improved from our experimental version!

**Notable Changes**

- ≡ƒôÉ┬á`st.container` can be configured with a height to create grids or scrolling containers ([#7697](https://github.com/streamlit/streamlit/pull/7697), [#2169](https://github.com/streamlit/streamlit/issues/2169), [#2447](https://github.com/streamlit/streamlit/issues/2447)).
- ≡ƒöù┬áFor dataframes,┬á`LinkColumn`┬áhas a simplified UI and can be configured with display text, including programmatically defined text through regular expressions ([#7784](https://github.com/streamlit/streamlit/pull/7784), [#7741](https://github.com/streamlit/streamlit/pull/7741), [#6787](https://github.com/streamlit/streamlit/issues/6787)).
- ≡ƒº¡┬áSidebar navigation for multipage apps can be hidden via configuration ([#7852](https://github.com/streamlit/streamlit/pull/7852)).
- ΓÅ⌐┬áPlotly figures can load even faster when used in combination with `orjson` ([#7860](https://github.com/streamlit/streamlit/pull/7860)). Thanks, [eric-skydio](https://github.com/eric-skydio)!
- ΓÖ╗∩╕Å Behavior change: Query parameters are removed when changing pages ([#7817](https://github.com/streamlit/streamlit/pull/7817),┬á[#6725](https://github.com/streamlit/streamlit/issues/6725),┬á[#5505](https://github.com/streamlit/streamlit/issues/5505)).

**Other Changes**

- ≡ƒ¢á∩╕Å┬á`showFooter` is no longer an embed option since the footer no longer exists ([#7902](https://github.com/streamlit/streamlit/pull/7902), [#7785](https://github.com/streamlit/streamlit/issues/7785)).
- ≡ƒò╡∩╕Å All security concerns should be reported through [HackerOne](https://hackerone.com/snowflake?type=team) ([#7783](https://github.com/streamlit/streamlit/pull/7783)).
- ≡ƒò╖∩╕Å┬áBug fix: Tabs are not disabled when stale to prevent flickering ([#7905](https://github.com/streamlit/streamlit/pull/7905), [#7820](https://github.com/streamlit/streamlit/issues/7820)).
- ≡ƒ¢í∩╕Å┬áBug fix: The full file path is used instead of a prefix to prevent custom components from reaching beyond their own folders ([#7901](https://github.com/streamlit/streamlit/pull/7901)).
- ≡ƒ¬▒┬áBug fix: Widgets raise an exception if its values aren't Python comparable ([#7840](https://github.com/streamlit/streamlit/pull/7840), [#3714](https://github.com/streamlit/streamlit/issues/3714)).
- ≡ƒÉ₧┬áBug fix: The down-arrow icons on expanders maintain a consistent size ([#7596](https://github.com/streamlit/streamlit/pull/7596)). Thanks, [matiboux](https://github.com/matiboux)!
- ≡ƒÉ¥┬áBug fix: Tabs no longer flicker when switching between them ([#7904](https://github.com/streamlit/streamlit/pull/7904)).
- ≡ƒÉ£┬áBug fix: Enter-to-submit is automatically disabled when the associated `st.form_submit_button` is disabled ([#7827](https://github.com/streamlit/streamlit/pull/7827), [#7822](https://github.com/streamlit/streamlit/issues/7822)).
- ≡ƒ¬▓┬áBug fix: Required columns cannot be hidden with column configuration ([#7888](https://github.com/streamlit/streamlit/pull/7888), [#7559](https://github.com/streamlit/streamlit/issues/7559)).
- ≡ƒÉ¢┬áBug fix: Using `nan` as a value in `SelectboxColumn` will raise an error instead of silently failing ([#7887](https://github.com/streamlit/streamlit/pull/7887), [#7558](https://github.com/streamlit/streamlit/issues/7558)).
- ≡ƒîÖ┬áBug fix: Custom component iframes allow dark mode ([#7821](https://github.com/streamlit/streamlit/pull/7821), [#7813](https://github.com/streamlit/streamlit/issues/7813)).
- ≡ƒ¬░┬áBug fix: The command to start Streamlit is not sent to the frontend ([#7787](https://github.com/streamlit/streamlit/pull/7787)).
- ≡ƒÆà┬áBug fix: The background color of `st.toggle` is enhanced for better visibility ([#7788](https://github.com/streamlit/streamlit/pull/7788)).
- ≡ƒ¬│┬áBug fix: Built-in charts can handle ordered categorical columns ([#7771](https://github.com/streamlit/streamlit/pull/7771), [#7776](https://github.com/streamlit/streamlit/issues/7776)).

## **Version 1.29.0**

_Release date: November 30, 2023_

**Highlights**

- ≡ƒö▓┬á[`st.container`](/develop/api-reference/layout/st.container) and [`st.form`](/develop/api-reference/execution-flow/st.form) now have a `border` parameter to show or hide a border.
- ≡ƒÉì┬áStreamlit supports Python 3.12!

**Notable Changes**

- Γî¢ `st.dataframe`, `st.data_editor`, and `st.table` support `datetime.timedelta` values ([#7689](https://github.com/streamlit/streamlit/pull/7689), [#4489](https://github.com/streamlit/streamlit/issues/4489)).
- ≡ƒÆÇ┬áStreamlit apps preload skeleton elements for a smoother appearance when initializing ([#7598](https://github.com/streamlit/streamlit/pull/7598)).
- ≡ƒÅâ┬áReduced the overhead of running `AppTest`-simulated apps, especially for fast-running apps ([#7691](https://github.com/streamlit/streamlit/pull/7691)).
- ≡ƒ¢ü┬áString representations of `AppTest` data are improved for a better testing and debugging experience ([#7658](https://github.com/streamlit/streamlit/pull/7658)).
- ≡ƒöó Apps can be configured to identify `Enum` classes as the same if they have matching member names ([#7408](https://github.com/streamlit/streamlit/pull/7408), [#4909](https://github.com/streamlit/streamlit/issues/4909)). Thanks, [Asaurus1](https://github.com/Asaurus1)!
- Γ¥î The "Made with Streamlit" footer no longer appears at the bottom of apps ([#7583](https://github.com/streamlit/streamlit/pull/7583)).
- ≡ƒº╣ Unused config options have been deprecated ([#7584](https://github.com/streamlit/streamlit/pull/7584)).
- ≡ƒò│∩╕Å Query parameters can be empty ([#7601](https://github.com/streamlit/streamlit/pull/7601), [#7416](https://github.com/streamlit/streamlit/issues/7416)).
- ≡ƒÆà┬áVisual tweaks ([#7592](https://github.com/streamlit/streamlit/pull/7592), [#7630](https://github.com/streamlit/streamlit/pull/7630)).

**Other Changes**

- ≡ƒªù┬áBug fix: Convert floats to bytes instead of hashing to avoid hashing instability ([#7754](https://github.com/streamlit/streamlit/pull/7754)). Thanks, [BlackHC](https://github.com/BlackHC)!
- ≡ƒªÄ┬áBug fix: Corrected broken URLs and typos in error messages ([#7746](https://github.com/streamlit/streamlit/pull/7746), [#7764](https://github.com/streamlit/streamlit/pull/7764), [#7770](https://github.com/streamlit/streamlit/pull/7770)). Thanks, [ObservedObserver](https://github.com/ObservedObserver)!
- ≡ƒÉî┬áBug fix: `st.connection` correctly caches results when using two connections of the same type ([#7730](https://github.com/streamlit/streamlit/pull/7730), [#7709](https://github.com/streamlit/streamlit/issues/7709)).
- ≡ƒò╕∩╕Å┬áBug fix: Using context managers with multithreading now displays content in the expected order ([#7715](https://github.com/streamlit/streamlit/pull/7715), [#7668](https://github.com/streamlit/streamlit/issues/7668)). Thanks, [eric-skydio](https://github.com/eric-skydio)!
- ≡ƒªé┬áBug fix: Added https fallback when obtaining the host machine's address ([#7712](https://github.com/streamlit/streamlit/pull/7712), [#7703](https://github.com/streamlit/streamlit/issues/7703)). Thanks, [LarsHill](https://github.com/LarsHill)!
- ≡ƒ¢í∩╕Å┬áBug fix: Added security patch for `pyarrow` vulnerability. Custom components using `pyarrow` table deserialization should require `pyarrow>=14.0.1` ([#7695](https://github.com/streamlit/streamlit/pull/7695), [#7700](https://github.com/streamlit/streamlit/issues/7700)).
- ≡ƒªƒ┬áBug fix: Improved typing for `st.connection` ([#7671](https://github.com/streamlit/streamlit/pull/7671)). Thanks, [thezanke](https://github.com/thezanke)!
- ≡ƒ¬░┬áBug fix: Retries of `SnowflakeConnection` methods are narrowed to only occur with transient errors to avoid unnecessary repeated errors ([#7645](https://github.com/streamlit/streamlit/pull/7645), [#7637](https://github.com/streamlit/streamlit/issues/7637)).
- ≡ƒÅù∩╕Å Removed the v0 testing framework which was undocumented ([#7657](https://github.com/streamlit/streamlit/pull/7657)).
- ≡ƒ¬│┬áBug fix: The navigation expander arrow no longer disappears ([#7634](https://github.com/streamlit/streamlit/pull/7634), [#7547](https://github.com/streamlit/streamlit/issues/7547)).
- Γ¥ä∩╕Å Improved the error message for `SnowflakeConnection` when a configuration is not found ([#7652](https://github.com/streamlit/streamlit/pull/7652)).
- ≡ƒò╖∩╕Å┬áBug fix: `st.rerun` no longer causes a `RecursionError` when used with `st.chat_input` ([#7643](https://github.com/streamlit/streamlit/pull/7643), [#7629](https://github.com/streamlit/streamlit/issues/7629)).
- ≡ƒÉ₧┬áBug fix: `st.file_uploader` no longer causes an extra rerun and therefore doesn't conflict with `st.chat_input` ([#7641](https://github.com/streamlit/streamlit/pull/7641), [#7556](https://github.com/streamlit/streamlit/issues/7556)).
- ≡ƒÉ¥┬áBug fix: `AppTest` no longer raises an error when encountering `st.container` ([#7644](https://github.com/streamlit/streamlit/pull/7644), [#7636](https://github.com/streamlit/streamlit/issues/7636)).
- ≡ƒ¬▓ Bug fix: Graphviz charts scale correctly when exiting fullscreen view ([#7398](https://github.com/streamlit/streamlit/pull/7398), [#7527](https://github.com/streamlit/streamlit/issues/6527)).
- ≡ƒÄÑ┬áBug fix: "Record a screencast" is hidden when known to be unsupported in a browser ([#7604](https://github.com/streamlit/streamlit/pull/7604)).
- ≡ƒÉ¢┬áBug fix: Increased the top padding of embedded apps to better display the dataframe toolbar ([#7681](https://github.com/streamlit/streamlit/pull/7681), [#7609](https://github.com/streamlit/streamlit/pull/7609), [#7607](https://github.com/streamlit/streamlit/issues/7607)).
- ≡ƒÉ£┬áBug fix: `st.rerun` uses `NoReturn` for improved type checking ([#7422](https://github.com/streamlit/streamlit/pull/7422)) Thanks, [kongzii](https://github.com/kongzii).

## **Version 1.28.0**

_Release date: October 26, 2023_

**Release videos**

- [Introducing `AppTest`](https://www.youtube.com/watch?v=99OEoP5sy0U)

**Highlights**

- ≡ƒº¬ Introducing a new testing framework for Streamlit apps! Check out our [documentation](/develop/api-reference/app-testing) to learn how to build automated tests for your apps.
- ≡ƒÆ╗ Announcing the general availability of `st.connection`, a command to conveniently manage connections in Streamlit apps. Check out the [docs](/develop/api-reference/connections/st.connection) to learn more.
- Γ¥ä∩╕Å `SnowparkConnection` has been upgraded to the new and improved `SnowflakeConnection` ΓÇö the same, great functionality _plus more_! Check out our [built-in connections](/develop/api-reference/connections#built-in-connections).
- ≡ƒ¢á∩╕Å `st.dataframe` and `st.data_editor` have a new toolbar! Users can search and download data in addition to enjoying improved UI for row additions and deletions. See our updated guide on [Dataframes](/develop/concepts/design/dataframes).

**Notable Changes**

- ≡ƒîÇ When using a spinner with cached functions, the spinner will be overlaid instead of pushing content down ([#7488](https://github.com/streamlit/streamlit/pull/7488)).
- ≡ƒôà `st.data_editor` now supports datetime index editing ([#7483](https://github.com/streamlit/streamlit/pull/7483)).
- ≡ƒöó Improved support for `decimal.Decimal` in `st.dataframe` and `st.data_editor` ([#7475](https://github.com/streamlit/streamlit/pull/7475)).
- ≡ƒÑ╕ Global kwargs were added for `hashlib` ([#7527](https://github.com/streamlit/streamlit/pull/7527), [#7526](https://github.com/streamlit/streamlit/issues/7526)). Thanks, [DueViktor](https://github.com/DueViktor)!
- ≡ƒôï `st.components.v1.iframe` now permits writing to clipboard ([#7487](https://github.com/streamlit/streamlit/pull/7487)). Thanks, [dilipthakkar](https://github.com/dilipthakkar)!
- ≡ƒô¥ `SafeSessionState` disconnect was replaced with script runner yield points for improved efficiency and clarity ([#7373](https://github.com/streamlit/streamlit/pull/7373)).
- ≡ƒñû The Langchain callback handler will show the full input string inside the body of a `st.status` when the input string is too long to show as a label ([#7478](https://github.com/streamlit/streamlit/pull/7478)). Thanks, [pokidyshev](https://github.com/pokidyshev)!
- ≡ƒôê `st.graphviz_chart` now supports using different Graphviz layout engines ([#7505](https://github.com/streamlit/streamlit/pull/7505), [#4089](https://github.com/streamlit/streamlit/issues/4089)).
- ≡ƒªï┬áAssorted visual tweaks ([#7486](https://github.com/streamlit/streamlit/pull/7486), [#7592](https://github.com/streamlit/streamlit/pull/7592)).
- ≡ƒôè `plotly.js` was upgraded to version 2.26.1 ([#7449](https://github.com/streamlit/streamlit/pull/7449), [#7476](https://github.com/streamlit/streamlit/issues/7476), [#7045](https://github.com/streamlit/streamlit/issues/7045)).
- ≡ƒÆ╜ Legacy serialization for DataFrames was removed. All DataFrames will be serialized by Apache Arrow ([#7429](https://github.com/streamlit/streamlit/pull/7429)).
- ≡ƒû╝∩╕Å Compatibility for Pillow 10.x was added ([#7442](https://github.com/streamlit/streamlit/pull/7442)).
- ≡ƒô¼ Migrated `_stcore/allowed-message-origins` endpoint to┬á`_stcore/host-config`┬á([#7342](https://github.com/streamlit/streamlit/pull/7342)).
- ≡ƒÆ¼ Added┬á`post_parent_message`┬áplatform command to send┬ácustom┬ámessages from a Streamlit app to its parent window ([#7522](https://github.com/streamlit/streamlit/pull/7522)).

**Other Changes**

- Γî¿∩╕Å Improved string dtype handling for DataFrames ([#7479](https://github.com/streamlit/streamlit/pull/7479)).
- Γ£Æ∩╕Å `st.write` will avoid using `unsafe_allow_html=True` if possible ([#7432](https://github.com/streamlit/streamlit/pull/7432)).
- ≡ƒÉ¢┬áBug fix: Implementation of `st.expander` was simplified for improved behavior and consistency ([#7247](https://github.com/streamlit/streamlit/pull/7247), [#2839](https://github.com/streamlit/streamlit/issues/2839), [#4111](https://github.com/streamlit/streamlit/issues/4111), [#4651](https://github.com/streamlit/streamlit/issues/4651), [#5604](https://github.com/streamlit/streamlit/issues/5604)).
- ≡ƒ¬▓┬áBug fix: Multipage links in the sidebar are now aligned with other sidebar elements ([#7531](https://github.com/streamlit/streamlit/pull/7531)).
- ≡ƒÉ£┬áBug fix: `st.chat_input` won't incorrectly prompt for `label` parameter in IDEs ([#7560](https://github.com/streamlit/streamlit/pull/7560)).
- ≡ƒÉ¥┬áBug fix: Scroll bars correctly overlay `st.dataframe` and `st.data_editor` without adding empty space ([#7090](https://github.com/streamlit/streamlit/pull/7090), [#6888](https://github.com/streamlit/streamlit/issues/6888)).
- ≡ƒÉ₧┬áBug fix: `st.chat_message` behaves correctly with the removal of AutoSizer ([#7504](https://github.com/streamlit/streamlit/pull/7504), [#7473](https://github.com/streamlit/streamlit/issues/7473)).
- ≡ƒò╖∩╕Å┬áBug fix: Anchor links are reliably produced for non-English headers ([#7454](https://github.com/streamlit/streamlit/pull/7454), [#5291](https://github.com/streamlit/streamlit/issues/5291)).
- Γÿâ∩╕Å┬áBug fix: `st.connections.SnowparkConnection` more accurately detects when it's running within Streamlit in Snowflake ([#7502](https://github.com/streamlit/streamlit/pull/7502)).
- ≡ƒ¬│┬áBug fix: A user-friendly warning is shown when exceeding the size limitations of a pandas `Styler` object ([#7497](https://github.com/streamlit/streamlit/pull/7497), [#5953](https://github.com/streamlit/streamlit/issues/5953)).
- ≡ƒ¬░┬áBug fix: `st.data_editor` automatically converts non-string column names to strings ([#7485](https://github.com/streamlit/streamlit/pull/7485), [#6950](https://github.com/streamlit/streamlit/issues/6950)).
- ≡ƒªá┬áBug fix: `st.data_editor` correctly identifies non-range indices as a required column ([#7481](https://github.com/streamlit/streamlit/pull/7481), [#6995](https://github.com/streamlit/streamlit/issues/6995)).
- ≡ƒªƒ┬áBug fix: `st.file_uploader` displays compound file extensions like `csv.gz` correctly ([#7362](https://github.com/streamlit/streamlit/pull/7362)). Thanks, [mo42](https://github.com/mo42)!
- ≡ƒªé┬áBug fix: Column Configuration no longer uses deprecated type checks ([#7496](https://github.com/streamlit/streamlit/pull/7496), [#7477](https://github.com/streamlit/streamlit/pull/7477), [#7550](https://github.com/streamlit/streamlit/issues/7550)). Thanks, [c-bik](https://github.com/c-bik)!
- ≡ƒªù┬áBug fix: Additional toolbar items no longer stack vertically ([#7470](https://github.com/streamlit/streamlit/pull/7470), [#7471](https://github.com/streamlit/streamlit/issues/7471)).
- ≡ƒò╕∩╕Å┬áBug fix: Column Configuration no longer causes a type warning in Mypy ([#7457](https://github.com/streamlit/streamlit/pull/7457)). Thanks, [kopp](https://github.com/kopp)!
- ≡ƒÉî┬áBug fix: Bokeh Sliders no longer cause JavaScript errors ([#7441](https://github.com/streamlit/streamlit/pull/7441), [#7171](https://github.com/streamlit/streamlit/issues/7171)).
- ≡ƒªÄ┬áBug fix: Caching now recognizes DataFrames with the same values but different column names as different ([#7331](https://github.com/streamlit/streamlit/pull/7331), [#7086](https://github.com/streamlit/streamlit/issues/7086)).

## **Version 1.27.0**

_Release date: September 21, 2023_

**Highlights**

- Γ£¿┬áIntroducing `st.scatter_chart` ΓÇö a new, simple chart element to build scatter charts Streamlit-y fast and easy! See our [documentation](/develop/api-reference/charts/st.scatter_chart).
- ≡ƒöù┬áIntroducing `st.link_button`! Want to open an external link in a new tab with a bit more pizazz than a plain-text link? Check out our [documentation](/develop/api-reference/widgets/st.link_button) to see how.
- ≡ƒÅâ┬áAnnouncing the general availability of [`st.rerun`](/develop/api-reference/execution-flow/st.rerun), a command to interrupt your script and trigger an immediate rerun.

**Notable Changes**

- ≡ƒæ╗┬áYou can initialize widgets with an empty state by setting┬á`None`┬áas an initial value for┬á[`st.number_input`](/develop/api-reference/widgets/st.number_input), [`st.selectbox`](/develop/api-reference/widgets/st.selectbox), [`st.date_input`](/develop/api-reference/widgets/st.date_input), [`st.time_input`](/develop/api-reference/widgets/st.time_input), [`st.radio`](/develop/api-reference/widgets/st.radio), [`st.text_input`](/develop/api-reference/widgets/st.text_input), and [`st.text_area`](/develop/api-reference/widgets/st.text_area)!
- ≡ƒôñ┬á[`st.download_button`](/develop/api-reference/widgets/st.download_button) now uses `target="_self"` instead of opening a new tab ([#7151](https://github.com/streamlit/streamlit/pull/7151), [#7132](https://github.com/streamlit/streamlit/issues/7132)).
- ≡ƒºƒ┬áRemoved unmaintained `pympler` dependency ([#7193](https://github.com/streamlit/streamlit/pull/7193), [#7131](https://github.com/streamlit/streamlit/issues/7131)). Thanks, [rudyardrichter](https://github.com/rudyardrichter)!

**Other Changes**

- ≡ƒÉ¢┬áBug fix: `st.multiselect` now shows a correct message when no result matches a user's search ([#7205](https://github.com/streamlit/streamlit/pull/7205), [#7116](https://github.com/streamlit/streamlit/issues/7116)).
- ≡ƒ¬▓┬áBug fix: `st.experimental_user` now defaults to `test@example.com` ([#7219](https://github.com/streamlit/streamlit/pull/7219), [#7215](https://github.com/streamlit/streamlit/issues/7215)).
- ≡ƒÉ£┬áBug fix: `st.slider` labels don't overlap when small ranges are selected ([#7221](https://github.com/streamlit/streamlit/pull/7221), [#3385](https://github.com/streamlit/streamlit/issues/3385)).
- ≡ƒÉ¥┬áBug fix: Type-checking correctly identifies all string types to avoid hashing errors ([#7255](https://github.com/streamlit/streamlit/pull/7255), [#6455](https://github.com/streamlit/streamlit/issues/6455)).
- ≡ƒÉ₧┬áBug fix: JSON is parsed with JSON5 to avoid errors from null values when using `st.pydeck_chart` ([#7256](https://github.com/streamlit/streamlit/pull/7256), [#5799](https://github.com/streamlit/streamlit/issues/5799)).
- ≡ƒò╖∩╕Å┬áBug fix: Identical widgets on different pages are correctly interpreted by Streamlit as distinct ([#7264](https://github.com/streamlit/streamlit/pull/7264), [#6146](https://github.com/streamlit/streamlit/issues/6146)).
- ≡ƒªï┬áBug fix: Visual tweaks to widgets for responsive behavior ([#7145](https://github.com/streamlit/streamlit/pull/7145)).
- ≡ƒ¬│┬áBug fix: SVGs are accurately displayed ([#7183](https://github.com/streamlit/streamlit/pull/7183), [#3882](https://github.com/streamlit/streamlit/issues/3882)).
- ≡ƒ¬░┬áBug fix: `st.video` correctly updates with changes to `start_time` ([#7257](https://github.com/streamlit/streamlit/pull/7257), [#7126](https://github.com/streamlit/streamlit/issues/7126)).
- ≡ƒªá┬áBug fix: Additional error handling was added to `st.session_state` ([#7280](https://github.com/streamlit/streamlit/pull/7280), [#7206](https://github.com/streamlit/streamlit/issues/7206)).
- ≡ƒªƒ┬áBug fix: `st.map` correctly refreshes with new data ([#7307](https://github.com/streamlit/streamlit/pull/7307), [#7294](https://github.com/streamlit/streamlit/issues/7294)).
- ≡ƒªé┬áBug fix: The decorative app header line is no longer covered by the sidebar ([#7297](https://github.com/streamlit/streamlit/pull/7297), [#6264](https://github.com/streamlit/streamlit/issues/6264)).
- ≡ƒªù┬áBug fix: `st.code` no longer triggers a `CachedStFunctionWarning` ([#7306](https://github.com/streamlit/streamlit/pull/7306), [#7055](https://github.com/streamlit/streamlit/issues/7055)).
- ≡ƒò╕∩╕Å┬áBug fix: `st.download_button` no longer resets with different `data` ([#7316](https://github.com/streamlit/streamlit/pull/7316), [#7308](https://github.com/streamlit/streamlit/issues/7308)).
- ≡ƒÉî┬áBug fix: Widgets consistently recognize user interaction while a page is still running, with or without `fastRerun` enabled ([#7283](https://github.com/streamlit/streamlit/pull/7283), [#6643](https://github.com/streamlit/streamlit/issues/6643)).
- ≡ƒªÄ┬áBug fix: `st.tabs` was improved to better handle and render conditionally appearing tabs ([#7287](https://github.com/streamlit/streamlit/pull/7287), [#7310](https://github.com/streamlit/streamlit/pull/7310), [#5454](https://github.com/streamlit/streamlit/issues/5454), [#7040](https://github.com/streamlit/streamlit/issues/7040)).

## **Version 1.26.0**

_Release date: August 24, 2023_

**Highlights**

- ≡ƒñû Introducing `st.status` to display output from long-running processes and external API calls ([#7140](https://github.com/streamlit/streamlit/pull/7140)). Works great with `st.chat_message`! See our [documentation](/develop/api-reference/status/st.status) for how to use this feature.
- ≡ƒÜÑ┬áIntroducing [`st.toggle`](/develop/api-reference/widgets/st.toggle) ΓÇö an alternative to `st.checkbox` when you need an on/off switch.

**Notable Changes**

- ≡ƒÄ¿ Simple [chart elements](/develop/api-reference/charts) have a `color` parameter to set the color of your data points or series ([#7022](https://github.com/streamlit/streamlit/pull/7022)).
- ≡ƒîê┬á[Markdown](/develop/api-reference/text/st.markdown) supports rainbow and gray colors ([#7106](https://github.com/streamlit/streamlit/pull/7106), [#7179](https://github.com/streamlit/streamlit/pull/7179)).
- ≡ƒôÅ [`st.header`](/develop/api-reference/text/st.header) and [`st.subheader`](/develop/api-reference/text/st.subheader) have optional, colored dividers ([#7133](https://github.com/streamlit/streamlit/pull/7133)).
- ≡ƒÜÇ Deploying to Community Cloud is even easierΓÇölocally running apps have a [deploy button](/develop/concepts/architecture/app-chrome#deploy-this-app) in their toolbars ([#7085](https://github.com/streamlit/streamlit/pull/7085), [#6935](https://github.com/streamlit/streamlit/issues/6935)).
- ≡ƒûî∩╕Å [`st.download_button`](/develop/api-reference/widgets/st.download_button) has a new parameter `type` for theming ([#7056](https://github.com/streamlit/streamlit/pull/7056), [#7038](https://github.com/streamlit/streamlit/issues/7038)).
- ≡ƒñû [`st.chat_message`](/develop/api-reference/chat/st.chat_message) has ai and human presets for messages ([#7094](https://github.com/streamlit/streamlit/pull/7094)).
- ≡ƒÆà [`st.radio`](/develop/api-reference/widgets/st.radio) options support markdown and have captions ([#7018](https://github.com/streamlit/streamlit/pull/7018), [#7105](https://github.com/streamlit/streamlit/pull/7105), [#6085](https://github.com/streamlit/streamlit/issues/6085)).
- ≡ƒº╝┬áAssorted visual tweaks ([#7050](https://github.com/streamlit/streamlit/pull/7050), [#894](https://github.com/streamlit/streamlit/issues/894)).
- ≡ƒ¢Å∩╕Å Replaced deprecated `imghdr` dependency with `pillow` ([#7081](https://github.com/streamlit/streamlit/pull/7081), [#7027](https://github.com/streamlit/streamlit/issues/7027)).
- ≡ƒöó [`st.number_input`](/develop/api-reference/widgets/st.number_input)'s step buttons (+/-) are ignored during tabbing navigation ([#7154](https://github.com/streamlit/streamlit/pull/7154)). Thanks [@denck007](https://github.com/denck007)!

**Other Changes**

- ≡ƒì₧ Bug fix: Toast messages are no longer blocked by `st.chat_input` ([#7204](https://github.com/streamlit/streamlit/pull/7204), [#7115](https://github.com/streamlit/streamlit/issues/7115)).
- ≡ƒò╕∩╕Å┬áBug fix: Widget IDs are now stable to prevent inconsistent statefulness ([#7003](https://github.com/streamlit/streamlit/pull/7003)).
- ≡ƒªƒ┬áBug fix: Browser autofill is correctly recognized within forms now ([#7150](https://github.com/streamlit/streamlit/pull/7150), [#7101](https://github.com/streamlit/streamlit/issues/7101), [#7084](https://github.com/streamlit/streamlit/issues/7084)).
- ≡ƒ¬▒ Bug fix: `st.file_uploader` no longer causes session state to reset when a websocket connection is dropped and reconnected ([#7149](https://github.com/streamlit/streamlit/pull/7149), [#7025](https://github.com/streamlit/streamlit/pull/7025)).
- ≡ƒÅÄ∩╕Å Bug fix: Pydeck JSON data is cached for improved performance ([#7113](https://github.com/streamlit/streamlit/pull/7113), [#5532](https://github.com/streamlit/streamlit/issues/5532)).
- ≡ƒªï Bug fix: `st.chat_input` no longer submits prematurely while typing with an input method editor ([#6993](https://github.com/streamlit/streamlit/pull/6993)).
- ≡ƒÉ₧ Bug fix: Label backgrounds for `st.tabs` are now transparent ([#7070](https://github.com/streamlit/streamlit/pull/7070), [#5707](https://github.com/streamlit/streamlit/issues/5707)).
- ≡ƒÉ¥ Bug fix: Page width is no longer ignored when using the `help` parameter in `st.button` ([#7033](https://github.com/streamlit/streamlit/pull/7033), [#6161](https://github.com/streamlit/streamlit/issues/6161)).
- ≡ƒÉ£ Bug fix: Tweaked Altair color specification for improved visibility in dark mode ([#7061](https://github.com/streamlit/streamlit/pull/7061), [#3343](https://github.com/streamlit/streamlit/issues/3343)).
- ≡ƒ¬▓┬áBug fix: `st.chat_message` can correctly use local images as avatars ([#7130](https://github.com/streamlit/streamlit/pull/7130)).
- ≡ƒÉ¢ Bug fix: Specified that MD5 is not used for security ([#7122](https://github.com/streamlit/streamlit/pull/7122), [#7120](https://github.com/streamlit/streamlit/issues/7120)).
- ≡ƒ¬ä Bug fix: Async function docstrings are ignored by [Streamlit magic](/develop/api-reference/write-magic/magic) ([#7143](https://github.com/streamlit/streamlit/pull/7143), [#7137](https://github.com/streamlit/streamlit/issues/7137)).

## **Version 1.25.0**

_Release date: July 20, 2023_

**Highlights**

- ≡ƒì₧┬áIntroducing `st.toast` ΓÇö a command to briefly show toast messages to users in the bottom-right corner of apps. See [our documentation](/develop/api-reference/status/st.toast) on how to use this feature.

**Notable Changes**

- ≡ƒù║∩╕Å┬á[`st.map`](/develop/api-reference/charts/st.map) now has parameters for `latitude`, `longitude`, `color`, and `size` to customize data points ([#6896](https://github.com/streamlit/streamlit/pull/6896)).
- ≡ƒÜ⌐┬á[`st.multiselect`](/develop/api-reference/widgets/st.multiselect) supports setting placeholders and specifying the maximum number of selections via the `placeholder` and `max_selections` keyword-only arguments, respectively ([#6901](https://github.com/streamlit/streamlit/pull/6901), [#4750](https://github.com/streamlit/streamlit/issues/4750)). Thanks, [@fhiroki](https://github.com/fhiroki)!
- ≡ƒôà┬áCustomize the date format for `st.date_input` with the `format` parameter ([#6974](https://github.com/streamlit/streamlit/pull/6974), [#5234](https://github.com/streamlit/streamlit/issues/5234)).
- Γå⌐∩╕Å [Forms](/develop/api-reference/execution-flow/st.form) can now be submitted with Enter/Return while inside [`st.text_input`](/develop/api-reference/widgets/st.text_input), [`st.number_input`](/develop/api-reference/widgets/st.number_input), or [`st.text_area`](/develop/api-reference/widgets/st.text_area) ([#6911](https://github.com/streamlit/streamlit/pull/6911), [#3790](https://github.com/streamlit/streamlit/issues/3790)).
- ≡ƒìó┬áThe app menu icon in the upper-right corner of apps has been changed from "**Γÿ░**" to "**Γï«**" ([#6947](https://github.com/streamlit/streamlit/pull/6947)).

**Other Changes**

- Γ¢ô∩╕Å Minimum required versions increased for multiple Python dependencies, including `numpy>=1.19.3` and `pandas>=1.3.0` ([#6802](https://github.com/streamlit/streamlit/pull/6802)).
- ≡ƒ¢í∩╕Å┬á`protobufjs` was bumped from 7.2.1 to 7.2.4 ([#6959](https://github.com/streamlit/streamlit/pull/6959)).
- Γ£¿┬áVisual design tweaks to Streamlit's input widgets ([#6944](https://github.com/streamlit/streamlit/pull/6944)).
- ≡ƒªï Bug Fix: `st.slider` now accepts general number types like `numpy.int64` instead of just `int` and `float` ([#6816](https://github.com/streamlit/streamlit/pull/6816), [#6815](https://github.com/streamlit/streamlit/issues/6815)). Thanks, [@milliams](https://github.com/milliams)!
- ≡ƒÉ£┬áBug Fix: Data labels for `st.slider` and `st.select_slider` no longer overflow when inside `st.expander` ([#6828](https://github.com/streamlit/streamlit/pull/6828), [#6297](https://github.com/streamlit/streamlit/issues/6297)).
- ≡ƒÉ¢┬áBug Fix: Elements no longer re-render from scratch with each rerun ([#6923](https://github.com/streamlit/streamlit/pull/6923), [#6920](https://github.com/streamlit/streamlit/issues/6920)).
- ≡ƒÉ₧┬áBug Fix: `st.data_editor` hashes styler objects correctly for stability across reruns ([#6815](https://github.com/streamlit/streamlit/pull/6915), [#6898](https://github.com/streamlit/streamlit/issues/6898)).
- ≡ƒÉ¥┬áBug Fix: Fixed the padding for embedded apps using `st.chat_input` to prevent messages being cutoff ([#6979](https://github.com/streamlit/streamlit/pull/6979)).

## **Version 1.24.0**

_Release date: June 27, 2023_

**Highlights**

- ≡ƒÆ¼ Introducing `st.chat_message` and `st.chat_input` ΓÇö two new [chat elements](/develop/api-reference/chat) that let you build conversational apps. Learn how to use these features in your LLM-powered chat apps in our [tutorial](/develop/tutorials/llms/build-conversational-apps).
- ≡ƒÆ╛┬áStreamlit's caching decorators now allow you to customize Streamlit's hashing of input parameters with the keyword-only argument [`hash_funcs`](/develop/concepts/architecture/caching#the-hash_funcs-parameter).

**Notable Changes**

- ≡ƒÉì┬áWe've deprecated support for Python 3.7 in the core library and Streamlit Community Cloud ([#6868](https://github.com/streamlit/streamlit/pull/6868)).
- ≡ƒôà┬á`st.cache_data` and `st.cache_resource` can hash timezone-aware `datetime` objects ([#6812](https://github.com/streamlit/streamlit/pull/6812), [#6690](https://github.com/streamlit/streamlit/issues/6690), [#5110](https://github.com/streamlit/streamlit/issues/5110)).

**Other Changes**

- Γ£¿┬áVisual design tweaks to Streamlit's input widgets ([#6817](https://github.com/streamlit/streamlit/pull/6817)).
- ≡ƒÉ¢┬áBug fix: `st.write` pretty-prints dataclasses using `st.help` ([#6750](https://github.com/streamlit/streamlit/pull/6750)).
- ≡ƒ¬▓┬áBug fix: `st.button`'s height is consistent with that of other widgets ([#6738](https://github.com/streamlit/streamlit/pull/6738)).
- ≡ƒÉ£┬áBug fix: Upgraded the `react-range` frontend dependency to fix the memory usage of sliders ([#6764](https://github.com/streamlit/streamlit/pull/6764), [#5436](https://github.com/streamlit/streamlit/issues/5436)). Thanks [@wolfd](https://github.com/wolfd)!
- ≡ƒÉ¥┬áBug fix: Pydantic validators no longer result in exceptions on app reruns ([#6664](https://github.com/streamlit/streamlit/pull/6664), [#3218](https://github.com/streamlit/streamlit/issues/3218)).
- ≡ƒÉ₧┬áBug fix: `streamlit config show` honors newlines ([#6758](https://github.com/streamlit/streamlit/pull/6758), [#2868](https://github.com/streamlit/streamlit/issues/2868)).
- ≡ƒ¬░┬áBug fix: Fixed a race condition to ensure Streamlit reruns the latest code when the file changes ([#6884](https://github.com/streamlit/streamlit/pull/6884)).
- ≡ƒªï┬áBug fix: Apps no longer rerun when users click anchor links ([#6834](https://github.com/streamlit/streamlit/pull/6834), [#6500](https://github.com/streamlit/streamlit/issues/6500)).
- ≡ƒò╕∩╕Å┬áBug fix: Added robust out-of-bounds checks for `min_value` and `max_value` in `st.number_input` ([#6847](https://github.com/streamlit/streamlit/pull/6847), [#6797](https://github.com/streamlit/streamlit/issues/6797)).

## **Version 1.23.0**

_Release date: June 1, 2023_

**Highlights**

- Γ£é∩╕Å Announcing the general availability of [st.data_editor](/develop/api-reference/data/st.data_editor), a widget that allows you to edit DataFrames and many other data structures in a table-like UI. **Breaking change:** the data editor's representation used in `st.session_state` was altered. Find out more about the new format in [Access edited data](/develop/concepts/design/dataframes#access-edited-data).
- ΓÜÖ∩╕Å Introducing the [Column configuration API](/develop/api-reference/data/st.column_config) with a suite of methods to configure the display and editing behavior of `st.dataframe` and `st.data_editor` columns (e.g. their title, visibility, type, or format). Keep an eye out for a detailed [blog post](https://blog.streamlit.io/) and in-depth [documentation](/develop/concepts/design/dataframes#configuring-columns) upcoming in the next two weeks.
- ≡ƒöî Learn to use `st.experimental_connection` to create and manage data connections in your apps with the new [Connecting to data](/develop/concepts/connections/connecting-to-data) docs and [video tutorial](https://www.youtube.com/watch?v=xQwDfW7UHMo).

**Notable Changes**

- ≡ƒôè┬áStreamlit now supports Protobuf 4 and Altair 5 ([#6215](https://github.com/streamlit/streamlit/issues/6215), [#6618](https://github.com/streamlit/streamlit/pull/6618), [#5626](https://github.com/streamlit/streamlit/issues/5626), [#6622](https://github.com/streamlit/streamlit/pull/6622)).
- ΓÿÄ∩╕Å st.dataframe and st.data_editor can hide index columns with `hide_index`, specify the display order of columns with `column_order`, and disable editing for individual columns with the `disabled` parameter.
- ΓÅ▒∩╕Å The `ttl` parameter in [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data) and [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource) accepts formatted strings, so you can simply say `ttl="30d"`, `ttl="1h30m"` and any other combination of `w`, `d`, `h`, `m`, `s` supported by [Pandas's Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html) ([#6560](https://github.com/streamlit/streamlit/pull/6560)).
- ≡ƒôé `st.file_uploader` now interprets the `type` parameter more accurately. For example, "jpg" or ".jpg" now accept both "jpg" and "jpeg" extensions. This functionality has also been extended to "mpeg/mpg", "tiff/tif", "html/htm", and "mpeg4/mp4".
- ≡ƒñ½┬áThe new `global.disableWidgetStateDuplicationWarning` configuration option allows the silencing of warnings triggered by setting widget default values and keyed session state values concurrently ([#3605](https://github.com/streamlit/streamlit/issues/3605), [#6640](https://github.com/streamlit/streamlit/pull/6640)). Thanks, [@antonAce](https://github.com/antonAce)!

**Other Changes**

- ≡ƒÅâΓÇìΓÖÇ∩╕ÅImproved startup time by lazy loading some dependencies ([#6531](https://github.com/streamlit/streamlit/pull/6531)).
- ≡ƒæï Removed `st.beta_*` and `st.experimental_show` due to deprecation and low-use ([#6558](https://github.com/streamlit/streamlit/pull/6558))
- ≡ƒÜÇ┬áFurther improvements to st.dataframe and st.data_editor:
  - Improved editing on mobile devices for the data editor ([#6548](https://github.com/streamlit/streamlit/pull/6548)).
  - All editable columns have an icon in their column header and support tooltips ([#6550](https://github.com/streamlit/streamlit/pull/6550), [#6561](https://github.com/streamlit/streamlit/pull/6561)).
  - Enable editing for columns containing datetime, date, or time values ([#6025](https://github.com/streamlit/streamlit/pull/6025)).
  - New input validation options for columns in the data editor, such as `max_chars` and `validate` for text columns, and `min_value`, `max_value` and `step` for number columns ([#6563](https://github.com/streamlit/streamlit/pull/6563)).
  - Improved type parsing capabilities in the data editor ([#6551](https://github.com/streamlit/streamlit/pull/6551)).
  - Unified missing values to `None` in returned data structures ([#6544](https://github.com/streamlit/streamlit/pull/6544)).
  - A warning is shown in cells when integers exceed the maximum safe value of `(2^53) -1` ([#6311](https://github.com/streamlit/streamlit/issues/6311), [#6549](https://github.com/streamlit/streamlit/pull/6549)).
  - Prevented editing the sessions state by showing a warning ([#6634](https://github.com/streamlit/streamlit/pull/6634)).
  - Fixed issues with list columns sometimes breaking the frontend ([#6644](https://github.com/streamlit/streamlit/pull/6644)).
  - Fixed a display issue with index columns using category dtype ([#6680](https://github.com/streamlit/streamlit/issues/6680), [#6598](https://github.com/streamlit/streamlit/pull/6598)).
  - Fixed an issue that prevented a rerun when adding empty rows ([#6598](https://github.com/streamlit/streamlit/pull/6598)).
  - Unified the behavior between `st.data_editor` and `st.dataframe` related to auto-hiding the index column(s) based on the input data ([#6659](https://github.com/streamlit/streamlit/issues/6659), [#6598](https://github.com/streamlit/streamlit/pull/6598))
- ≡ƒ¢í∩╕Å┬áStreamlit's [Security Policy](https://github.com/streamlit/streamlit/blob/develop/SECURITY.md) can be found in its GitHub repository ([#6666](https://github.com/streamlit/streamlit/pull/6666)).
- ≡ƒñÅ Documented the integer size limit for `st.number_input` and `st.slider` ([#6724](https://github.com/streamlit/streamlit/pull/6724)).
- ≡ƒÉì┬áThe majority of Streamlit's Python dependencies have set a maximum allowable version, with the standard upper limit set to the next major version, but not inclusive of it ([#6691](https://github.com/streamlit/streamlit/pull/6691)).
- ≡ƒÆà┬áUI design improvements to in-app modals ([#6688](https://github.com/streamlit/streamlit/pull/6688)).
- ≡ƒÉ₧┬áBug fix: `st.date_input`'s date selector is equally visible in dark mode ([#6072](https://github.com/streamlit/streamlit/issues/6072), [#6630](https://github.com/streamlit/streamlit/pull/6630)).
- ≡ƒÉ£┬áBug fix: the sidebar navigation expansion indicator in multipage apps is restored ([#6731](https://github.com/streamlit/streamlit/pull/6731)).
- ≡ƒÉ¢┬áBug fix: The docstring and exception message for `st.set_page_config` have been updated to clarify that this command can be invoked once for each page within a multipage app, rather than once per entire app ([#6594](https://github.com/streamlit/streamlit/pull/6594)).
- ≡ƒÉ¥┬áBug fix: `st.json`┬áno longer collapses multiple spaces in both keys and values with single space when rendered ([#6657](https://github.com/streamlit/streamlit/issues/6657), [#6663](https://github.com/streamlit/streamlit/pull/6663)).

## **Version 1.22.0**

_Release date: April 27, 2023_

**Highlights**

- ≡ƒöî┬áIntroducing `st.experimental_connection`: Easily connect your app to data sources and APIs using our new connection feature. Find more details in the [API reference](/develop/api-reference/connections), and stay tuned for an upcoming blog post and in-depth documentation! In the meantime, explore our updated [MySQL](/develop/tutorials/databases/mysql) and [Snowflake](/develop/tutorials/databases/snowflake) connection tutorials for examples of this feature.

**Notable Changes**

- ≡ƒÉ╝┬áStreamlit now supports Pandas 2.0 ([#6413](https://github.com/streamlit/streamlit/issues/6413), [#6378](https://github.com/streamlit/streamlit/pull/6378), [#6507](https://github.com/streamlit/streamlit/pull/6507)). Thanks, [connortann](https://github.com/connortann)!
- ≡ƒìö┬áCustomize the visibility of items in the toolbar, options menu, and the settings dialog using the `client.toolbarMode` [config option](https://docs.streamlit.io/develop/concepts/configuration#view-all-configuration-options) ([#6174](https://github.com/streamlit/streamlit/pull/6174)).
- ≡ƒ¬╡┬áStreamlit logs now reside in the "streamlit" namespace instead of the root logger, enabling app developers to better manage log handling ([#3978](https://github.com/streamlit/streamlit/issues/3978), [#6377](https://github.com/streamlit/streamlit/pull/6377)).

**Other Changes**

- ≡ƒöÅ┬áCLI parameters can no longer be used to set sensitive configuration values ([#6376](https://github.com/streamlit/streamlit/pull/6376)).
- ≡ƒñû┬áImproved the debugging experience by reducing log noise ([#6391](https://github.com/streamlit/streamlit/pull/6391)).
- ≡ƒÉ₧┬áBug fix:┬á`@st.cache_data` decorated functions support UUID objects as parameters ([#6440](https://github.com/streamlit/streamlit/issues/6440), [#6459](https://github.com/streamlit/streamlit/pull/6459)).
- ≡ƒÉ¢┬áBug fix: Tabbing through buttons and other elements now displays a red border only when focused, not when clicked ([#6373](https://github.com/streamlit/streamlit/pull/6373)).
- ≡ƒ¬▓┬áBug fix: `st.multiselect`'s clear icon is larger and includes a hover effect ([#6471](https://github.com/streamlit/streamlit/pull/6471)).
- ≡ƒÉ£┬áBug fix: Custom theme font settings no longer apply to code blocks ([#6484](https://github.com/streamlit/streamlit/issues/6484), [#6535](https://github.com/streamlit/streamlit/pull/6535)).
- ┬⌐∩╕Å┬áBug fix: `st.code`'s copy-to-clipboard button appears when you hover on code blocks ([#6490](https://github.com/streamlit/streamlit/issues/6490), [#6498](https://github.com/streamlit/streamlit/pull/6498)).

## **Version 1.21.0**

_Release date: April 6, 2023_

**Highlights**

- ≡ƒôÅ Introducing `st.divider` ΓÇö a command that displays a horizontal line in your app. Learn how to use this command in its [API reference](/develop/api-reference/text/st.divider).
- ≡ƒöÅ Streamlit now supports the use of a global `secrets.toml` file, in addition to a project-level file, to easily store and securely access your secrets. Learn more in [Secrets management](/develop/concepts/connections/secrets-management).
- ≡ƒÜÇ [st.help](/develop/api-reference/utilities/st.help) has been revamped to show more information about object methods, attributes, classes, and more, which is great for debugging ([#5857](https://github.com/streamlit/streamlit/pull/5857), [#6382](https://github.com/streamlit/streamlit/pull/6382))!

**Notable Changes**

- ≡ƒ¬£ [st.time_input](/develop/api-reference/widgets/st.time_input) supports adding a stepping interval with the keyword-only `step` parameter ([#6071](https://github.com/streamlit/streamlit/pull/6071)).
- Γ¥ô Most [text elements](/develop/api-reference/text) can include tooltips with the `help` parameter ([#6043](https://github.com/streamlit/streamlit/pull/6043)).
- Γåö∩╕Å [st.pyplot](/develop/api-reference/charts/st.pyplot) has a `use_container_width` parameter to set the chart to the container width (now all [chart elements](/develop/api-reference/charts) support this parameter) ([#6067](https://github.com/streamlit/streamlit/pull/6067)).
- ≡ƒæ⌐ΓÇì≡ƒÆ╗ [st.code](/develop/api-reference/text/st.code) supports optionally displaying line numbers to the code block's left with the boolean `line_numbers` parameter ([#5756](https://github.com/streamlit/streamlit/issues/5756), [#6042](https://github.com/streamlit/streamlit/pull/6042)).
- ΓÜô Anchors in header elements can be turned off by setting `anchor=False` ([#6158](https://github.com/streamlit/streamlit/pull/6158)).

**Other Changes**

- ≡ƒÉ╝┬á[st.table](/develop/api-reference/data/st.table) and [st.dataframe](/develop/api-reference/data/st.dataframe) support `pandas.Period`, and number and boolean types in categorical columns ([#2547](https://github.com/streamlit/streamlit/issues/2547), [#5429](https://github.com/streamlit/streamlit/pull/5429), [#5329](https://github.com/streamlit/streamlit/issues/5392), [#6248](https://github.com/streamlit/streamlit/pull/6248)).
- ≡ƒò╕∩╕Å┬áAdded `.webp` to the list of allowed static file extensions ([#6331](https://github.com/streamlit/streamlit/pull/6331))
- ≡ƒÉ₧┬áBug fix: stop script execution on websocket close to immediately clear session information ([#6166](https://github.com/streamlit/streamlit/issues/6166), [#6204](https://github.com/streamlit/streamlit/pull/6204)).
- ≡ƒÉ£┬áBug fixes: updated allowed/disallowed label markdown behavior such that unsupported elements are unwrapped and only their children (text contents) render ([#5872](https://github.com/streamlit/streamlit/issues/5872), [#6036](https://github.com/streamlit/streamlit/issues/6036), [#6054](https://github.com/streamlit/streamlit/issues/6054), [#6163](https://github.com/streamlit/streamlit/pull/6163)).
- ≡ƒ¬▓┬áBug fixes: don't push browser history states on rerun, use HTTPS to load external resources in `streamlit hello`, and make the browser back button work for multipage apps ([#5292](https://github.com/streamlit/streamlit/issues/5292), [#6266](https://github.com/streamlit/streamlit/pull/6266), [#6232](https://github.com/streamlit/streamlit/pull/6232)). Thanks, [whitphx](https://github.com/whitphx)!
- ≡ƒÉ¥┬áBug fix: avoid showing emoji on non-UTF-8 terminals. ([#2284](https://github.com/streamlit/streamlit/issues/2284), [#6088](https://github.com/streamlit/streamlit/pull/6088)). Thanks, [kcarnold](https://github.com/kcarnold)!
- ≡ƒôü┬áBug fix: override default use of┬á[File System Access API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API) for┬á`react-dropzone` so that `st.file_uploader`'s File Selection Dialog only shows file types corresponding to those included in the `type` parameter ([#6176](https://github.com/streamlit/streamlit/issues/6176), [#6315](https://github.com/streamlit/streamlit/pull/6315)).
- ≡ƒÆ╛┬áBug fix: make the `.clear()` method on cache-decorated functions work ([#6310](https://github.com/streamlit/streamlit/issues/6310), [#6321](https://github.com/streamlit/streamlit/pull/6321)).
- ≡ƒÅâ┬áBug fix: `st.experimental_get_query_params` doesn't need reruns to work ([#6347](https://github.com/streamlit/streamlit/issues/6347), [#6348](https://github.com/streamlit/streamlit/pull/6348)). Thanks, [PaleNeutron](https://github.com/PaleNeutron)!
- ≡ƒÉ¢┬áBug fix: `CachedStFunctionWarning` mentions `experimental_allow_widgets` instead of the deprecated `suppress_st_warning` ([#6216](https://github.com/streamlit/streamlit/issues/6216), [#6217](https://github.com/streamlit/streamlit/pull/6217)).

## **Version 1.20.0**

_Release date: March 09, 2023_

**Notable Changes**

- ≡ƒöÉ┬áAdded support for configuring SSL to┬á[serve apps directly over HTTPS](/develop/concepts/configuration/https-support)┬á([#5969](https://github.com/streamlit/streamlit/pull/5969)).
- ≡ƒû╝∩╕Å┬áGranular control over app embedding behavior with the `/?embed` and `/?embed_options` query parameters. Learn how to use this feature in our [docs](/deploy/streamlit-community-cloud/share-your-app/embed-your-app) ([#6011](https://github.com/streamlit/streamlit/pull/6011), [#6019](https://github.com/streamlit/streamlit/pull/6019)).
- ΓÜí┬áEnabled the `runner.fastReruns` [configuration option](/develop/concepts/configuration#view-all-configuration-options) by default to make apps much more responsive to user interaction ([#6200](https://github.com/streamlit/streamlit/pull/6200)).

**Other Changes**

- ≡ƒìö┬áCleaned up the hamburger menu by removing the least used options ([#6080](https://github.com/streamlit/streamlit/pull/6080)).
- ≡ƒû¿∩╕Å┬áDesign changes to ensure apps being printed or saved as a PDF look good ([#6180](https://github.com/streamlit/streamlit/pull/6180)).
- ≡ƒÉ₧┬áBug fix: improved `dtypes` checking in `st.experimental_data_editor` ([#6185](https://github.com/streamlit/streamlit/issues/6185), [#6188](https://github.com/streamlit/streamlit/pull/6188)).
- ≡ƒÉ¢┬áBug fix: properly position `st.metric`'s `help` tooltip when not inside columns ([#6168](https://github.com/streamlit/streamlit/pull/6168)).
- ≡ƒ¬▓┬áBug fix: regression in retrieving messages from the server's `ForwardMsgCache` ([#6210](https://github.com/streamlit/streamlit/pull/6210)).
- ≡ƒîÇ┬áBug fix: `st.cache_data` docstring for the `show_spinner` param now lists `str` as a supported type ([#6207](https://github.com/streamlit/streamlit/issues/6207), [#6213](https://github.com/streamlit/streamlit/pull/6213)).
- ΓÅ▒∩╕Å┬áMade ping and websocket timeouts far more forgiving ([#6212](https://github.com/streamlit/streamlit/pull/6212)).
- ≡ƒù║∩╕Å┬á`st.map` and `st.pydeck_chart` docs state that Streamlit's Mapbox token will not work indefinitely ([#6143](https://github.com/streamlit/streamlit/pull/6143)).

## **Version 1.19.0**

_Release date: February 23, 2023_

**Highlights**

- Γ£é∩╕Å┬áIntroducing `st.experimental_data_editor`, a widget that allows you to edit DataFrames and many other data structures in a table-like UI. Read more in our [documentation](/develop/concepts/design/dataframes) and [blog post](https://blog.streamlit.io/editable-dataframes-are-here/).

**Other Changes**

- Γ£¿ Streamlit's GitHub README got a new look ([#6016](https://github.com/streamlit/streamlit/pull/6016)).
- ≡ƒîÜ┬áImproved readability of styled dataframe cells in dark mode ([#6060](https://github.com/streamlit/streamlit/issues/6060), [#6098](https://github.com/streamlit/streamlit/pull/6098)).
- ≡ƒÉ¢┬áBug fix: make apps work again in the latest versions of Safari, and in Chrome with third-party cookies blocked ([#6092](https://github.com/streamlit/streamlit/issues/6092), [#6094](https://github.com/streamlit/streamlit/pull/6094), [#6087](https://github.com/streamlit/streamlit/issues/6087), [#6100](https://github.com/streamlit/streamlit/pull/6100)).
- ≡ƒÉ₧┬áBug fix: refer to new cache primitives in the "Clear cache" dialog and error messages ([#6082](https://github.com/streamlit/streamlit/pull/6082), [#6128](https://github.com/streamlit/streamlit/pull/6128)).
- ≡ƒÉ¥┬áBug fix: properly cache class member functions and instance methods ([#6109](https://github.com/streamlit/streamlit/issues/6109), [#6114](https://github.com/streamlit/streamlit/pull/6114)).
- ≡ƒÉ£┬áBug fix: regression in `st.metric` tooltip position ([#6093](https://github.com/streamlit/streamlit/issues/6093), [#6129](https://github.com/streamlit/streamlit/pull/6129)).
- ≡ƒ¬▓┬áBug fix: allow fullscreen button to show for dataframes, charts, etc, in expander ([#6083](https://github.com/streamlit/streamlit/pull/6083), [#6148](https://github.com/streamlit/streamlit/pull/6148)).

## **Version 1.18.0**

_Release date: February 09, 2023_

**Highlights**

- ≡ƒÄè┬áIntroducing┬á`@st.cache_data`┬áand┬á`@st.cache_resource`┬áΓÇö two new caching commands to replace┬á`st.cache`! Check out our┬á[blog post](https://blog.streamlit.io/p/c0a90231-9848-47ec-a40c-ad4a344e4de1/)┬áand┬á[documentation](/develop/concepts/architecture/caching)┬áfor more information.

**Notable Changes**

- ≡ƒ¬å┬á`st.columns` supports up to one level of column nesting (i.e., columns inside columns) in the main area of the app.
- ΓÅ│┬á`st.progress` supports adding a message to display above the progress bar with the `text` keyword parameter.
- Γåö∩╕Å `st.button` has an optional┬á`use_container_width`┬áparameter to allow you to stretch buttons across the full container width.
- ≡ƒÉì We formally added support for Python 3.11.
- ≡ƒû¿∩╕Å┬áSave your app as a PDF via the "Print" option in your app's hamburger menu.
- ≡ƒ¢Ä∩╕Å┬áApps can serve small, static media files via the `enableStaticServing` config option. See our [documentation](/develop/concepts/configuration/serving-static-files) on how to use this feature and our demo [app](https://static-file-serving.streamlit.app/) for an example.

**Other Changes**

- ≡ƒÅü┬áAll Streamlit endpoints (including `/healthz`) have been renamed to have a consistent pattern and avoid any clashes with reserved endpoints of GCP (notably Cloud Run and App Engine) ([#5534](https://github.com/streamlit/streamlit/pull/5534)).
- ΓÜí┬áImproved caching performance when multiple sessions access an uncomputed cached value simultaneously ([#6017](https://github.com/streamlit/streamlit/pull/6017)).
- ≡ƒÜº┬áStreamlit only displays deprecation warnings in the browser when the `client.showErrorDetails` config option is set to `True`. Deprecation warnings always get logged to the console, regardless of whether they're displayed in-browser ([#5945](https://github.com/streamlit/streamlit/pull/5945)).
- ≡ƒÅô┬áRefactored the `st.dataframe` internals to improve dataframe handling and conversion, such as detecting more types, converting key-value dicts to dataframes, and more ([#6026](https://github.com/streamlit/streamlit/pull/6026), [#6023](https://github.com/streamlit/streamlit/pull/6023)).
- ≡ƒÆ╜ The behavior of widget labels when they are passed unsupported Markdown elements is documented ([#5978](https://github.com/streamlit/streamlit/pull/5978)).
- ≡ƒôè┬áBug fix: Plotly improvements ΓÇö upgraded multiple frontend dependencies, including Plotly, to the latest version to properly redraw cached charts, make Plotly mapbox animations work, and allow users to update the figure layout when using the Streamlit theme ([#5885](https://github.com/streamlit/streamlit/pull/5885), [#5967](https://github.com/streamlit/streamlit/pull/5967), [#6055](https://github.com/streamlit/streamlit/pull/6055)).
- ≡ƒô╢┬áBug fix: allow browser tabs that transiently disconnect (due to a network blip, load balancer timeout, etc.) to avoid losing all of their state ([#5856](https://github.com/streamlit/streamlit/pull/5856)).
- ≡ƒô▒ Bug fix: the keyboard is hidden on mobile when `st.selectbox` and `st.multiselect` have less than 10 options ([#5979](https://github.com/streamlit/streamlit/pull/5979)).
- ≡ƒÉ¥┬áBug fix: design tweaks to `st.metric`, `st.multiselect`, `st.tabs` , and menu items to prevent label overflow and scrolling issues, especially with small viewport sizes ([#5933](https://github.com/streamlit/streamlit/pull/5933), [#6034](https://github.com/streamlit/streamlit/pull/6034)).
- ≡ƒÉ₧┬áBug fix: switched to a functioning Twemoji URL from which page favicons are loaded in `st.set_page_config` ([#5943](https://github.com/streamlit/streamlit/pull/5943)).
- Γ£ì∩╕Å More type hints ([#5986](https://github.com/streamlit/streamlit/pull/5986)). Thanks, [harahu](https://github.com/harahu)!

## **Version 1.17.0**

_Release date: January 12, 2023_

**Notable Changes**

- ≡ƒ¬ä┬á[`@st.experimental_singleton`](/develop/api-reference/caching-and-state/st.experimental_singleton#validating-the-cache) supports an optional `validate` parameter that accepts a validation function for cached data and is called each time the cached value is accessed.
- ≡ƒÆ╛┬á [`@st.experimental_memo`](/develop/api-reference/caching-and-state/st.experimental_memo)'s `persist` parameter can also accept booleans.

**Other Changes**

- ≡ƒôƒ┬áMultipage apps exclude `__init__.py` from the page selector ([#5890](https://github.com/streamlit/streamlit/pull/5890)).
- ≡ƒôÉ┬áThe iframes of embedded apps have the ability to dynamically resize their height ([#5894](https://github.com/streamlit/streamlit/pull/5894)).
- ≡ƒÉ₧┬áBug fix: thumb values of range sliders respect the container width ([#5913](https://github.com/streamlit/streamlit/pull/5913)).
- ≡ƒ¬▓┬áBug fix: all examples in docstrings of Streamlit commands contain relevant imports to make them reproducible ([#5877](https://github.com/streamlit/streamlit/pull/5877)).

## **Version 1.16.0**

_Release date: December 14, 2022_

**Highlights**

- ≡ƒæ⌐ΓÇì≡ƒÄ¿┬áIntroducing a new Streamlit theme for Altair, Plotly, and Vega-Lite charts! Check out our [blog post](https://blog.streamlit.io/a-new-streamlit-theme-for-altair-and-plotly/) for more information.
- ≡ƒÄ¿┬áStreamlit now supports colored text in all commands that accept Markdown, including `st.markdown`, `st.header`, and more. Learn more in our [documentation](/develop/api-reference/text/st.markdown).

**Notable Changes**

- ≡ƒöü┬áFunctions cached with `st.experimental_memo` or `st.experimental_singleton` can contain Streamlit media elements and forms.
- Γ¢ä┬áAll Streamlit commands that accept pandas DataFrames as input also support Snowpark and PySpark DataFrames.
- ≡ƒÅ╖┬á[st.checkbox](/develop/api-reference/widgets/st.checkbox) and [st.metric](/develop/api-reference/data/st.metric) can customize how to hide their labels with the `label_visibility` parameter.

**Other Changes**

- ≡ƒù║∩╕Å┬á`st.map` improvements: support for upper case columns and better exception messages ([#5679](https://github.com/streamlit/streamlit/pull/5679), [#5792](https://github.com/streamlit/streamlit/pull/5792)).
- ≡ƒÉ₧┬áBug fix: `st.plotly_chart` respects the figure's height attribute and the `use_container_width` parameter ([#5779](https://github.com/streamlit/streamlit/pull/5779)).
- ≡ƒ¬▓┬áBug fix: all commands with the `icon` parameter such as [st.error](/develop/api-reference/status/st.error), [st.warning](/develop/api-reference/status/st.warning), etc, can contain emojis with variant selectors ([#5583](https://github.com/streamlit/streamlit/pull/5583)).
- ≡ƒÉ¥┬áBug fix: prevent `st.camera_input` from jittering when resizing the browser window ([#5661](https://github.com/streamlit/streamlit/pull/5711)).
- ≡ƒÉ£┬áBug fix: update exception layout to avoid overflow of stack traces ([#5700](https://github.com/streamlit/streamlit/pull/5700)).

## **Version 1.15.0**

_Release date: November 17, 2022_

**Notable Changes**

- ≡ƒÆà┬áWidget labels can contain inline Markdown. See our [docs](/develop/api-reference/widgets) and demo [app](https://markdown-labels.streamlit.app/) for more info.
- ≡ƒÄ╡ [`st.audio`](/develop/api-reference/media/st.audio) now supports playing audio data passed in as NumPy arrays with the keyword-only `sample_rate` parameter.
- ≡ƒöü┬áFunctions cached with `st.experimental_memo` or `st.experimental_singleton` can contain Streamlit widgets using the `experimental_allow_widgets` parameter. This allows caching checkboxes, sliders, radio buttons, and more!

**Other Changes**

- ≡ƒæ⌐ΓÇì≡ƒÄ¿┬áDesign tweak to prevent jittering in sliders ([#5612](https://github.com/streamlit/streamlit/pull/5612)).
- ≡ƒÉ¢┬áBug fix: links in headers are red, not blue ([#5609](https://github.com/streamlit/streamlit/pull/5609)).
- ≡ƒÉ₧┬áBug fix: properly resize Plotly charts when exiting fullscreen ([#5645](https://github.com/streamlit/streamlit/pull/5645)).
- ≡ƒÉ¥: Bug fix: don't accidentally trigger `st.balloons` and `st.snow` ([#5401](https://github.com/streamlit/streamlit/pull/5401)).

## **Version 1.14.0**

_Release date: October 27, 2022_

**Highlights**

- ≡ƒÄ¿┬á`st.button` and `st.form_submit_button` support designating buttons as "primary" (for additional emphasis) or "secondary" (for normal buttons) with the `type` keyword-only parameter.

**Notable Changes**

- ≡ƒñÅ┬á`st.multiselect` has a keyword-only `max_selections` parameter to limit the number of options that can be selected at a time.
- ≡ƒôä┬á`st.form_submit_button` now has the `disabled` parameter that removes interactivity.

**Other Changes**

- ≡ƒÅô┬á`st.dataframe` and `st.table` accept categorical intervals as input ([#5395](https://github.com/streamlit/streamlit/pull/5395)).
- ΓÜí┬áPerformance improvements to Plotly charts ([#5542](https://github.com/streamlit/streamlit/pull/5542)).
- ≡ƒ¬▓┬áBug fix: `st.download_button` supports non-latin1 characters in filenames ([#5465](https://github.com/streamlit/streamlit/pull/5465)).
- ≡ƒÉ₧┬áBug fix: Allow `st.image` to render a local GIF as a GIF, not as a static PNG ([#5438](https://github.com/streamlit/streamlit/pull/5438)).
- ≡ƒô▒┬áDesign tweaks to the sidebar in multipage apps ([#5538](https://github.com/streamlit/streamlit/pull/5538), [#5445](https://github.com/streamlit/streamlit/pull/5445), [#5559](https://github.com/streamlit/streamlit/pull/5559)).
- ≡ƒôè┬áImprovements to the axis configuration for built-in charts ([#5412](https://github.com/streamlit/streamlit/pull/5412)).
- ≡ƒöº┬áMemo and singleton improvements: support text values for `show_spinner`, use `datetime.timedelta` objects as `ttl` parameter value, properly hash PIL images and `Enum` classes, show better error messages when returning unevaluated dataframes ([#5447](https://github.com/streamlit/streamlit/pull/5447), [#5413](https://github.com/streamlit/streamlit/pull/5413), [#5504](https://github.com/streamlit/streamlit/pull/5504), [#5426](https://github.com/streamlit/streamlit/pull/5426), [#5515](https://github.com/streamlit/streamlit/pull/5515)).
- ≡ƒöì┬áZoom buttons in maps created with `st.map` and `st.pydeck_chart` use light or dark style based on the app's theme ([#5479](https://github.com/streamlit/streamlit/pull/5479)).
- ≡ƒù£┬áWebsocket headers from the current session's incoming WebSocket request can be obtained from a new "internal" (i.e.: subject to change without deprecation) API ([#5457](https://github.com/streamlit/streamlit/pull/5457)).
- ≡ƒô¥┬áImprove the text that gets printed when you first install and use Streamlit ([#5473](https://github.com/streamlit/streamlit/pull/5473)).

## **Version 1.13.0**

_Release date: September 22, 2022_

**Notable Changes**

- ≡ƒÅ╖┬áWidgets can customize how to hide their labels with the `label_visibility` parameter.
- ≡ƒöì `st.map` adds zoom buttons to the map by default.
- Γåö∩╕Å┬á`st.dataframe`┬ásupports the┬á`use_container_width`┬áparameter to stretch across the full container width.
- ≡ƒ¬ä Improvements to┬á`st.dataframe`┬ásizing: Column width calculation respects column headers, supports double click between column headers to autosize, better fullscreen support, and fixes the issue with the┬á`width`┬áparameter.

**Other Changes**

- Γî¿∩╕Å `st.time_input` allows for keyboard-only input ([#5194](https://github.com/streamlit/streamlit/pull/5194)).
- ≡ƒÆ┐ `st.memo` will warn the user when using┬á`ttl`┬áand┬á`persist`┬ákeyword argument together ([#5032](https://github.com/streamlit/streamlit/pull/5032)).
- ≡ƒöó┬á`st.number_input` returns consistent type after rerun ([#5359](https://github.com/streamlit/streamlit/pull/5359)).
- ≡ƒÜÆ┬á`st.sidebar` UI fixes including a fix for scrollbars in Firefox browsers ([#5157](https://github.com/streamlit/streamlit/pull/5157), [#5324](https://github.com/streamlit/streamlit/pull/5324)).
- ≡ƒæ⌐ΓÇì≡ƒÆ╗┬áImprovements to usage metrics to guide API development.
- Γ£ì∩╕Å┬áMore type hints! ([#5191](https://github.com/streamlit/streamlit/pull/5191), [#5192](https://github.com/streamlit/streamlit/pull/5192), [#5242](https://github.com/streamlit/streamlit/pull/5242), [#5243](https://github.com/streamlit/streamlit/pull/5243), [#5244](https://github.com/streamlit/streamlit/pull/5244), [#5245](https://github.com/streamlit/streamlit/pull/5245), [#5246](https://github.com/streamlit/streamlit/pull/5246)) Thanks [harahu](https://github.com/harahu)!

## **Version 1.12.0**

_Release date: August 11, 2022_

**Highlights**

- ≡ƒôè┬áBuilt-in charts (e.g. `st.line_chart`) get a brand-new look and parameters `x` and `y`! Check out our [blog post](https://blog.streamlit.io/built-in-charts-get-a-new-look-and-parameters/) for more information.

**Notable Changes**

- ΓÅ»┬áFunctions cached with `st.experimental_memo` or `st.experimental_singleton` can now contain static `st` commands. This allows caching text, charts, dataframes, and more!
- Γåö∩╕Å┬áThe sidebar is now resizable via drag and drop.
- ΓÿÄ∩╕Å┬á`st.info`, `st.success`, `st.error`, and `st.warning` got a redesign and have a new keyword-only parameter: `icon`.

**Other Changes**

- ≡ƒÄÜ∩╕Å┬á`st.select_slider` correctly handles all floats now ([#4973](https://github.com/streamlit/streamlit/pull/4973), [#4978](https://github.com/streamlit/streamlit/pull/4978)).
- ≡ƒöó┬á`st.multi_select` can take values from enums ([#4987](https://github.com/streamlit/streamlit/pull/4987)).
- ≡ƒìè┬á`st.slider` range values can now be set through `st.session_state` ([#5007](https://github.com/streamlit/streamlit/pull/5007)).
- ≡ƒÄ¿┬á`st.progress` got a redesign ([#5011](https://github.com/streamlit/streamlit/pull/5011), [#5086](https://github.com/streamlit/streamlit/pull/5086)).
- ≡ƒöÿ┬á`st.radio` better deals with list-like dataframes ([#5021](https://github.com/streamlit/streamlit/pull/5021)).
- ≡ƒº₧ΓÇìΓÖé∩╕Å┬á`st.cache` properly handles JSON files now ([#5023](https://github.com/streamlit/streamlit/pull/5023)).
- ΓÜô∩╕Å Headers render markdown now when the `anchor` parameter is set ([#5038](https://github.com/streamlit/streamlit/pull/5038)).
- ≡ƒù╗┬á`st.image` can now load SVGs from Inkscape ([#5040](https://github.com/streamlit/streamlit/pull/5040)).
- ≡ƒù║∩╕Å┬á`st.map` and `st.pydeck_chart` use light or dark style based on the app's theme ([#5074](https://github.com/streamlit/streamlit/pull/5074), [#5108](https://github.com/streamlit/streamlit/pull/5108)).
- ≡ƒÄê┬áClicks on elements below┬á`st.balloons` and `st.snow` don't get blocked anymore ([#5098](https://github.com/streamlit/streamlit/pull/5098)).
- ≡ƒö¥┬áEmbedded apps have lower top padding ([#5111](https://github.com/streamlit/streamlit/pull/5111)).
- ≡ƒÆà┬áAdjusted padding and alignment for widgets, charts, and dataframes ([#4995](https://github.com/streamlit/streamlit/pull/4995), [#5061](https://github.com/streamlit/streamlit/pull/5061), [#5081](https://github.com/streamlit/streamlit/pull/5081)).
- Γ£ì∩╕Å┬áMore type hints! ([#4926](https://github.com/streamlit/streamlit/pull/4926), [#4932](https://github.com/streamlit/streamlit/pull/4932), [#4933](https://github.com/streamlit/streamlit/pull/4933))

## **Version 1.11.0**

_Release date: July 14, 2022_

**Highlights**

- ≡ƒùé┬áIntroducing `st.tabs` to have tab containers in your app. See our [documentation](/develop/api-reference/layout/st.tabs) on how to use this feature.

**Notable Changes**

- Γä╣∩╕Å┬á`st.metric` supports tooltips with the `help` keyword parameter.
- ≡ƒÜç┬á`st.columns` supports setting the gap size between columns with the `gap` keyword parameter.

**Other Changes**

- ≡ƒÆà┬áDesign tweaks to `st.selectbox`, `st.expander`, `st.spinner` ([#4801](https://github.com/streamlit/streamlit/pull/4801)).
- ≡ƒô▒┬áThe sidebar will close when users select a page from the navigation menu on mobile devices ([#4851](https://github.com/streamlit/streamlit/pull/4841)).
- ≡ƒºá┬á`st.memo` supports dataclasses! ([#4850](https://github.com/streamlit/streamlit/pull/4850))
- ≡ƒÅÄ┬áBug fix for a race condition that destroyed widget state with rapid interaction ([#4882](https://github.com/streamlit/streamlit/pull/4882)).
- ≡ƒÅô┬á`st.table` presents overflowing content to be scrollable when placed inside columns and expanders ([#4934](https://github.com/streamlit/streamlit/pull/4934)).
- ≡ƒÉì┬áTypes: More updated type annotations across Streamlit! ([#4808](https://github.com/streamlit/streamlit/pull/4808), [#4809](https://github.com/streamlit/streamlit/pull/4809), [#4856](https://github.com/streamlit/streamlit/pull/4856))

## **Version 1.10.0**

_Release date: June 2, 2022_

**Highlights**

- ≡ƒôû Introducing native support for multipage apps! Check out our [blog post](https://blog.streamlit.io/introducing-multipage-apps) and try out our new `streamlit hello`.

**Notable Changes**

- Γ£¿ `st.dataframe` has been redesigned.
- ≡ƒöÿ `st.radio` has a `horizontal` keyword-only parameter to display options horizontally.
- ΓÜá∩╕Å Streamlit Community Cloud will support richer exception formatting.
- ≡ƒÅé Get user information on private apps using `st.experimental_user`.

**Other Changes**

- ≡ƒôè Upgraded Vega-Lite library to support even more interactive charting improvements. See their [release notes](https://github.com/vega/vega-lite/releases) to find out more. ([#4751](https://github.com/streamlit/streamlit/pull/4751)).
- ≡ƒôê `st.vega_lite_chart` will respond to updates, particularly in response to input widgets ([#4736](https://github.com/streamlit/streamlit/pull/4736)).
- ≡ƒÆ¼ `st.markdown` with long text will always wrap ([#4696](https://github.com/streamlit/streamlit/pull/4696)).
- ≡ƒôª Support for [PDM](https://pdm.fming.dev/) ([#4724](https://github.com/streamlit/streamlit/pull/4724)).
- Γ£ì∩╕Å Types: Updated type annotations across Streamlit! ([#4679](https://github.com/streamlit/streamlit/pull/4679), [#4680](https://github.com/streamlit/streamlit/pull/4680), [#4681](https://github.com/streamlit/streamlit/pull/4681), [#4682](https://github.com/streamlit/streamlit/pull/4682), [#4683](https://github.com/streamlit/streamlit/pull/4683), [#4684](https://github.com/streamlit/streamlit/pull/4684), [#4685](https://github.com/streamlit/streamlit/pull/4685), [#4686](https://github.com/streamlit/streamlit/pull/4686), [#4687](https://github.com/streamlit/streamlit/pull/4687), [#4688](https://github.com/streamlit/streamlit/pull/4688), [#4690](https://github.com/streamlit/streamlit/pull/4690), [#4703](https://github.com/streamlit/streamlit/pull/4703), [#4704](https://github.com/streamlit/streamlit/pull/4704), [#4705](https://github.com/streamlit/streamlit/pull/4705), [#4706](https://github.com/streamlit/streamlit/pull/4706), [#4707](https://github.com/streamlit/streamlit/pull/4707), [#4708](https://github.com/streamlit/streamlit/pull/4708), [#4710](https://github.com/streamlit/streamlit/pull/4710), [#4723](https://github.com/streamlit/streamlit/pull/4723), [#4733](https://github.com/streamlit/streamlit/pull/4733)).

## **Version 1.9.0**

_Release date: May 4, 2022_

**Notable Changes**

- ≡ƒ¬ù `st.json` now supports a keyword-only argument, `expanded` on whether the JSON should be expanded by default (defaults to `True`).
- ≡ƒÅâΓÇìΓÖÇ∩╕Å More performance improvements from reducing redundant work each script run.

**Other Changes**

- ≡ƒÅç Widgets when `disabled` is set/unset will maintain its value ([#4527](https://github.com/streamlit/streamlit/pull/4527)).
- ≡ƒº¬ Experimental feature to increase the speed of reruns using configuration `runner.fastReruns`. See [#4628](https://github.com/streamlit/streamlit/pull/4628) for the known issues in enabling this feature.
- ≡ƒù║∩╕Å DataFrame timestamps support UTC offset (in addition to time zone notation) ([#4669](https://github.com/streamlit/streamlit/pull/4669)).

## **Version 1.8.0**

_Release date: March 24, 2022_

**Notable Changes**

- ≡ƒÅâΓÇìΓÖÇ∩╕Å┬áDataframes should see performance improvements ([#4463](https://github.com/streamlit/streamlit/pull/4463)).

**Other Changes**

- ≡ƒò░┬á`st.slider` handles timezones better by removing timezone conversions on the backend ([#4348](https://github.com/streamlit/streamlit/pull/4358)).
- ≡ƒæ⌐ΓÇì≡ƒÄ¿┬áDesign improvements to our header ([#4496](https://github.com/streamlit/streamlit/pull/4496)).

## **Version 1.7.0**

_Release date: March 3, 2022_

**Highlights**

- Introducing `st.snow`, celebrating our acquisition by Snowflake! See more information in [our blog post](https://blog.streamlit.io/snowflake-to-acquire-streamlit/).

## **Version 1.6.0**

_Release date: Feb 24, 2022_

**Other Changes**

- ≡ƒù£┬áWebSocket compression is now disabled by default, which will improve CPU and latency performance for large dataframes. You can use the┬á`server.enableWebsocketCompression` configuration option to re-enable it if you find the increased network traffic more impactful.
- Γÿæ∩╕Å┬á≡ƒöÿ┬áRadio and checkboxes improve focus on Keyboard navigation ([#4308](https://github.com/streamlit/streamlit/pull/4308)).

## **Version 1.5.0**

_Release date: Jan 27, 2022_

**Notable Changes**

- ≡ƒîƒ Favicon defaults to a PNG to allow for transparency ([#4272](https://github.com/streamlit/streamlit/pull/4272)).
- ≡ƒÜª Select Slider Widget now has the `disabled` parameter that removes interactivity (completing all of our widgets) ([#4314](https://github.com/streamlit/streamlit/pull/4314)).

**Other Changes**

- ≡ƒöñ Improvements to our markdown library to provide better support for HTML (specifically nested HTML) ([#4221](https://github.com/streamlit/streamlit/pull/4221)).
- ≡ƒôû Expanders maintain their expanded state better when multiple expanders are present ([#4290](https://github.com/streamlit/streamlit/pull/4290)).
- ≡ƒù│ Improved file uploader and camera input to call its `on_change` handler only when necessary ([#4270](https://github.com/streamlit/streamlit/pull/4270)).

## **Version 1.4.0**

_Release date: Jan 13, 2022_

**Highlights**

- ≡ƒô╕ Introducing `st.camera_input` for uploading images straight from your camera.

**Notable Changes**

- ≡ƒÜª Widgets now have the `disabled` parameter that removes interactivity.
- ≡ƒÜ« Clear `st.experimental_memo` and `st.experimental_singleton` programmatically by using the `clear()` method on a cached function.
- ≡ƒô¿ Developers can now configure the maximum size of a message to accommodate larger messages within the Streamlit application. See `server.maxMessageSize`.
- ≡ƒÉì We formally added support for Python 3.10.

**Other Changes**

- ≡ƒÿ╡ΓÇì≡ƒÆ½ Calling `str` or `repr` on `threading.current_thread()` does not cause a RecursionError ([#4172](https://github.com/streamlit/streamlit/issues/4172)).
- ≡ƒô╣ Gracefully stop screencast recording when user removes permission to record ([#4180](https://github.com/streamlit/streamlit/pull/4180)).
- ≡ƒîç Better scale images by using a higher-quality image bilinear resampling algorithm ([#4159](https://github.com/streamlit/streamlit/pull/4159)).

## Version 1.3.0

_Release date: Dec 16, 2021_

**Notable Changes**

- ≡ƒÆ» Support for NumPy values in `st.metric`.
- ≡ƒîÉ Support for Mesh Layers in PyDeck.
- ≡ƒôè Updated Plotly chart version to support the latest features.
- ≡ƒÅÇ `st.spinner` element has visual animated spinner.
- ≡ƒì░ `st.caption` supports HTML in text with `unsafe_allow_html` parameter.

**Other Changes**

- ≡ƒ¬▓ Bug fix: Allow `st.session_state` to be used to set number_input values with no warning ([#4047](https://github.com/streamlit/streamlit/pull/4047)).
- ≡ƒ¬▓ Bug fix: Fix footer alignment in wide mode ([#4035](https://github.com/streamlit/streamlit/pull/4035)).
- ≡ƒÉ₧ Bug fix: Better support for Graphviz and Bokeh charts in containers (columns, expanders, etc.) ([#4039](https://github.com/streamlit/streamlit/pull/4039)).
- ≡ƒÉ₧ Bug fix: Support inline data values in Vega-Lite ([#4070](https://github.com/streamlit/streamlit/pull/4070)).
- Γ£ì∩╕Å Types: Updated type annotations for experimental memo and singleton decorators.
- Γ£ì∩╕Å Types: Improved type annotations for `st.selectbox`, `st.select_slider`, `st.radio`, `st.number_input`, and `st.multiselect`.

## Version 1.2.0

_Release date: Nov 11, 2021_

**Notable Changes**

- Γ£Å∩╕Å┬á`st.text_input`┬áand `st.text_area` now have a┬á`placeholder`┬áparameter to display text when the field is empty.
- ≡ƒôÅ Viewers can now resize the input box in `st.text_area`.
- ≡ƒôü Streamlit can auto-reload when files in sub-directories change.
- ≡ƒîê We've upgraded Bokeh support to 2.4.1! We recommend updating your Bokeh library to 2.4.1 to maintain functionality. Going forward, we'll let you know if there's a mismatch in your Bokeh version via an error prompt.
- ≡ƒöÆ Developers can access secrets via attribute notation (e.g. `st.secrets.key` vs `st.secrets["key"]`) just like session state.
- Γ£ì∩╕Å Publish type annotations according to [PEP 561](https://mypy.readthedocs.io/en/stable/installed_packages.html). Users now get type annotations for Streamlit when running mypy ([#4025](https://github.com/streamlit/streamlit/pull/4025)).

**Other Changes**

- ≡ƒæÇ Visual fixes ([#3863](https://github.com/streamlit/streamlit/pull/3863), [#3995](https://github.com/streamlit/streamlit/pull/3995), [#3926](https://github.com/streamlit/streamlit/pull/3926), [#3975](https://github.com/streamlit/streamlit/pull/3975)).
- ≡ƒìö Fixes to the hamburger menu ([#3968](https://github.com/streamlit/streamlit/pull/3968)).
- ≡ƒû¿∩╕Å Ability to print session state ([#3970](https://github.com/streamlit/streamlit/pull/3970)).

## Version 1.1.0

_Release date: Oct 21, 2021_

**Highlights**

- ≡ƒºá Memory improvements: Streamlit apps allocate way less memory over time now.

**Notable Changes**

- ΓÖ╗∩╕Å Apps automatically rerun now when the content of `secrets.toml` changes (before this you had to refresh the page manually).

**Other Changes**

- ≡ƒöù Redirected some links to our [brand-new docs site](https://docs.streamlit.io/), e.g. in exceptions.
- ≡ƒ¬▓ Bug fix: Allow initialization of range slider with session state ([#3586](https://github.com/streamlit/streamlit/issues/3586)).
- ≡ƒÉ₧ Bug fix: Refresh chart when using `add_rows` with `datetime` index ([#3653](https://github.com/streamlit/streamlit/issues/3653)).
- Γ£ì∩╕Å Added some more type annotation in our codebase ([#3908](https://github.com/streamlit/streamlit/issues/3908)).

## Version 1.0.0

_Release date: Oct 5, 2021_

**Highlights**

- ≡ƒÄêAnnouncing Streamlit 1.0! To read more about check out our [1.0 blog post](https://blog.streamlit.io/announcing-streamlit-1-0/).

**Other Changes**

- ≡ƒÉ₧ Fixed an issue where using `df.dtypes` to show datatypes for a DF fails while using Arrow ([#3709](https://github.com/streamlit/streamlit/issues/3709)), Image captions stay within image width and are readable ([#3530](https://github.com/streamlit/streamlit/issues/3530)).

## Version 0.89.0

_Release date: Sep 22, 2021_

**Highlights**

- ≡ƒÆ░ Introducing `st.experimental_memo` and `experimental_singleton`, a new primitive for caching! See [our blog post](https://blog.streamlit.io/new-experimental-primitives-for-caching/).
- ≡ƒìö Streamlit allows developers to configure their hamburger menu to be more user-centric.

**Notable Changes**

- ≡ƒÆà We updated our UI to a more polished look with a new font.
- ≡ƒÄ¿ We now support `theme.base` in the theme object when it's sent to custom components.
- ≡ƒºá We've modified session state to reset widgets if any of their arguments changed even if they provide a key.
  - Some widget behavior may have changed, but we believe this change makes the most sense. We have added a section to [our documentation](/develop/concepts/widget-semantics) describing how they behave.

**Other Changes**

- ≡ƒÉ₧ Bug fixes: Support svgs from a URL ([#3809](https://github.com/streamlit/streamlit/pull/3809)) and that do not start with `<svg>` tag ([#3789](https://github.com/streamlit/streamlit/pull/3789)).

## Version 0.88.0

_Release date: Sep 2, 2021_

**Highlights**

- Γ¼ç∩╕Å Introducing `st.download_button`, a new button widget for easily downloading files.

**Notable Changes**

- ≡ƒ¢æ We made changes to improve the redacted exception experience on Streamlit Community Cloud. When `client.showErrorDetails=true` exceptions display the Error Type and the Traceback, but redact the actual error text to prevent data leaks.

## Version 0.87.0

_Release date: Aug 19, 2021_

**Highlights**

- ≡ƒöó Introducing `st.metric`, an API for displaying KPIs. Check out the [demo app](https://streamlit-release-demos-0-87streamlit-app-0-87-rfzphf.streamlit.app/) showcasing the functionality.

**Other Changes**

- ≡ƒÉ₧ **Bug Fixes**: File uploader retains state upon expander closing ([#3557](https://github.com/streamlit/streamlit/issues/3557)), setIn Error with `st.empty` ([#3659](https://github.com/streamlit/streamlit/issues/3659)), Missing IFrame embeds in docs ([#3706](https://github.com/streamlit/streamlit/issues/3706)), Fix error writing certain PNG files ([#3597](https://github.com/streamlit/streamlit/issues/3597)).

## Version 0.86.0

_Release date: Aug 5, 2021_

**Highlights**

- ≡ƒÄô Our layout primitives are graduating from beta! You can now use `st.columns`, `st.container` and `st.expander` without the `beta_` prefix.

**Notable Changes**

- ≡ƒô▒ When using `st.columns`, columns will stack vertically when viewport size \<640px so that column layout on smaller viewports is consistent and cleaner. ([#3594](https://github.com/streamlit/streamlit/issues/3594)).

**Other Changes**

- ≡ƒÉ₧ **Bug fixes**: Fixed `st.date_input` crashes if its empty ([#3194](https://github.com/streamlit/streamlit/issues/3194)), Opening files with utf-8([#3022](https://github.com/streamlit/streamlit/issues/3022)), `st.select_slider` resets its state upon interaction ([#3600](https://github.com/streamlit/streamlit/issues/3600)).

## Version 0.85.0

_Release date: Jul 22, 2021_

**Highlights**

- ≡ƒÅ╣ Streamlit now uses [Apache Arrow](https://arrow.apache.org) for serializing data frames when they are sent from Streamlit server to the front end. See our [blog post](https://blog.streamlit.io/).
  - (Users who wish to continue using the legacy data frame serialization can do so by setting the `dataFrameSerialization` config option to `"legacy"` in their `config.toml`).

**Other Changes**

- ≡ƒÉ₧ Bug fixes: Unresponsive pydeck example ([#3395](https://github.com/streamlit/streamlit/issues/3395)), JSON parse error message ([#2324](https://github.com/streamlit/streamlit/issues/2324)), Tooltips rendering ([#3300](https://github.com/streamlit/streamlit/issues/3300)), Colorpicker not working on Streamlit Sharing ([#2689](https://github.com/streamlit/streamlit/issues/2689)).

## Version 0.84.0

_Release date: Jul 1, 2021_

**Highlights**

- ≡ƒºá Introducing `st.session_state` and widget callbacks to allow you to add statefulness to your apps. Check out the [blog post](http://blog.streamlit.io/session-state-for-streamlit/)

**Notable Changes**

- ≡ƒ¬ä `st.text_input` now has an `autocomplete` parameter to allow password managers to be used

**Other Changes**

- Using st.set_page_config to assign the page title no longer appends "Streamlit" to that title ([#3467](https://github.com/streamlit/streamlit/pull/3467))
- NumberInput: disable plus/minus buttons when the widget is already at its max (or min) value ([#3493](https://github.com/streamlit/streamlit/pull/3493))

## Version 0.83.0

_Release date: Jun 17, 2021_

**Highlights**

- ≡ƒ¢ú∩╕Å Updates to Streamlit docs to include step-by-step guides which demonstrate how to connect Streamlit apps to various databases & APIs

**Notable Changes**

- ≡ƒôä `st.form` now has a `clear_on_submit` parameter which "resets" all the form's widgets when the form is submitted.

**Other Changes**

- Fixed bugs regarding file encodings ([#3320](https://github.com/streamlit/streamlit/issues/3220), [#3108](https://github.com/streamlit/streamlit/issues/3108), [#2731](https://github.com/streamlit/streamlit/issues/2731))

## Version 0.82.0

_Release date: May 13, 2021_

**Notable Changes**

- ΓÖ╗∩╕Å Improvements to memory management by forcing garbage collection between script runs.

## Version 0.81.1

_Release date: Apr 29, 2021_

**Highlights**

- ≡ƒô¥ Introducing `st.form` and `st.form_submit_button` to allow you to batch input widgets. Check out our [blog post](http://blog.streamlit.io/introducing-submit-button-and-forms)
- ≡ƒöñ Introducing `st.caption` so you can add explainer text anywhere in you apps.
- ≡ƒÄ¿ Updates to Theming, including ability to build a theme that inherits from any of our default themes.
- ≡ƒÜÇ Improvements to deployment experience to Streamlit sharing from the app menu.

**Other changes**

- Support for binary files in Custom Components ([#3144](https://github.com/streamlit/streamlit/pull/3144))

## Version 0.80.0

_Release date: Apr 8, 2021_

**Highlights**

- ≡ƒöÉ Streamlit now support Secrets management for apps deployed to Streamlit Sharing!
- ΓÜô∩╕Å Titles and headers now come with automatically generated anchor links. Just hover over any title and click the ≡ƒöù to get the link!

**Other changes**

- Added `allow-downloads` capability to custom components ([#3040](https://github.com/streamlit/streamlit/issues/3040))
- Fixed markdown tables in dark theme ([#3020](https://github.com/streamlit/streamlit/issues/3020))
- Improved color picker widget in the Custom Theme dialog ([#2970](https://github.com/streamlit/streamlit/issues/2970))

## Version 0.79.0

_Release date: Mar 18, 2021_

**Highlights**

- ≡ƒîê Introducing support for custom themes. Check out our [blog post](http://blog.streamlit.io/introducing-theming/)
- ≡ƒîÜ This release also introduces dark mode!
- ≡ƒ¢á∩╕Å Support for tooltips on all input widgets

**Other changes**

- Fixed bugs regarding file encodings ([#1936](https://github.com/streamlit/streamlit/issues/1936), [#2606](https://github.com/streamlit/streamlit/issues/2606)) and caching functions ([#2728](https://github.com/streamlit/streamlit/issues/2728))

## Version 0.78.0

_Release date: Mar 4, 2021_

**Features**

- If you're in the Streamlit for Teams beta, we made a few updates to how secrets work. Check the beta docs for more info!
- Dataframes now displays timezones for all DateTime and Time columns, and shows the time with the timezone applied, rather than in UTC

**Notable Bug Fixes**

- Various improvement to column alignment in `st.beta_columns`
- Removed the long-deprecated `format` param from `st.image`, and replaced with `output_format`.

## Version 0.77.0

_Release date: Feb 23, 2021_

**Features**

- Added a new config option `client.showErrorDetails` allowing the developer to control the granularity of error messages. This is useful for when you deploy an app, and want to conceal from your users potentially-sensitive information contained in tracebacks.

**Notable bug fixes**

- Fixed [bug](https://github.com/streamlit/streamlit/issues/1957) where `st.image` wasn't rendering certain kinds of SVGs correctly.
- Fixed [regression](https://github.com/streamlit/streamlit/issues/2699) where the current value of an `st.slider` was only shown on hover.

## Version 0.76.0

_Release date: February 4, 2021_

**Notable Changes**

- ≡ƒÄ¿ [`st.color_picker`](https://docs.streamlit.io/en/0.76.0/api.html#streamlit.color_picker) is now out of beta. This means the old beta_color_picker function, which was marked as deprecated for the past 3 months, has now been replaced with color_picker.
- ≡ƒÉì Display a warning when a Streamlit script is run directly as `python script.py`.
- [`st.image`](https://docs.streamlit.io/en/0.76.0/api.html#streamlit.image)'s `use_column_width` now defaults to an `auto` option which will resize the image to the column width if the image exceeds the column width.
- Γ£é∩╕Å Fixed bugs ([2437](https://github.com/streamlit/streamlit/issues/2437) and [2247](https://github.com/streamlit/streamlit/issues/2247)) with content getting cut off within a [`st.beta_expander`](https://docs.streamlit.io/en/0.76.0/api.html#streamlit.beta_expander)
- ≡ƒô£ Fixed a [bug](https://github.com/streamlit/streamlit/issues/2543) in [`st.dataframe`](https://docs.streamlit.io/en/0.76.0/api.html#streamlit.dataframe) where the scrollbar overlapped with the contents in the last column.
- ≡ƒÆ╛ Fixed a [bug](https://github.com/streamlit/streamlit/issues/2561) for [`st.file_uploader`](https://docs.streamlit.io/en/0.76.0/api.html#streamlit.file_uploader) where file data returned was not the most recently uploaded file.
- Γ₧ò Fixed bugs ([2086](https://github.com/streamlit/streamlit/issues/2086) and [2556](https://github.com/streamlit/streamlit/issues/2556)) where some LaTeX commands were not rendering correctly.

## Version 0.75.0

_Release date: January 21, 2021_

**Notable Changes**

- ≡ƒò│ [`st.empty`](https://docs.streamlit.io/en/0.75.0/api.html#streamlit.empty)
  previously would clear the component at the end of the script. It has now been
  updated to clear the component instantly.
- ≡ƒ¢╣ Previously in wide mode, we had thin margins around the webpage. This has
  now been increased to provide a better visual experience.

## Version 0.74.0

_Release date: January 6, 2021_

**Notable Changes**

- ≡ƒÆ╛ [`st.file_uploader`](https://docs.streamlit.io/en/0.74.0/api.html#streamlit.file_uploader). has been stabilized and the deprecation warning
  and associated configuration option (`deprecation.showfileUploaderEncoding`) has been removed.
- ≡ƒôè [`st.bokeh_chart`](https://docs.streamlit.io/en/0.74.0/api.html#streamlit.bokeh_chart) is no longer duplicated when the page loads.
- ≡ƒÄê Fixed page icon to support emojis with variants (i.e. ≡ƒñªΓÇìΓÖÇ∩╕Å vs ≡ƒñª≡ƒÅ╝ΓÇìΓÖÇ∩╕Å) or dashes (i.e ≡ƒîÖ - crescent-moon).

## Version 0.73.0

_Release date: December 17, 2020_

**Notable Changes**

- ≡ƒÉì Streamlit can now be installed on Python 3.9. Streamlit components are not
  yet compatible with Python 3.9 and must use version 3.8 or earlier.
- ≡ƒº▒ Streamlit Components now allows same origin, enabling features provided by
  the browser such as a webcam component.
- ≡ƒÉÖ Fix Streamlit sharing deploy experience for users running on Git versions
  2.7.0 or earlier.
- ≡ƒº░ Handle unexpected closing of uploaded files for [`st.file_uploader`](https://docs.streamlit.io/en/0.72.0/api.html#streamlit.file_uploader).

## Version 0.72.0

_Release date: December 2, 2020_

**Notable Changes**

- ≡ƒîê Establish a framework for theming and migrate existing components.
- ≡ƒô▒ Improve the sidebar experience for mobile devices.
- ≡ƒº░ Update [`st.file_uploader`](https://docs.streamlit.io/en/0.71.0/api.html#streamlit.file_uploader) to reduce reruns.

## Version 0.71.0

_Release date: November 11, 2020_

**Notable Changes**

- ≡ƒôü Updated [`st.file_uploader`](https://docs.streamlit.io/en/0.71.0/api.html#streamlit.file_uploader)
  to automatically reset buffer on app reruns.
- ≡ƒôè Optimize the default rendering of charts and reduce issues with the initial render.

## Version 0.70.0

_Release date: October 28, 2020_

**Notable Changes**

- ≡ƒº¬ [`st.set_page_config`](https://docs.streamlit.io/en/0.70.0/api.html#streamlit.set_page_config) and [`st.color_picker`](https://docs.streamlit.io/en/0.70.0/api.html#streamlit.color_picker) have now been moved into the
  Streamlit namespace. These will be removed from beta January 28th, 2021. Learn
  more about our beta process [here](https://docs.streamlit.io/en/0.70.0/api.html#beta-and-experimental-features).
- ≡ƒôè Improve display of bar charts for discrete values.

## Version 0.69.0

_Release date: October 15, 2020_

**Highlights:**

- ≡ƒÄü Introducing Streamlit sharing, the best way to deploy, manage, and share your public Streamlit appsΓÇöfor free. Read more about it on our [blog post](http://blog.streamlit.io/introducing-streamlit-sharing/) or sign up [here](https://streamlit.io/sharing)!
- Added `st.experimental_rerun` to programatically re-run your app. Thanks [SimonBiggs](https://github.com/SimonBiggs)!

**Notable Changes**

- ≡ƒô╣ Better support across browsers for start and stop times for st.video.
- ≡ƒû╝ Bug fix for intermittently failing media files
- ≡ƒôª Bug fix for custom components compatibility with Safari. Make sure to upgrade to the latest [streamlit-component-lib](https://www.npmjs.com/package/streamlit-component-lib).

## Version 0.68.0

_Release date: October 8, 2020_

**Highlights:**

- Γîù Introducing new layout options for Streamlit! Move aside, vertical layout.
  Make a little space for... horizontal layout! Check out our
  [blog post](https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/).
- ≡ƒÆ╛ File uploader redesigned with new functionality for multiple files uploads
  and better support for working with uploaded files. This may cause breaking
  changes. Please see the new api in our
  [documentation](https://docs.streamlit.io/en/0.68.0/api.html#streamlit.file_uploader)

**Notable Changes**

- ≡ƒÄê `st.balloon` has gotten a facelift with nicer balloons and smoother animations.
- ≡ƒÜ¿ Breaking Change: Following the deprecation of `st.deck_gl_chart` in
  January 2020, we have now removed the API completely. Please use
  `st.pydeck_chart` instead.
- ≡ƒÜ¿ Breaking Change: Following the deprecation of `width` and `height` for
  `st.altair_chart`, `st.graphviz_chart`, `st.plotly_chart`, and
  `st.vega_lite_chart` in January 2020, we have now removed the args completely.
  Please set the width and height in the respective charting library.

## Version 0.67.0

_Release date: September 16, 2020_

**Highlights:**

- ≡ƒª╖ Streamlit Components can now return bytes to your Streamlit App. To create a
  component that returns bytes, make sure to upgrade to the latest
  [streamlit-component-lib](https://www.npmjs.com/package/streamlit-component-lib).

**Notable Changes**

- ≡ƒôê Deprecation warning: Beginning December 1st, 2020 `st.pyplot()` will require a figure to
  be provided. To disable the deprecation warning, please set `deprecation.showPyplotGlobalUse`
  to `False`
- ≡ƒÄÜ `st.multiselect` and `st.select` are now lightning fast when working with large datasets. Thanks [masa3141](https://github.com/masa3141)!

## Version 0.66.0

_Release date: September 1, 2020_

**Highlights:**

- Γ£Å∩╕Å `st.write` is now available for use in the sidebar!
- ≡ƒÄÜ A slider for distinct or non-numerical values is now available with `st.select_slider`.
- Γîù Streamlit Components can now return dataframes to your Streamlit App. Check out our [SelectableDataTable example](https://github.com/streamlit/component-template/tree/master/examples/SelectableDataTable).
- ≡ƒôª The Streamlit Components library used in our Streamlit Component template is
  now available as a npm package ([streamlit-component-lib](https://www.npmjs.com/package/streamlit-component-lib)) to simplify future upgrades to the latest version.
  Existing components do not need to migrate.

**Notable Changes**

- ≡ƒÉ╝ Support StringDtype from pandas version 1.0.0
- ≡ƒºª Support for running Streamlit on Unix sockets

## Version 0.65.0

_Release date: August 12, 2020_

**Highlights:**

- ΓÜÖ∩╕Å Ability to set page title, favicon, sidebar state, and wide mode via st.beta_set_page_config(). See our [documentation](https://docs.streamlit.io/en/0.65.0/api.html#streamlit.set_page_config) for details.
- ≡ƒô¥ Add stateful behaviors through the use of query parameters with st.experimental_set_query_params and st.experimental_get_query_params. Thanks [@zhaoooyue](https://github.com/zhaoooyue)!
- ≡ƒÉ╝ Improved pandas dataframe support for st.radio, st.selectbox, and st.multiselect.
- ≡ƒ¢æ Break out of your Streamlit app with st.stop.
- ≡ƒû╝ Inline SVG support for st.image.

**Callouts:**

- ≡ƒÜ¿Deprecation Warning: The st.image parameter format has been renamed to output_format.

## Version 0.64.0

_Release date: July 23, 2020_

**Highlights:**

- ≡ƒôè Default matplotlib to display charts with a tight layout. To disable this,
  set `bbox_inches` to `None`, inches as a string, or a `Bbox`
- ≡ƒùâ Deprecation warning for automatic encoding on `st.file_uploader`
- ≡ƒÖê If `gatherUserStats` is `False`, do not even load the Segment library.
  Thanks [@tanmaylaud](https://github.com/tanmaylaud)!

## Version 0.63.0

_Release date: July 13, 2020_

**Highlights:**

- ≡ƒº⌐ **Support for Streamlit Components!!!** See
  [documentation](https://docs.streamlit.io/en/latest/streamlit_components.html) for more info.
- ≡ƒòù Support for datetimes in
  [`st.slider`](https://docs.streamlit.io/en/latest/api.html#streamlit.slider). And, of course, just
  like any other value you use in `st.slider`, you can also pass in two-element lists to get a
  datetime range slider.

## Version 0.62.0

_Release date: June 21, 2020_

**Highlights:**

- ≡ƒô¿ Ability to turn websocket compression on/off via the config option
  `server.enableWebsocketCompression`. This is useful if your server strips HTTP headers and you do
  not have access to change that behavior.
- ≡ƒù¥∩╕Å Out-of-the-box support for CSRF protection using the
  [Cookie-to-header token](https://en.wikipedia.org/wiki/Cross-site_request_forgery#Cookie-to-header_token)
  technique. This means that if you're serving your Streamlit app from multiple replicas you'll need
  to configure them to to use the same cookie secret with the `server.cookieSecret` config option.
  To turn XSRF protection off, set `server.enableXsrfProtection=false`.

**Notable bug fixes:**

- ≡ƒû╝∩╕Å Added a grace period to the image cache expiration logic in order to fix multiple related bugs
  where images sent with `st.image` or `st.pyplot` were sometimes missing.

## Version 0.61.0

_Release date: June 2, 2020_

**Highlights:**

- ≡ƒôà Support for date ranges in `st.date_picker`. See
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.date_picker)
  for more info, but the TLDR is: just pass a list/tuple as the default date and it will be
  interpreted as a range.
- ≡ƒùú∩╕Å You can now choose whether `st.echo` prints the code above or below the output of the echoed
  block. To learn more, refer to the `code_location` argument in the
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.echo).
- ≡ƒôª Improved `@st.cache` support for Keras models and Tensorflow `saved_models`.

## Version 0.60.0

_Release date: May 18, 2020_

**Highlights:**

- Γåò∩╕Å Ability to set the height of an `st.text_area` with the `height` argument
  (expressed in pixels). See
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.text_area) for more.
- ≡ƒöí Ability to set the maximimum number of characters allowed in `st.text_area`
  or `st.text_input`. Check out the `max_chars` argument in the
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.text_area).
- ≡ƒù║∩╕Å Better DeckGL support for the [H3](https://h3geo.org/) geospatial indexing
  system. So now you can use things like `H3HexagonLayer` in
  [`st.pydeck_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.pydeck_chart).
- ≡ƒôª Improved `@st.cache` support for PyTorch TensorBase and Model.

## Version 0.59.0

_Release date: May 05, 2020_

**Highlights:**

- ≡ƒÄ¿ New color-picker widget! Use it with
  [`st.beta_color_picker()`](https://docs.streamlit.io/en/0.69.0/api.html#streamlit.beta_color_picker)
- ≡ƒº¬ Introducing `st.beta_*` and `st.experimental_*` function prefixes, for faster
  Streamlit feature releases. See
  [docs](https://docs.streamlit.io/en/latest/api.html#pre-release-features) for more info.
- ≡ƒôª Improved `@st.cache` support for SQL Alchemy objects, CompiledFFI, PyTorch
  Tensors, and `builtins.mappingproxy`.

## Version 0.58.0

_Release date: April 22, 2020_

**Highlights:**

- ≡ƒÆ╝ Made `st.selectbox` filtering case-insensitive.
- πê¼ Better support for Tensorflow sessions in `@st.cache`.
- ≡ƒôè Changed behavior of `st.pyplot` to auto-clear the figure only when using
  the global Matplotlib figure (i.e. only when calling `st.pyplot()` rather
  than `st.pyplot(fig)`).

## Version 0.57.0

_Release date: March 26, 2020_

**Highlights:**

- ΓÅ▓∩╕Å Ability to set expiration options for `@st.cache`'ed functions by setting
  the `max_entries` and `ttl` arguments. See
  [docs](https://docs.streamlit.io/en/latest/api.html#streamlit.cache).
- ≡ƒåÖ Improved the machinery behind `st.file_uploader`, so it's much more
  performant now! Also increased the default upload limit to 200MB
  (configurable via `server.max_upload_size`).
- ≡ƒöÆ The `server.address` config option now _binds_ the server to that address
  for added security.
- ≡ƒôä Even more details added to error messages for `@st.cache` for easier
  debugging.

## Version 0.56.0

_Release date: February 15, 2020_

**Highlights:**

- ≡ƒôä Improved error messages for st.cache. The errors now also point to the new
  caching docs we just released. Read more
  [here](https://discuss.streamlit.io/t/help-us-stress-test-streamlit-s-latest-caching-update/1944)!

**Breaking changes:**

- ≡ƒÉì As [announced last month](https://discuss.streamlit.io/t/streamlit-will-deprecate-python-2-in-february/1656),
  **Streamlit no longer supports Python 2.** To use Streamlit you'll need
  Python 3.5 or above.

## Version 0.55.0

_Release date: February 4, 2020_

**Highlights:**

- ≡ƒô║ **Ability to record screencasts directly from Streamlit!** This allows
  you to easily record and share explanations about your models, analyses,
  data, etc. Just click Γÿ░ then "Record a screencast". Give it a try!

## Version 0.54.0

_Release date: January 29, 2020_

**Highlights:**

- Γî¿∩╕Å Support for password fields! Just pass `type="password"` to
  `st.text_input()`.

**Notable fixes:**

- Γ£│∩╕Å Numerous st.cache improvements, including better support for complex objects.
- ≡ƒùú∩╕Å Fixed cross-talk in sidebar between multiple users.

**Breaking changes:**

- If you're using the SessionState <del>hack</del> Gist, you should re-download it!
  Depending on which hack you're using, here are some links to save you some
  time:
  - [SessionState.py](https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92)
  - [st_state_patch.py](https://gist.github.com/tvst/0899a5cdc9f0467f7622750896e6bd7f)

## Version 0.53.0

_Release date: January 14, 2020_

**Highlights:**

- ≡ƒù║∩╕Å Support for all DeckGL features! Just use
  [Pydeck](https://deckgl.readthedocs.io/en/latest/) instead of
  [`st.deck_gl_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.pydeck_chart).
  To do that, simply pass a PyDeck object to
  [`st.pydeck_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.pydeck_chart),
  [`st.write`](https://docs.streamlit.io/en/latest/api.html#streamlit.write),
  or [magic](https://docs.streamlit.io/en/latest/api.html#magic).

  _Note that as a **preview release** things may change in the near future.
  Looking forward to hearing input from the community before we stabilize the
  API!_

  **The goals is for this to replace `st.deck_gl_chart`,** since it
  is does everything the old API did _and much more!_

- ≡ƒåò Better handling of Streamlit upgrades while developing. We now auto-reload
  the browser tab if the app it is displaying uses a newer version of Streamlit
  than the one the tab is running.

- ≡ƒææ New favicon, with our new logo!

**Notable fixes:**

- Magic now works correctly in Python 3.8. It no longer causes
  docstrings to render in your app.

**Breaking changes:**

- Updated how we calculate the default width and height of all chart types.
  We now leave chart sizing up to your charting library itself, so please refer
  to the library's documentation.

  As a result, the `width` and `height` arguments have been deprecated
  from most chart commands, and `use_container_width` has been introduced
  everywhere to allow you to make charts fill as much horizontal space as
  possible (this used to be the default).

## Version 0.52.0

_Release date: December 20, 2019_

**Highlights:**

- ≡ƒôñ Preview release of the file uploader widget. To try it out just call
  [`st.file_uploader`](https://docs.streamlit.io/en/latest/api.html#streamlit.file_uploader)!

  _Note that as a **preview release** things may change in the near future.
  Looking forward to hearing input from the community before we stabilize the
  API!_

- ≡ƒæï Support for [emoji codes](https://www.webfx.com/tools/emoji-cheat-sheet/) in
  `st.write` and `st.markdown`! Try it out with `st.write("Hello :wave:")`.

**Breaking changes:**

- ≡ƒº╣ `st.pyplot` now clears figures by default, since that's what you want 99% of
  the time. This allows you to create two or more Matplotlib charts without
  having to call
  [`pyplot.clf`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.clf.html)
  every time. If you want to turn this behavior off, use
  [`st.pyplot(clear_figure=False)`](https://docs.streamlit.io/en/latest/api.html#streamlit.pyplot)
- ≡ƒôú `st.cache` no longer checks for input mutations. This is the first change
  of our ongoing effort to simplify the caching system and prepare Streamlit
  for the launch of other caching primitives like Session State!

## Version 0.51.0

_Release date: November 30, 2019_

**Highlights:**

- ≡ƒÉò You can now tweak the behavior of the file watcher with the config option `server.fileWatcherType`. Use it to switch between:
  - `auto` (default) : Streamlit will attempt to use the watchdog module, and
    falls back to polling if watchdog is not available.
  - `watchdog` : Force Streamlit to use the watchdog module.
  - `poll` : Force Streamlit to always use polling.
  - `none` : Streamlit will not watch files.

**Notable bug fixes:**

- Fix the "keyPrefix" option in static report sharing [#724](https://github.com/streamlit/streamlit/pull/724)
- Add support for getColorX and getTargetColorX to DeckGL Chart [#718](https://github.com/streamlit/streamlit/pull/718)
- Fixing Tornado on Windows + Python 3.8 [#682](https://github.com/streamlit/streamlit/pull/682)
- Fall back on webbrowser if xdg-open is not installed on Linux [#701](https://github.com/streamlit/streamlit/pull/701)
- Fixing number input spin buttons for Firefox [#683](https://github.com/streamlit/streamlit/pull/683)
- Fixing CTRL+ENTER on Windows [#699](https://github.com/streamlit/streamlit/pull/699)
- Do not automatically create credential file when in headless mode [#467](https://github.com/streamlit/streamlit/pull/467)

## Version 0.50.1

_Release date: November 10, 2019_

**Highlights:**

- ≡ƒæ⌐ΓÇì≡ƒÄô SymPy support and ability to draw mathematical expressions using LaTeX! See
  [`st.latex`](/develop/api-reference/text/st.latex),
  [`st.markdown`](/develop/api-reference/text/st.markdown),
  and
  [`st.write`](/develop/api-reference/write-magic/st.write).
- ≡ƒîä You can now set config options using environment variables. For example,
  `export STREAMLIT_SERVER_PORT=9876`.
- ≡ƒÉ▒ Ability to call `streamlit run` directly with Github and Gist URLs. No
  need to grab the "raw" URL first!
- ≡ƒôâ Cleaner exception stack traces. We now remove all Streamlit-specific code
  from stack traces originating from the user's app.

## Version 0.49.0

_Release date: October 23, 2019_

**Highlights:**

- ≡ƒÆ» New input widget for entering numbers with the keyboard: `st.number_input()`
- ≡ƒô║ Audio/video improvements: ability to load from a URL, to embed YouTube
  videos, and to set the start position.
- ≡ƒñ¥ You can now (once again) share static snapshots of your apps to S3! See
  the S3 section of `streamlit config show` to set it up. Then share from
  top-right menu.
- ΓÜÖ∩╕Å Use `server.baseUrlPath` config option to set Streamlit's URL to something
  like `http://domain.com/customPath`.

**Notable bug fixes:**

- Fixes numerous Windows bugs, including [Issues
  #339](https://github.com/streamlit/streamlit/issues/399) and
  [#401](https://github.com/streamlit/streamlit/issues/301).

## Version 0.48.0

_Release date: October 12, 2019_

**Highlights:**

- ≡ƒöº Ability to set config options as command line flags or in a local config file.
- Γåò∩╕Å You can now maximize charts and images!
- ΓÜí Streamlit is now much faster when writing data in quick succession to your app.
- Γ£│∩╕Å Ability to blacklist folder globs from "run on save" and `@st.cache` hashing.
- ≡ƒÄ¢∩╕Å Improved handling of widget state when Python file is modified.
- ≡ƒÖê Improved HTML support in `st.write` and `st.markdown`. HTML is still unsafe, though!

**Notable bug fixes:**

- Fixes `@st.cache` bug related to having your Python environment on current
  working directory. [Issue #242](https://github.com/streamlit/streamlit/issues/242)
- Fixes loading of root url `/` on Windows. [Issue #244](https://github.com/streamlit/streamlit/issues/244)

## Version 0.47.0

_Release date: October 1, 2019_

**Highlights:**

- ≡ƒîä New hello.py showing off 4 glorious Streamlit apps. Try it out!
- ≡ƒöä Streamlit now automatically selects an unused port when 8501 is already in use.
- ≡ƒÄü Sidebar support is now out of beta! Just start any command with `st.sidebar.` instead of `st.`
- ΓÜí Performance improvements: we added a cache to our websocket layer so we no longer re-send data to the browser when it hasn't changed between runs
- ≡ƒôê Our "native" charts `st.line_chart`, `st.area_chart` and `st.bar_chart` now use Altair behind the scenes
- ≡ƒö½ Improved widgets: custom st.slider labels; default values in multiselect
- ≡ƒò╡∩╕ÅΓÇìΓÖÇ∩╕Å The filesystem watcher now ignores hidden folders and virtual environments
- ≡ƒÆà Plus lots of polish around caching and widget state management

**Breaking change:**

- ≡ƒ¢í∩╕Å We have temporarily disabled support for sharing static "snapshots" of Streamlit apps. Now that we're no longer in a limited-access beta, we need to make sure sharing is well thought through and abides by laws like the DMCA. But we're working on a solution!

## Version 0.46.0

_Release date: September 19, 2019_

**Highlights:**

- Γ£¿ Magic commands! Use `st.write` without typing `st.write`. See
  [https://docs.streamlit.io/en/latest/api.html#magic-commands](https://docs.streamlit.io/en/latest/api.html#magic-commands)
- ≡ƒÄ¢∩╕Å New `st.multiselect` widget.
- ≡ƒÉì Fixed numerous install issues so now you can use `pip install streamlit`
  even in Conda! We've therefore deactivated our Conda repo.
- ≡ƒÉ₧ Multiple bug fixes and additional polish in preparation for our launch!

**Breaking change:**

- ≡ƒ¢í∩╕Å HTML tags are now blacklisted in `st.write`/`st.markdown` by default. More
  information and a temporary work-around at:
  [https://github.com/streamlit/streamlit/issues/152](https://github.com/streamlit/streamlit/issues/152)

## Version 0.45.0

_Release date: August 28, 2019_

**Highlights:**

- ≡ƒÿ▒ Experimental support for _sidebar_! Let us know if you want to be a beta
  tester.
- ≡ƒÄü Completely redesigned `st.cache`! Much more performant, has a cleaner API,
  support for caching functions called by `@st.cached` functions,
  user-friendly error messages, and much more!
- ≡ƒû╝∩╕Å Lightning fast `st.image`, ability to choose between JPEG and PNG
  compression, and between RGB and BGR (for OpenCV).
- ≡ƒÆí Smarter API for `st.slider`, `st.selectbox`, and `st.radio`.
- ≡ƒñû Automatically fixes the Matplotlib backend -- no need to edit .matplotlibrc

## Version 0.44.0

_Release date: July 28, 2019_

**Highlights:**

- ΓÜí Lightning-fast reconnect when you do a ctrl-c/rerun on your Streamlit code
- ≡ƒôú Useful error messages when the connection fails
- ≡ƒÆÄ Fixed multiple bugs and improved polish of our newly-released interactive widgets

## Version 0.43.0

_Release date: July 9, 2019_

**Highlights:**

- ΓÜí Support for interactive widgets! ≡ƒÄê≡ƒÄë

## Version 0.42.0

_Release date: July 1, 2019_

**Highlights:**

- ≡ƒÆ╛ Ability to save Vega-Lite and Altair charts to SVG or PNG
- ≡ƒÉç We now cache JS files in your browser for faster loading
- Γ¢ö Improvements to error-handling inside Streamlit apps

## Version 0.41.0

_Release date: June 24, 2019_

**Highlights:**

- ≡ƒôê Greatly improved our support for named datasets in Vega-Lite and Altair
- ≡ƒÖä Added ability to ignore certain folders when watching for file changes. See the `server.folderWatchBlacklist` config option.
- Γÿö More robust against syntax errors on the user's script and imported modules

## Version 0.40.0

_Release date: June 10, 2019_

**Highlights:**

- Streamlit is more than 10x faster. Just save and watch your analyses update instantly.
- We changed how you run Streamlit apps:
  `$ streamlit run your_script.py [script args]`
- Unlike the previous versions of Streamlit, `streamlit run [script] [script args]` creates a server (now you don't need to worry if the proxy is up). To kill the server, all you need to do is hit **Ctrl+c**.

**Why is this so much faster?**

Now, Streamlit keeps a single Python session running until you kill the server. This means that Streamlit can re-run your code without kicking off a new process; imported libraries are cached to memory. An added bonus is that `st.cache` now caches to memory instead of to disk.

**What happens if I run Streamlit the old way?**

If you run `$ python your_script.py` the script will execute from top to bottom, but won't produce a Streamlit app.

**What are the limitations of the new architecture?**

- To switch Streamlit apps, first you have to kill the Streamlit server with **Ctrl-c**. Then, you can use `streamlit run` to generate the next app.
- Streamlit only works when used inside Python files, not interactively from the Python REPL.

**What else do I need to know?**

- The strings we print to the command line when **liveSave** is on have been cleaned up. You may need to adjust any RegEx that depends on those.
- A number of config options have been renamed:

  | Old config                 | New config            |
  | -------------------------- | --------------------- |
  | proxy.isRemote             | server.headless       |
  | proxy.liveSave             | server.liveSave       |
  | proxy.runOnSave            | server.runOnSave      |
  | proxy.watchFileSystem      | server.runOnSave      |
  | proxy.enableCORS           | server.enableCORS     |
  | proxy.port                 | server.port           |
  | browser.proxyAddress       | browser.serverAddress |
  | browser.proxyPort          | browser.serverPort    |
  | client.waitForProxySecs    | _n/a_                 |
  | client.throttleSecs        | _n/a_                 |
  | client.tryToOutliveProxy   | _n/a_                 |
  | client.proxyAddress        | _n/a_                 |
  | client.proxyPort           | _n/a_                 |
  | proxy.autoCloseDelaySecs   | _n/a_                 |
  | proxy.reportExpirationSecs | _n/a_                 |

**What if something breaks?**

If the new Streamlit isn't working, please let us know by Slack or email. You can downgrade at any time with these commands:

```bash
pip install --upgrade streamlit==0.37
```

```bash
conda install streamlit=0.37
```

**What's next?**

Thank you for staying with us on this journey! This version of Streamlit lays the foundation for interactive widgets, a new feature of Streamlit we're really excited to share with you in the next few months.

## Version 0.36.0

_Release date: May 03, 2019_

**Highlights**

- ≡ƒÜúΓÇìΓÖÇ∩╕Å `st.progress()` now also accepts floats from 0.0ΓÇô1.0
- ≡ƒñ» Improved rendering of long headers in DataFrames
- ≡ƒöÉ Shared apps now default to HTTPS

## Version 0.35.0

_Release date: April 26, 2019_

**Highlights**

- ≡ƒô╖ Bokeh support! Check out docs for `st.bokeh_chart`
- ΓÜí∩╕Å Improved the size and load time of saved apps
- ΓÜ╛∩╕Å Implemented better error-catching throughout the codebase

```

File: api-reference/_index.md
```

---

title: API Reference
slug: /develop/api-reference

---

# API reference

Streamlit makes it easy for you to visualize, mutate, and share data. The API
reference is organized by activity type, like displaying data or optimizing
performance. Each section includes methods associated with the activity type,
including examples.

Browse our API below and click to learn more about any of our available commands! ≡ƒÄê

## Display almost anything

### Write and magic

<br />

<TileContainer>

<RefCard href="/develop/api-reference/write-magic/st.write">

<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">

<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>

### Text elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/text/st.markdown">

<Image pure alt="screenshot" src="/images/api/markdown.jpg" />

<h4>Markdown</h4>

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.title">

<Image pure alt="screenshot" src="/images/api/title.jpg" />

<h4>Title</h4>

Display text in title formatting.

```python
st.title("The app title")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.header">

<Image pure alt="screenshot" src="/images/api/header.jpg" />

<h4>Header</h4>

Display text in header formatting.

```python
st.header("This is a header")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.subheader">

<Image pure alt="screenshot" src="/images/api/subheader.jpg" />

<h4>Subheader</h4>

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.caption">

<Image pure alt="screenshot" src="/images/api/caption.jpg" />

<h4>Caption</h4>

Display text in small font.

```python
st.caption("This is written small caption text")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.code">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

<h4>Code block</h4>

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.echo">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

<h4>Echo</h4>

Display some code in the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.latex">

<Image pure alt="screenshot" src="/images/api/latex.jpg" />

<h4>LaTeX</h4>

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.text">

<Image pure alt="screenshot" src="/images/api/text.jpg" />

<h4>Preformatted text</h4>

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.divider">

<Image pure alt="screenshot" src="/images/api/divider.jpg" />

<h4>Divider</h4>

Display a horizontal rule.

```python
st.divider()
```

</RefCard>
</TileContainer>

<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">

<Image pure alt="screenshot" src="/images/api/components/annotated-text.jpg" />

<h4>Annotated text</h4>

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/JohnSnowLabs/nlu">

<Image pure alt="screenshot" src="/images/api/components/nlu.jpg" />

<h4>NLU</h4>

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! <3')
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-mentions.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
mention(label="An awesome Streamlit App", icon="streamlit",  url="https://extras.streamlit.app",)
```

</ComponentCard>
</ComponentSlider>

### Data elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/data/st.dataframe">
<Image pure alt="screenshot" src="/images/api/dataframe.jpg" />

<h4>Dataframes</h4>

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.column_config">

<Image pure alt="screenshot" src="/images/api/column_config.jpg" />

<h4>Column configuration</h4>

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.table">
<Image pure alt="screenshot" src="/images/api/table.jpg" />

<h4>Static tables</h4>

Display a static table.

```python
st.table(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.metric">
<Image pure alt="screenshot" src="/images/api/metric.jpg" />

<h4>Metrics</h4>

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.json">
<Image pure alt="screenshot" src="/images/api/json.jpg" />

<h4>Dicts and JSON</h4>

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/PablocFonseca/streamlit-aggrid">

<Image pure alt="screenshot" src="/images/api/components/aggrid.jpg" />

<h4>Streamlit Aggrid</h4>

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)

new_df = grid_return['data']
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">

<Image pure alt="screenshot" src="/images/api/components/pandas-profiling.jpg" />

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])

selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-metric-cards.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)

style_metric_cards()
```

</ComponentCard>

</ComponentSlider>

### Chart elements

<br />

<TileContainer>

<RefCard href="/develop/api-reference/charts/st.area_chart">
<Image pure alt="screenshot" src="/images/api/area_chart.jpg" />

<h4>Simple area charts</h4>

Display an area chart.

```python
st.area_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bar_chart">
<Image pure alt="screenshot" src="/images/api/bar_chart.jpg" />

<h4>Simple bar charts</h4>

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.line_chart">
<Image pure alt="screenshot" src="/images/api/line_chart.jpg" />

<h4>Simple line charts</h4>

Display a line chart.

```python
st.line_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.scatter_chart">
<Image pure alt="screenshot" src="/images/api/scatter_chart.svg" />

<h4>Simple scatter charts</h4>

Display a line chart.

```python
st.scatter_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.map">
<Image pure alt="screenshot" src="/images/api/map.jpg" />

<h4>Scatterplots on maps</h4>

Display a map with points on it.

```python
st.map(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.pyplot">
<Image pure alt="screenshot" src="/images/api/pyplot.jpg" />

<h4>Matplotlib</h4>

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.altair_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Altair</h4>

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.vega_lite_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Vega-Lite</h4>

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.plotly_chart">
<Image pure alt="screenshot" src="/images/api/plotly_chart.jpg" />

<h4>Plotly</h4>

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bokeh_chart">
<Image pure alt="screenshot" src="/images/api/bokeh_chart.jpg" />

<h4>Bokeh</h4>

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.pydeck_chart">
<Image pure alt="screenshot" src="/images/api/pydeck_chart.jpg" />

<h4>PyDeck</h4>

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.graphviz_chart">
<Image pure alt="screenshot" src="/images/api/graphviz_chart.jpg" />

<h4>GraphViz</h4>

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/tvst/plost">

<Image pure alt="screenshot" src="/images/api/components/plost.jpg" />

<h4>Plost</h4>

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

</ComponentCard>

<ComponentCard href="https://github.com/facebookresearch/hiplot">

<Image pure alt="screenshot" src="/images/api/components/hiplot.jpg" />

<h4>HiPlot</h4>

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-echarts">

<Image pure alt="screenshot" src="/images/api/components/echarts.jpg" />

<h4>ECharts</h4>

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/explosion/spacy-streamlit">

<Image pure alt="screenshot" src="/images/api/components/spacy.jpg" />

<h4>Spacy-Streamlit</h4>

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

</ComponentCard>

<ComponentCard href="https://github.com/ChrisDelClea/streamlit-agraph">

<Image pure alt="screenshot" src="/images/api/components/agraph.jpg" />

<h4>Streamlit Agraph</h4>

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-chart-annotations.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

</ComponentCard>

</ComponentSlider>

### Input widgets

<br />

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.button">

<Image pure alt="screenshot" src="/images/api/button.svg" />

<h4>Button</h4>

Display a button widget.

```python
clicked = st.button("Click me")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.download_button">

<Image pure alt="screenshot" src="/images/api/download_button.svg" />

<h4>Download button</h4>

Display a download button widget.

```python
st.download_button("Download file", file)
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button">

<Image pure alt="screenshot" src="/images/api/form_submit_button.svg" />

<h4>Form button</h4>

Display a form submit button. For use with `st.form`.

```python
st.form_submit_button("Sign up")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.link_button">

<Image pure alt="screenshot" src="/images/api/link_button.svg" />

<h4>Link button</h4>

Display a link button.

```python
st.link_button("Go to gallery", url)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="≡ƒÅá")
st.page_link("pages/profile.py", label="My profile")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.checkbox">

<Image pure alt="screenshot" src="/images/api/checkbox.jpg" />

<h4>Checkbox</h4>

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.color_picker">

<Image pure alt="screenshot" src="/images/api/color_picker.jpg" />

<h4>Color picker</h4>

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.multiselect">

<Image pure alt="screenshot" src="/images/api/multiselect.jpg" />

<h4>Multiselect</h4>

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.radio">

<Image pure alt="screenshot" src="/images/api/radio.jpg" />

<h4>Radio</h4>

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.selectbox">

<Image pure alt="screenshot" src="/images/api/selectbox.jpg" />

<h4>Selectbox</h4>

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.select_slider">

<Image pure alt="screenshot" src="/images/api/select_slider.jpg" />

<h4>Select-slider</h4>

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.toggle">

<Image pure alt="screenshot" src="/images/api/toggle.jpg" />

<h4>Toggle</h4>

Display a toggle widget.

```python
activated = st.toggle("Activate")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.number_input">

<Image pure alt="screenshot" src="/images/api/number_input.jpg" />

<h4>Number input</h4>

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.slider">

<Image pure alt="screenshot" src="/images/api/slider.jpg" />

<h4>Slider</h4>

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.date_input">

<Image pure alt="screenshot" src="/images/api/date_input.jpg" />

<h4>Date input</h4>

Display a date input widget.

```python
date = st.date_input("Your birthday")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.time_input">

<Image pure alt="screenshot" src="/images/api/time_input.jpg" />

<h4>Time input</h4>

Display a time input widget.

```python
time = st.time_input("Meeting time")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_area">

<Image pure alt="screenshot" src="/images/api/text_area.jpg" />

<h4>Text-area</h4>

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_input">

<Image pure alt="screenshot" src="/images/api/text_input.jpg" />

<h4>Text input</h4>

Display a single-line text input widget.

```python
name = st.text_input("First name")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.experimental_data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.file_uploader">

<Image pure alt="screenshot" src="/images/api/file_uploader.jpg" />

<h4>File Uploader</h4>

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.camera_input">

<Image pure alt="screenshot" src="/images/api/camera_input.jpg" />

<h4>Camera input</h4>

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">

<Image pure alt="screenshot" src="/images/api/components/timeline.jpg" />

<h4>Timeline</h4>

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">

<Image pure alt="screenshot" src="/images/api/components/camera-live.jpg" />

<h4>Camera input live</h4>

Alternative for st.camera_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/AI-Yash/st-chat">

<Image pure alt="screenshot" src="/images/api/components/chat.jpg" />

<h4>Streamlit Chat</h4>

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

</ComponentCard>

<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">

<Image pure alt="screenshot" src="/images/api/components/option-menu.jpg" />

<h4>Streamlit Option Menu</h4>

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-toggle.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """≡ƒÑ╖ Surprise! Here's some additional content""",)
```

</ComponentCard>

</ComponentSlider>

### Media elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/media/st.image">

<Image pure alt="screenshot" src="/images/api/image.jpg" />

<h4>Image</h4>

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

</RefCard>
<RefCard href="/develop/api-reference/media/st.audio">

<Image pure alt="screenshot" src="/images/api/audio.jpg" />

<h4>Audio</h4>

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```

</RefCard>
<RefCard href="/develop/api-reference/media/st.video">

<Image pure alt="screenshot" src="/images/api/video.jpg" />

<h4>Video</h4>

Display a video player.

```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/whitphx/streamlit-webrtc">

<Image pure alt="screenshot" src="/images/api/components/webrtc.jpg" />

<h4>Streamlit Webrtc</h4>

Handling and transmitting real-time video/audio streams with Streamlit. Created by [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas

st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/fcakyon/streamlit-image-comparison">

<Image pure alt="screenshot" src="/images/api/components/image-comparison.jpg" />

<h4>Image Comparison</h4>

Compare images with a slider using [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison

image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

</ComponentCard>

<ComponentCard href="https://github.com/turner-anderson/streamlit-cropper">

<Image pure alt="screenshot" src="/images/api/components/cropper.jpg" />

<h4>Streamlit Cropper</h4>

A simple image cropper for Streamlit. Created by [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper

st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates

streamlit_image_coordinates("https://placekitten.com/200/300")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

</ComponentSlider>

### Layouts and containers

<br />

<TileContainer>
<RefCard href="/develop/api-reference/layout/st.columns">

<Image pure alt="screenshot" src="/images/api/columns.jpg" />

<h4>Columns</h4>

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.container">

<Image pure alt="screenshot" src="/images/api/container.jpg" />

<h4>Container</h4>

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.empty">

<Image pure alt="screenshot" src="/images/api/empty.jpg" />

<h4>Empty</h4>

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.expander">

<Image pure alt="screenshot" src="/images/api/expander.jpg" />

<h4>Expander</h4>

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
  st.write("This is more content")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.popover">

<Image pure alt="screenshot" src="/images/api/popover.svg" />

<h4>Popover</h4>

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
  st.checkbox("Show completed")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.sidebar">

<Image pure alt="screenshot" src="/images/api/sidebar.jpg" />

<h4>Sidebar</h4>

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

</RefCard>
<RefCard href="/develop/api-reference/layout/st.tabs">

<Image pure alt="screenshot" src="/images/api/tabs.jpg" />

<h4>Tabs</h4>

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "≡ƒÅá"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

### Chat elements

<br />

Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message.

<TileContainer>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_message">

<Image pure alt="screenshot" src="/images/api/chat_message.jpg" />

<h4>Chat message</h4>

Insert a chat message container.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello ≡ƒæï")
    st.line_chart(np.random.randn(30, 3))
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.status">

<Image pure alt="screenshot" src="/images/api/status.jpg" />

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
</TileContainer>

### Status elements

<br />

<TileContainer>
<RefCard href="/develop/api-reference/status/st.progress">

<Image pure alt="screenshot" src="/images/api/progress.jpg" />

<h4>Progress bar</h4>

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.spinner">

<Image pure alt="screenshot" src="/images/api/spinner.jpg" />

<h4>Spinner</h4>

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.status">

<Image pure alt="screenshot" src="/images/api/status.jpg" />

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.toast">

<Image pure alt="screenshot" src="/images/api/toast.jpg" />

<h4>Toast</h4>

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='≡ƒºê')
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.balloons">

<Image pure alt="screenshot" src="/images/api/balloons.jpg" />

<h4>Balloons</h4>

Display celebratory balloons!

```python
do_something()

# Celebrate when all done!
st.balloons()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.snow">

<Image pure alt="screenshot" src="/images/api/snow.jpg" />

<h4>Snowflakes</h4>

Display celebratory snowflakes!

```python
do_something()

# Celebrate when all done!
st.snow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.success">

<Image pure alt="screenshot" src="/images/api/success.jpg" />

<h4>Success box</h4>

Display a success message.

```python
st.success("Match found!")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.info">

<Image pure alt="screenshot" src="/images/api/info.jpg" />

<h4>Info box</h4>

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.warning">

<Image pure alt="screenshot" src="/images/api/warning.jpg" />

<h4>Warning box</h4>

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.error">

<Image pure alt="screenshot" src="/images/api/error.jpg" />

<h4>Error box</h4>

Display error message.

```python
st.error("We encountered an error")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.exception">

<Image pure alt="screenshot" src="/images/api/exception.jpg" />

<h4>Exception output</h4>

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">

<Image pure alt="screenshot" src="/images/api/components/custom-notification-box.jpg" />

<h4>Custom notification box</h4>

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-emojis.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="≡ƒÄê", font_size=54,
  falling_speed=5, animation_length="infinite",)
```

</ComponentCard>

</ComponentSlider>

## App logic and configuration

### Navigation and pages

<br />

<TileContainer>

<RefCard href="/develop/api-reference/navigation/st.switch_page">

<h4>Switch page</h4>

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="≡ƒÅá")
st.page_link("pages/profile.py", label="My profile")
```

</RefCard>

</TileContainer>

### Execution flow

<br />

<TileContainer>
<RefCard href="/develop/api-reference/execution-flow/st.form" size="half">

<h4>Forms</h4>

Create a form that batches elements together with a ΓÇ£Submit" button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.fragment" size="half">

<h4>Partial reruns</h4>

Define a fragment to rerun independently from the rest of the script.

```python
@st.experimental_fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.rerun">

<h4>Rerun script</h4>

Rerun the script immediately.

```python
st.rerun()
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.stop">

<h4>Stop execution</h4>

Stops execution immediately.

```python
st.stop()
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/kmcgrady/streamlit-autorefresh">

<Image pure alt="screenshot" src="/images/api/components/autorefresh.jpg" />

<h4>Autorefresh</h4>

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "≡ƒÅá"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

### Caching and state

<br />

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.cache_data" size="half">

<h4>Cache data</h4>

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_resource" size="half">

<h4>Cache resource</h4>

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.session_state">

<h4>Session state</h4>

Session state is a way to share variables between reruns, for each user session.

```python
st.session_state['key'] = value
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.query_params">

<h4>Query parameters</h4>

Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

</RefCard>

</TileContainer>

### Connections and databases

#### Setup your connection

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connection" size="half">

<Image pure alt="screenshot" src="/images/api/connection.svg" />

<h4>Create a connection</h4>

Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</RefCard>
</TileContainer>

#### Built-in connections

<TileContainer>

<RefCard href="/develop/api-reference/connections/st.connections.snowflakeconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SnowflakeConnection.svg" />

<h4>SnowflakeConnection</h4>

A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

</RefCard>

<RefCard href="/develop/api-reference/connections/st.connections.sqlconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SQLConnection.svg" />

<h4>SQLConnection</h4>

A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

</RefCard>
</TileContainer>

#### Build your own connections

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.baseconnection" size="half">

<h4>Connection base class</h4>

Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>

</TileContainer>

#### Secrets management

<TileContainer>

<RefCard href="/develop/api-reference/connections/st.secrets" size="half">

<h4>Secrets singleton</h4>

Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

</RefCard>
<RefCard href="/develop/api-reference/connections/secrets.toml" size="half">

<h4>Secrets file</h4>

Save your secrets in a per-project or per-profile TOML file.

```python
OpenAI_key = "<YOUR_SECRET_KEY>"
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/mkhorasani/Streamlit-Authenticator">

<Image pure alt="screenshot" src="/images/api/components/authenticator.jpg" />

<h4>Authenticator</h4>

A secure authentication module to validate user credentials. Created by [@mkhorasani](https://github.com/mkhorasani).

```python
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate( config['credentials'], config['cookie']['name'],
config['cookie']['key'], config['cookie']['expiry_days'], config['preauthorized'])
```

</ComponentCard>

<ComponentCard href="https://github.com/gagangoku/streamlit-ws-localstorage">

<Image pure alt="screenshot" src="/images/api/components/localstorage.jpg" />

<h4>WS localStorage</h4>

A simple synchronous way of accessing localStorage from your app. Created by [@gagangoku](https://github.com/gagangoku).

```python
from streamlit_ws_localstorage import injectWebsocketCode

ret = conn.setLocalStorageVal(key='k1', val='v1')
st.write('ret: ' + ret)
```

</ComponentCard>

<ComponentCard href="https://github.com/conradbez/streamlit-auth0">

<Image pure alt="screenshot" src="/images/api/components/auth0.jpg" />

<h4>Streamlit Auth0</h4>

The fastest way to provide comprehensive login inside Streamlit. Created by [@conradbez](https://github.com/conradbez).

```python
from auth0_component import login_button

user_info = login_button(clientId, domain = domain)
st.write(user_info)
```

</ComponentCard>

</ComponentSlider>

### Custom Components

<br />

<TileContainer>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.declare_component">

<h4>Declare a component</h4>

Create and register a custom component.

```python
st.components.v1.declare_component(
    "custom_slider",
    "/frontend",
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.html">

<h4>HTML</h4>

Display an HTML string in an iframe.

```python
st.components.v1.html(
    "<p>Foo bar.</p>"
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.iframe">

<h4>iframe</h4>

Load a remote URL in an iframe.

```python
st.components.v1.iframe(
    "docs.streamlit.io"
)
```

</RefCard>

</TileContainer>

### Utilities and user info

<br />

<TileContainer>
<RefCard href="/develop/api-reference/utilities/st.experimental_user">

<h4>User info</h4>

`st.experimental_user` returns information about the logged-in user of private apps on Streamlit Community Cloud.

```python
if st.experimental_user.email == "foo@corp.com":
  st.write("Welcome back, ", st.experimental_user.email)
else:
  st.write("You are not authorized to view this page.")
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.help">

<h4>Get help</h4>

Display objectΓÇÖs doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.html">

<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
css = """
<style>
    p { color: red; }
</style>
"""
st.html(css)
```

</RefCard>
</TileContainer>

### Configuration

<br />

<TileContainer>
<RefCard href="/develop/api-reference/configuration/config.toml">

<h4>Configuration file</h4>

Configures the default settings for your app.

```
your-project/
Γö£ΓöÇΓöÇ .streamlit/
Γöé   ΓööΓöÇΓöÇ config.toml
ΓööΓöÇΓöÇ your_app.py
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_page_config">

<h4>Set page title, favicon, and more</h4>

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```

</RefCard>
</TileContainer>

## Developer tools

### App testing

<br />

<TileContainer>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest" size="full">

<h4>st.testing.v1.AppTest</h4>

`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception

at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_file" size="full">

<h4>AppTest.from_file</h4>

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_string" size="full">

<h4>AppTest.from_string</h4>

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_string(app_script_as_string)
at.run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/st.testing.v1.apptest#apptestfrom_function" size="full">

<h4>AppTest.from_function</h4>

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_function(app_script_as_callable)
at.run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock" size="half">

<h4>Block</h4>

A representation of container elements, including:

- `st.chat_message`
- `st.columns`
- `st.sidebar`
- `st.tabs`
- The main body of the app.

```python
# at.sidebar returns a Block
at.sidebar.button[0].click().run()
assert not at.exception
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeelement" size="half">

<h4>Element</h4>

The base class for representation of all elements, including:

- `st.title`
- `st.header`
- `st.markdown`
- `st.dataframe`

```python
# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton" size="third">

<h4>Button</h4>

A representation of `st.button` and `st.form_submit_button`.

```python
at.button[0].click().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treechatinput" size="third">

<h4>ChatInput</h4>

A representation of `st.chat_input`.

```python
at.chat_input[0].set_value("What is Streamlit?").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecheckbox" size="third">

<h4>Checkbox</h4>

A representation of `st.checkbox`.

```python
at.checkbox[0].check().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecolorpicker" size="third">

<h4>ColorPicker</h4>

A representation of `st.color_picker`.

```python
at.color_picker[0].pick("#FF4B4B").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treedateinput" size="third">

<h4>DateInput</h4>

A representation of `st.date_input`.

```python
release_date = datetime.date(2023, 10, 26)
at.date_input[0].set_value(release_date).run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treemultiselect" size="third">

<h4>Multiselect</h4>

A representation of `st.multiselect`.

```python
at.multiselect[0].select("New York").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treenumberinput" size="third">

<h4>NumberInput</h4>

A representation of `st.number_input`.

```python
at.number_input[0].increment().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeradio" size="third">

<h4>Radio</h4>

A representation of `st.radio`.

```python
at.radio[0].set_value("New York").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectslider" size="third">

<h4>SelectSlider</h4>

A representation of `st.select_slider`.

```python
at.select_slider[0].set_range("A","C").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectbox" size="third">

<h4>Selectbox</h4>

A representation of `st.selectbox`.

```python
at.selectbox[0].select("New York").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeslider" size="third">

<h4>Slider</h4>

A representation of `st.slider`.

```python
at.slider[0].set_range(2,5).run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextarea" size="third">

<h4>TextArea</h4>

A representation of `st.text_area`.

```python
at.text_area[0].input("Streamlit is awesome!").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextinput" size="third">

<h4>TextInput</h4>

A representation of `st.text_input`.

```python
at.text_input[0].input("Streamlit").run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetimeinput" size="third">

<h4>TimeInput</h4>

A representation of `st.time_input`.

```python
at.time_input[0].increment().run()
```

</RefCard>

<RefCard href="/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetoggle" size="third">

<h4>Toggle</h4>

A representation of `st.toggle`.

```python
at.toggle[0].set_value("True").run()
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">

<Image pure alt="screenshot" src="/images/api/components/pandas-profiling.jpg" />

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/jrieke/streamlit-analytics">

<Image pure alt="screenshot" src="/images/api/components/analytics.jpg" />

<h4>Streamlit Analytics</h4>

Track & visualize user interactions with your streamlit app. Created by [@jrieke](https://github.com/jrieke).

```python
import streamlit_analytics

with streamlit_analytics.track():
    st.text_input("Write something")
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/command-line/run.md
```

---

title: streamlit run
slug: /develop/api-reference/cli/run

---

## `$ streamlit run`

### Syntax

```
streamlit run <entrypoint file> [-- config options] [script args]
```

### Arguments

`<entrypoint file>`: The path to your entrypoint file for your Streamlit app. Your entrypoint file is your app's homepage.

### Options

Configuration options are passed in the form of `--<section>.<option>=<value>`. For example, if you want to set the primary color of your app to blue, you could use one of the three equivalent options:

- `--theme.primaryColor=blue`
- `--theme.primaryColor="blue"`
- `--theme.primaryColor=#0000FF`

For a complete list of configuration options, see [`config.toml`](/develop/api-reference/configuration/config.toml) in the API reference. For examples, see below.

### Script arguments

If you need to pass arguments directly to your script, you can pass them as positional arguments. If you use `sys.argv` to read your arguments, `sys.arfgv` returns a list of all arugments and does _not_ include any configuration options. Python interprets all arguments as strings.

- `sys.argv[0]` returns the provided path to your entrypoint file (`<entrypoint file>`).
- `sys.argv[1:]` returns a list of arguments in order and does not include any configuration options.

### Examples

- If your app is in your working directory, run it as follows:

  ```
  streamlit run your_app.py
  ```

- If your app is in a subdirectory, run it as follows:

  ```
  streamlit run your_subdirectory/your_app.py
  ```

- If your app is saved in a public GitHub repo or gist, run it as follows:

  ```
  streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
  ```

- If you need to set one or more configuration options, run it as follows:

  ```
  streamlit run your_app.py --client.showErrorDetails=False --theme.primaryColor=blue
  ```

- If you need to pass an argument to your script, run it as follows:

  ```
  streamlit run your_app.py "my list" of arguments
  ```

  Within your script, the following statement will be true:

  ```
  sys.argv[0] == "your_app.py"
  sys.argv[1] == "my list"
  sys.argv[2] == "of"
  sys.argv[3] == "arguments"
  ```

```

File: api-reference/command-line/_index.md
```

---

title: Command-line options
slug: /develop/api-reference/cli

---

# Command-line interface

When you install Streamlit, a command-line (CLI) tool gets installed
as well. The purpose of this tool is to run Streamlit apps, change Streamlit configuration options,
and help you diagnose and fix issues.

To see all of the supported commands:

```bash
streamlit --help
```

### Run Streamlit apps

```bash
streamlit run your_script.py [-- script args]
```

Runs your app. At any time you can stop the server with **Ctrl+c**.

<Note>

When passing your script some custom arguments, **they must be passed after
two dashes**. Otherwise the arguments get interpreted as arguments to Streamlit
itself.

</Note>

To see the Streamlit 'Hello, World!' example app, run `streamlit hello`.

### View Streamlit version

To see what version of Streamlit is installed, just type:

```bash
streamlit version
```

### View documentation

```bash
streamlit docs
```

Opens the Streamlit documentation (i.e. this website) in a web browser.

### Clear cache

```bash
streamlit cache clear
```

Clears persisted files from the on-disk [Streamlit cache](/develop/api-reference/caching-and-state), if
present.

### View all configuration options

As described in [Configuration](/develop/concepts/configuration), Streamlit has several
configuration options. To view them all, including their current values, just type:

```bash
streamlit config show
```

```

File: api-reference/control-flow/form_submit_button.md
```

---

title: st.form_submit_button
slug: /develop/api-reference/execution-flow/st.form_submit_button
description: st.form_submit_button displays a form submit button.

---

<Autofunction function="streamlit.form_submit_button" />

```

File: api-reference/control-flow/experimental_rerun.md
```

---

title: st.experimental_rerun
slug: /develop/api-reference/execution-flow/st.experimental_rerun
description: st.experimental_rerun will rerun the script immediately.

---

<Autofunction function="streamlit.experimental_rerun" deprecated={true} deprecatedText="<code>st.experimental_rerun</code> was deprecated in version 1.27.0. Use <a href='/develop/api-reference/execution-flow/st.rerun'><code>st.rerun</code></a> instead."/>

```

File: api-reference/control-flow/rerun.md
```

---

title: st.rerun
slug: /develop/api-reference/execution-flow/st.rerun
description: st.rerun will rerun the script immediately.

---

<Autofunction function="streamlit.rerun" oldName="streamlit.experimental_rerun" />

### Caveats for `st.rerun`

`st.rerun` is one of the tools to control the logic of your app. While it is great for prototyping, there can be adverse side effects:

- Additional script runs may be inefficient and slower.
- Excessive reruns may complicate your app's logic and be harder to follow.
- If misused, infinite looping may crash your app.

In many cases where `st.rerun` works, [callbacks](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) may be a cleaner alternative. [Containers](/develop/api-reference/layout) may also be helpful.

### A simple example in three variations

###### Using `st.rerun` to update an earlier header

```python
import streamlit as st

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()
```

###### Using a callback to update an earlier header

```python
##### Option using a callback #####
st.header(st.session_state.value)

def update_value():
    st.session_state.value = "Bar"

st.button("Bar", on_click=update_value)
```

###### Using containers to update an earlier header

```python
##### Option using a container #####
container = st.container()

if st.button("Baz"):
    st.session_state.value = "Baz"

container.header(st.session_state.value)
```

```

File: api-reference/control-flow/fragment.md
```

---

title: st.fragment
slug: /develop/api-reference/execution-flow/st.fragment
description: st.fragment is a decorator that allows a function to rerun independently

---

<Autofunction function="streamlit.experimental_fragment" />

```

File: api-reference/control-flow/_index.md
```

---

title: Execution flow
slug: /develop/api-reference/execution-flow

---

# Execution flow

## Change execution

By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

<TileContainer>

<RefCard href="/develop/api-reference/execution-flow/st.fragment">

<h4>Partial reruns</h4>

Define a fragment to rerun independently from the rest of the script.

```python
@st.experimental_fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

</RefCard>

<RefCard href="/develop/api-reference/execution-flow/st.rerun">

<h4>Rerun script</h4>

Rerun the script immediately.

```python
st.rerun()
```

</RefCard>

<RefCard href="/develop/api-reference/execution-flow/st.stop">

<h4>Stop execution</h4>

Stops execution immediately.

```python
st.stop()
```

</RefCard>

</TileContainer>

## Group multiple widgets

By default, Streamlit reruns your script everytime a user interacts with your app.
However, sometimes it's a better user experience to wait until a group of related
widgets is filled before actually rerunning the script. That's what `st.form` is for!

<TileContainer>
<RefCard href="/develop/api-reference/execution-flow/st.form" size="half">

<h4>Forms</h4>

Create a form that batches elements together with a ΓÇ£Submit" button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

</RefCard>

<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button" size="half">

<h4>Form submit button</h4>

Display a form submit button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

</RefCard>

</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/kmcgrady/streamlit-autorefresh">

<Image pure alt="screenshot" src="/images/api/components/autorefresh.jpg" />

<h4>Autorefresh</h4>

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

</ComponentCard>

<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">

<Image pure alt="screenshot" src="/images/api/components/pydantic.jpg" />

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/st_pages">

<Image pure alt="screenshot" src="/images/api/components/pages.jpg" />

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "≡ƒÅá"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/control-flow/form.md
```

---

title: st.form
slug: /develop/api-reference/execution-flow/st.form
description: st.form creates a form that batches elements together with a ΓÇ£Submit" button.

---

<Tip>

This page only contains information on the `st.forms` API. For a deeper dive into creating and using forms within Streamlit apps, read our guide on [Using forms](/develop/concepts/architecture/forms).

</Tip>

<Autofunction function="streamlit.form" />

```

File: api-reference/control-flow/stop.md
```

---

title: st.stop
slug: /develop/api-reference/execution-flow/st.stop
description: st.stop stops the execution immediately.

---

<Autofunction function="streamlit.stop" />

```

File: api-reference/widgets/button.md
```

---

title: st.button
slug: /develop/api-reference/widgets/st.button
description: st.button displays a button widget.
keywords: button

---

<Autofunction function="streamlit.button" />

### Advanced functionality

Although a button is the simplest of input widgets, it's very common for buttons to be deeply tied to the use of [`st.session_state`](/develop/api-reference/caching-and-state/st.session_state). Check out our advanced guide on [Button behavior and examples](/develop/concepts/design/buttons).

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the button!

<YouTube videoId="JSeQSnGovSE" />

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and [radio button](/develop/api-reference/widgets/st.radio)!

<YouTube videoId="EnXJBsCIl_A" />

```

File: api-reference/widgets/select_slider.md
```

---

title: st.select_slider
slug: /develop/api-reference/widgets/st.select_slider
description: st.select_slider displays a slider widget to select items from a list.

---

<Autofunction function="streamlit.select_slider" />

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the select slider! ≡ƒÄê
<YouTube videoId="MTaL_1UCb2g" />

In the video below, we'll take it a step further and make a double-ended slider.
<YouTube videoId="sCvdt79asrE" />

```

File: api-reference/widgets/radio.md
```

---

title: st.radio
slug: /develop/api-reference/widgets/st.radio
description: st.radio displays a radio button widget.

---

<Autofunction function="streamlit.radio" />

<br />

Widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesnΓÇÖt show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Radio buttons can also be disabled with the `disabled` parameter, and oriented horizontally with the `horizontal` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility ≡ƒæç",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
```

<Cloud src="https://doc-radio1.streamlit.app/?embed=true" height="300" />

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the radio button! ≡ƒöÿ

<YouTube videoId="CVHIMGVAzwA" />

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and radio button!

<YouTube videoId="EnXJBsCIl_A" />

```

File: api-reference/widgets/selectbox.md
```

---

title: st.selectbox
slug: /develop/api-reference/widgets/st.selectbox
description: st.selectbox displays a select widget.

---

<Autofunction function="streamlit.selectbox" />

<br />

Select widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesnΓÇÖt show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Select widgets can also be disabled with the `disabled` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility ≡ƒæë",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
```

<Cloud src="https://doc-selectbox1.streamlit.app/?embed=true" height="300" />

```

File: api-reference/widgets/slider.md
```

---

title: st.slider
slug: /develop/api-reference/widgets/st.slider
description: st.slider displays a slider widget.

---

<Autofunction function="streamlit.slider" />

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the slider!
<YouTube videoId="tzAdd-MuWPw" />

In the video below, we'll take it a step further and make a double-ended slider.
<YouTube videoId="sCvdt79asrE" />

```

File: api-reference/widgets/page_link.md
```

---

title: st.page_link
slug: /develop/api-reference/widgets/st.page_link
description: st.page_link displays a link to another page in a multipage app or to an external page.

---

<Tip>

Check out our [tutorial](/develop/tutorials/multipage/st.page_link-nav) to learn about building custom, dynamic menus with `st.page_link`.

</Tip>

<Autofunction function="streamlit.page_link" />

```

File: api-reference/widgets/text_input.md
```

---

title: st.text_input
slug: /develop/api-reference/widgets/st.text_input
description: st.text_input displays a single-line text input widget.

---

<Autofunction function="streamlit.text_input" />

<br />

Text input widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesnΓÇÖt show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Text input widgets can also be disabled with the `disabled` parameter, and can display an optional placeholder text when the text input is empty using the `placeholder` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility ≡ƒæë",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text ≡ƒæç",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)
```

<Cloud src="https://doc-text-input1.streamlit.app/?embed=true" height="400" />

```

File: api-reference/widgets/download_button.md
```

---

title: st.download_button
slug: /develop/api-reference/widgets/st.download_button
description: st.download_button displays a download button widget.

---

<Autofunction function="streamlit.download_button" />

```

File: api-reference/widgets/camera_input.md
```

---

title: st.camera_input
slug: /develop/api-reference/widgets/st.camera_input
description: st.camera_input displays a widget to upload images from a camera

---

<Autofunction function="streamlit.camera_input" />

To read the image file buffer as bytes, you can use `getvalue()` on the `UploadedFile` object.

```python
import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
```

<Important>

`st.camera_input` returns an object of the `UploadedFile` class, which a subclass of BytesIO. Therefore it is a "file-like" object. This means you can pass it anywhere where a file is expected, similar to `st.file_uploader`.

</Important>

## Image processing examples

You can use the output of `st.camera_input` for various downstream tasks, including image processing. Below, we demonstrate how to use the `st.camera_input` widget with popular image and data processing libraries such as [Pillow](https://pillow.readthedocs.io/en/stable/installation.html), [NumPy](https://numpy.org/), [OpenCV](https://pypi.org/project/opencv-python-headless/), [TensorFlow](https://www.tensorflow.org/), [torchvision](https://pytorch.org/vision/stable/index.html), and [PyTorch](https://pytorch.org/).

While we provide examples for the most popular use-cases and libraries, you are welcome to adapt these examples to your own needs and favorite libraries.

### Pillow (PIL) and NumPy

Ensure you have installed [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) and [NumPy](https://numpy.org/).

To read the image file buffer as a PIL Image and convert it to a NumPy array:

```python
import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
```

### OpenCV (cv2)

Ensure you have installed [OpenCV](https://pypi.org/project/opencv-python-headless/) and [NumPy](https://numpy.org/).

To read the image file buffer with OpenCV:

```python
import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
```

### TensorFlow

Ensure you have installed [TensorFlow](https://www.tensorflow.org/install/).

To read the image file buffer as a 3 dimensional uint8 tensor with TensorFlow:

```python
import streamlit as st
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)
```

### Torchvision

Ensure you have installed [Torchvision](https://pypi.org/project/torchvision/) (it is not bundled with PyTorch) and [PyTorch](https://pytorch.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with `torchvision.io`:

```python
import streamlit as st
import torch
import torchvision

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with `torchvision.io`:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torchvision.io.decode_image(
        torch.frombuffer(bytes_data, dtype=torch.uint8)
    )

    # Check the type of torch_img:
    # Should output: <class 'torch.Tensor'>
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```

### PyTorch

Ensure you have installed [PyTorch](https://pytorch.org/) and [NumPy](https://numpy.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with PyTorch:

```python
import streamlit as st
import torch
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with PyTorch:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torch.ops.image.decode_image(
        torch.from_numpy(np.frombuffer(bytes_data, np.uint8)), 3
    )

    # Check the type of torch_img:
    # Should output: <class 'torch.Tensor'>
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```

```

File: api-reference/widgets/link_button.md
```

---

title: st.link_button
slug: /develop/api-reference/widgets/st.link_button

---

<Autofunction function="streamlit.link_button" />

```

File: api-reference/widgets/multiselect.md
```

---

title: st.multiselect
slug: /develop/api-reference/widgets/st.multiselect
description: st.multiselect displays a multiselect widget. The multiselect widget starts as empty.

---

<Autofunction function="streamlit.multiselect" />

```

File: api-reference/widgets/toggle.md
```

---

title: st.toggle
slug: /develop/api-reference/widgets/st.toggle
description: st.toggle displays a toggle widget.

---

<Autofunction function="streamlit.toggle" />

```

File: api-reference/widgets/number_input.md
```

---

title: st.number_input
slug: /develop/api-reference/widgets/st.number_input
description: st.number_input displays a numeric input widget.

---

<Autofunction function="streamlit.number_input" />

```

File: api-reference/widgets/color_picker.md
```

---

title: st.color_picker
slug: /develop/api-reference/widgets/st.color_picker
description: st.color_picker displays a color picker widget.

---

<Autofunction function="streamlit.color_picker" />

```

File: api-reference/widgets/text_area.md
```

---

title: st.text_area
slug: /develop/api-reference/widgets/st.text_area
description: st.text_area displays a multi-line text input widget.

---

<Autofunction function="streamlit.text_area" />

```

File: api-reference/widgets/checkbox.md
```

---

title: st.checkbox
slug: /develop/api-reference/widgets/st.checkbox
description: st.checkbox displays a checkbox widget.

---

<Autofunction function="streamlit.checkbox" />

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the checkbox! Γÿæ

<YouTube videoId="Jte0Reue7z8" />

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and [radio button](/develop/api-reference/widgets/st.radio)!

<YouTube videoId="EnXJBsCIl_A" />

```

File: api-reference/widgets/_index.md
```

---

title: Input widgets
slug: /develop/api-reference/widgets

---

# Input widgets

With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.

## Button elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.button">

<Image pure alt="screenshot" src="/images/api/button.svg" />

<h4>Button</h4>

Display a button widget.

```python
clicked = st.button("Click me")
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.download_button">

<Image pure alt="screenshot" src="/images/api/download_button.svg" />

<h4>Download button</h4>

Display a download button widget.

```python
st.download_button("Download file", file)
```

</RefCard>

<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button">

<Image pure alt="screenshot" src="/images/api/form_submit_button.svg" />

<h4>Form button</h4>

Display a form submit button. For use with `st.form`.

```python
st.form_submit_button("Sign up")
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.link_button">

<Image pure alt="screenshot" src="/images/api/link_button.svg" />

<h4>Link button</h4>

Display a link button.

```python
st.link_button("Go to gallery", url)
```

</RefCard>

<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="≡ƒÅá")
st.page_link("pages/profile.py", label="My profile")
```

</RefCard>

</TileContainer>

## Selection elements

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.checkbox">

<Image pure alt="screenshot" src="/images/api/checkbox.jpg" />

<h4>Checkbox</h4>

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.toggle">

<Image pure alt="screenshot" src="/images/api/toggle.jpg" />

<h4>Toggle</h4>

Display a toggle widget.

```python
activated = st.toggle("Activate")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.radio">

<Image pure alt="screenshot" src="/images/api/radio.jpg" />

<h4>Radio</h4>

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.selectbox">

<Image pure alt="screenshot" src="/images/api/selectbox.jpg" />

<h4>Selectbox</h4>

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.multiselect">

<Image pure alt="screenshot" src="/images/api/multiselect.jpg" />

<h4>Multiselect</h4>

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.select_slider">

<Image pure alt="screenshot" src="/images/api/select_slider.jpg" />

<h4>Select slider</h4>

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.color_picker">

<Image pure alt="screenshot" src="/images/api/color_picker.jpg" />

<h4>Color picker</h4>

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

</RefCard>

</TileContainer>

## Numeric input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.number_input">

<Image pure alt="screenshot" src="/images/api/number_input.jpg" />

<h4>Number input</h4>

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.slider">

<Image pure alt="screenshot" src="/images/api/slider.jpg" />

<h4>Slider</h4>

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```

</RefCard>

</TileContainer>

## Date and time input elements

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.date_input">

<Image pure alt="screenshot" src="/images/api/date_input.jpg" />

<h4>Date input</h4>

Display a date input widget.

```python
date = st.date_input("Your birthday")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.time_input">

<Image pure alt="screenshot" src="/images/api/time_input.jpg" />

<h4>Time input</h4>

Display a time input widget.

```python
time = st.time_input("Meeting time")
```

</RefCard>

</TileContainer>

## Text input elements

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.text_input">

<Image pure alt="screenshot" src="/images/api/text_input.jpg" />

<h4>Text input</h4>

Display a single-line text input widget.

```python
name = st.text_input("First name")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_area">

<Image pure alt="screenshot" src="/images/api/text_area.jpg" />

<h4>Text area</h4>

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>

</TileContainer>

## Other input elements

<TileContainer>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.experimental_data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.file_uploader">

<Image pure alt="screenshot" src="/images/api/file_uploader.jpg" />

<h4>File uploader</h4>

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```

</RefCard>
<RefCard href="/develop/api-reference/widgets/st.camera_input">

<Image pure alt="screenshot" src="/images/api/camera_input.jpg" />

<h4>Camera input</h4>

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/okld/streamlit-elements">

<Image pure alt="screenshot" src="/images/api/components/elements.jpg" />

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">

<Image pure alt="screenshot" src="/images/api/components/timeline.jpg" />

<h4>Timeline</h4>

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">

<Image pure alt="screenshot" src="/images/api/components/camera-live.jpg" />

<h4>Camera input live</h4>

Alternative for st.camera_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-ace">

<Image pure alt="screenshot" src="/images/api/components/ace.jpg" />

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</ComponentCard>

<ComponentCard href="https://github.com/AI-Yash/st-chat">

<Image pure alt="screenshot" src="/images/api/components/chat.jpg" />

<h4>Streamlit Chat</h4>

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

</ComponentCard>

<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">

<Image pure alt="screenshot" src="/images/api/components/option-menu.jpg" />

<h4>Streamlit Option Menu</h4>

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-toggle.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """≡ƒÑ╖ Surprise! Here's some additional content""",)
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/widgets/date_input.md
```

---

title: st.date_input
slug: /develop/api-reference/widgets/st.date_input
description: st.date_input displays a date input widget.

---

<Autofunction function="streamlit.date_input" />

```

File: api-reference/widgets/time_input.md
```

---

title: st.time_input
slug: /develop/api-reference/widgets/st.time_input
description: st.time_input displays a time input widget.

---

<Autofunction function="streamlit.time_input" />

```

File: api-reference/widgets/file_uploader.md
```

---

title: st.file_uploader
slug: /develop/api-reference/widgets/st.file_uploader
description: st.file_uploader displays a file uploader widget.

---

<Autofunction function="streamlit.file_uploader" />

```

File: api-reference/text/echo.md
```

---

title: st.echo
slug: /develop/api-reference/text/st.echo
description: st.echo displays some code on the app, then execute it. Useful for tutorials.

---

<Autofunction function="streamlit.echo" />

### Display code

Sometimes you want your Streamlit app to contain _both_ your usual
Streamlit graphic elements _and_ the code that generated those elements.
That's where `st.echo()` comes in.

Ok so let's say you have the following file, and you want to make its
app a little bit more self-explanatory by making that middle section
visible in the Streamlit app:

```python
import streamlit as st

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')
```

The file above creates a Streamlit app containing the words "Hi there,
`John`", and then "Done!".

Now let's use `st.echo()` to make that middle section of the code visible
in the app:

```python
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
```

It's _that_ simple!

<Note>

You can have multiple `st.echo()` blocks in the same file.
Use it as often as you wish!

</Note>

```

File: api-reference/text/markdown.md
```

---

title: st.markdown
slug: /develop/api-reference/text/st.markdown
description: st.markdown displays string formatted as Markdown.

---

<Autofunction function="streamlit.markdown" />

```python
import streamlit as st

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)
```

<Cloud src="https://doc-markdown1.streamlit.app/?embed=true" height="500" />

```

File: api-reference/text/caption.md
```

---

title: st.caption
slug: /develop/api-reference/text/st.caption
description: st.caption displays text in small font.

---

<Autofunction function="streamlit.caption" />

<Image src="/images/api/st.caption.png" clean />

```

File: api-reference/text/header.md
```

---

title: st.header
slug: /develop/api-reference/text/st.header
description: st.header displays text in header formatting.

---

<Autofunction function="streamlit.header" />

```

File: api-reference/text/subheader.md
```

---

title: st.subheader
slug: /develop/api-reference/text/st.subheader
description: st.subheader displays text in subheader formatting.

---

<Autofunction function="streamlit.subheader" />

```

File: api-reference/text/divider.md
```

---

title: st.divider
slug: /develop/api-reference/text/st.divider
description: st.divider displays a horizontal rule in your app.

---

<Autofunction function="streamlit.divider" />

Here's what it looks like in action when you have multiple elements in the app:

```python
import streamlit as st

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # ≡ƒæê Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # ≡ƒæê Another horizontal rule
```

<Image src="/images/api/st.divider.png" clean />

```

File: api-reference/text/_index.md
```

---

title: Text elements
slug: /develop/api-reference/text

---

# Text elements

Streamlit apps usually start with a call to `st.title` to set the
app's title. After that, there are 2 heading levels you can use:
`st.header` and `st.subheader`.

Pure text is entered with `st.text`, and Markdown with
`st.markdown`.

We also offer a "swiss-army knife" command called `st.write`, which accepts
multiple arguments, and multiple data types. And as described above, you can
also use [magic commands](/develop/api-reference/write-magic/magic) in place of `st.write`.

## Headings and body text

<TileContainer>
<RefCard href="/develop/api-reference/text/st.markdown">

<Image pure alt="screenshot" src="/images/api/markdown.jpg" />

<h4>Markdown</h4>

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.title">

<Image pure alt="screenshot" src="/images/api/title.jpg" />

<h4>Title</h4>

Display text in title formatting.

```python
st.title("The app title")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.header">

<Image pure alt="screenshot" src="/images/api/header.jpg" />

<h4>Header</h4>

Display text in header formatting.

```python
st.header("This is a header")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.subheader">

<Image pure alt="screenshot" src="/images/api/subheader.jpg" />

<h4>Subheader</h4>

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

</RefCard>
</TileContainer>

## Formatted text

<TileContainer>

<RefCard href="/develop/api-reference/text/st.caption">

<Image pure alt="screenshot" src="/images/api/caption.jpg" />

<h4>Caption</h4>

Display text in small font.

```python
st.caption("This is written small caption text")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.code">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

<h4>Code block</h4>

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.echo">

<Image pure alt="screenshot" src="/images/api/code.jpg" />

<h4>Echo</h4>

Display some code on the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.text">

<Image pure alt="screenshot" src="/images/api/text.jpg" />

<h4>Preformatted text</h4>

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.latex">

<Image pure alt="screenshot" src="/images/api/latex.jpg" />

<h4>LaTeX</h4>

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.divider">

<Image pure alt="screenshot" src="/images/api/divider.jpg" />

<h4>Divider</h4>

Display a horizontal rule.

```python
st.divider()
```

</RefCard>
</TileContainer>

<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">

<Image pure alt="screenshot" src="/images/api/components/annotated-text.jpg" />

<h4>Annotated text</h4>

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/gagan3012/streamlit-tags">

<Image pure alt="screenshot" src="/images/api/components/tags.jpg" />

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</ComponentCard>

<ComponentCard href="https://github.com/JohnSnowLabs/nlu">

<Image pure alt="screenshot" src="/images/api/components/nlu.jpg" />

<h4>NLU</h4>

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! <3')
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-mentions.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
mention(label="An awesome Streamlit App", icon="streamlit",  url="https://extras.streamlit.app",)
```

</ComponentCard>
</ComponentSlider>

```

File: api-reference/text/latex.md
```

---

title: st.latex
slug: /develop/api-reference/text/st.latex
description: st.latex displays mathematical expressions formatted as LaTeX.

---

<Autofunction function="streamlit.latex" />

<Image src="/images/api/st.latex.png" clean />

```

File: api-reference/text/text.md
```

---

title: st.text
slug: /develop/api-reference/text/st.text
description: st.text writes fixed-width and preformatted text.

---

<Autofunction function="streamlit.text" />

<Image src="/images/api/st.text.png" clean />

```

File: api-reference/text/title.md
```

---

title: st.title
slug: /develop/api-reference/text/st.title
description: st.title displays text in title formatting.

---

<Autofunction function="streamlit.title" />

```

File: api-reference/text/code.md
```

---

title: st.code
slug: /develop/api-reference/text/st.code
description: st.code displays a code block with optional syntax highlighting.

---

<Autofunction function="streamlit.code" />

<Image src="/images/api/st.code.png" clean />

```

File: api-reference/chat/chat-input.md
```

---

title: st.chat_input
slug: /develop/api-reference/chat/st.chat_input
description: st.chat_input displays a chat input widget.

---

<Tip>

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

</Tip>

<Autofunction function="streamlit.chat_input" />

For an overview of the `st.chat_input` and `st.chat_message` API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

<YouTube videoId="4sPnOqeUDmk" />

```

File: api-reference/chat/chat-message.md
```

---

title: st.chat_message
slug: /develop/api-reference/chat/st.chat_message
description: st.chat_message inserts a chat message container into the app.

---

<Tip>

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

</Tip>

<Autofunction function="streamlit.chat_message" />

For an overview of the `st.chat_message` and `st.chat_input` API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

<YouTube videoId="4sPnOqeUDmk" />

```

File: api-reference/chat/_index.md
```

---

title: Chat elements
slug: /develop/api-reference/chat

---

# Chat elements

Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message. Remember to check out `st.status` to display output from long-running processes and external API calls.

<TileContainer>
<RefCard href="/develop/api-reference/chat/st.chat_input">

<Image pure alt="screenshot" src="/images/api/chat_input.jpg" />

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

</RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_message">

<Image pure alt="screenshot" src="/images/api/chat_message.jpg" />

<h4>Chat message</h4>

Insert a chat message container.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello ≡ƒæï")
    st.line_chart(np.random.randn(30, 3))
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.status">

<Image pure alt="screenshot" src="/images/api/status.jpg" />

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
</TileContainer>

```

File: api-reference/connections/connections-sql.md
```

---

title: st.connections.SQLConnection
slug: /develop/api-reference/connections/st.connections.sqlconnection

---

<Tip>

This page only contains the `st.connections.SQLConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.SQLConnection" />

### Basic usage:

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) and any required drivers must be installed to use this connection.

```python
import streamlit as st

conn = st.connection("sql")
df = conn.query("select * from pet_owners")
st.dataframe(df)
```

In case you want to pass a connection URL (or other parameters) directly, it also works:

```python
conn = st.connection(
    "local_db",
    type="sql",
    url="mysql://user:pass@localhost:3306/mydb"
)
```

Or specify parameters in [secrets](/develop/concepts/connections/secrets-management):

```toml
# .streamlit/secrets.toml
[connections.mydb]
dialect = "mysql"
username = "myuser"
password = "password"
host = "localhost"
database = "mydb"
```

```python
# streamlit_app.py
conn = st.connection("mydb", type="sql", autocommit=True)
```

As described above, some cloud databases use extra `**kwargs` to specify credentials. These can be passed via secrets using the `create_engine_kwargs` section:

```toml
# .streamlit/secrets.toml
[connections.snowflake]
url = "snowflake://<username>@<account>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
role = "..."
# ...
```

<Autofunction function="streamlit.connections.SQLConnection.connect" />

<Autofunction function="streamlit.connections.SQLConnection.query" />

<Autofunction function="streamlit.connections.SQLConnection.reset" />

<Autofunction function="streamlit.connections.SQLConnection.driver" />

<Autofunction function="streamlit.connections.SQLConnection.engine" />

<Autofunction function="streamlit.connections.SQLConnection.session" />

```

File: api-reference/connections/connections-snowflake.md
```

---

title: st.connections.SnowflakeConnection
slug: /develop/api-reference/connections/st.connections.snowflakeconnection

---

<Tip>

This page only contains the `st.connections.SnowflakeConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.SnowflakeConnection" />

### Configuration

{/**
Internal note: This section is deep-linked from the library in 1.28.1 via /st.connections.snowflakeconnection-configuration through a redirect.
Maintain the redirect if moved or modified.
**/}

`st.connection("snowflake")` can be configured using [Streamlit secrets](/develop/concepts/connections/secrets-management) or keyword args just like any other connection. It can also use existing Snowflake connection configuration when available.

Note that [snowflake-snowpark-python](https://pypi.org/project/snowflake-snowpark-python/) must be installed to use this connection.

#### Using Streamlit secrets

For example, if your Snowflake account supports SSO, you can set up a quick local connection for development using [browser-based SSO](https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use#how-browser-based-sso-works) and `secrets.toml` as follows:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
account = "<ACCOUNT ID>"
user = "<USERNAME>"
authenticator = "EXTERNALBROWSER"
```

Learn more about [account indentifier here](https://docs.snowflake.com/en/user-guide/admin-account-identifier). You could also specify the full configuration and credentials in your secrets file, as in the [example here](/develop/tutorials/databases/snowflake#add-connection-parameters-to-your-local-app-secrets).

#### Using existing Snowflake configuration

Snowflake's python driver also supports a [connection configuration file](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#connecting-using-the-connections-toml-file), which is well integrated with Streamlit `SnowflakeConnection`. If you already have one or more connections configured, all you need to do is pass Streamlit the name of the connection to use. This can be done in several ways:

- Set `connection_name` in your app code, such as `st.connnection("<name>", type="snowflake")`.
- Set `connection_name = "<name>"` in the `[connections.snowflake]` section of your Streamlit secrets.
- Set the environment variable `SNOWFLAKE_DEFAULT_CONNECTION_NAME=<name>`.
- [Set a default connection](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-example#setting-a-default-connection) in your Snowflake configuration.

When available in [Streamlit in Snowflake](https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit), `st.connection("snowflake")` will connect automatically using the [app owner role](https://docs.snowflake.com/en/developer-guide/streamlit/owners-rights) and does not require any configuration.

Learn more about setting up connections in the [Connecting Streamlit to Snowflake tutorial](/develop/tutorials/databases/snowflake) and [Connecting to data](/develop/concepts/connections/connecting-to-data).

<Autofunction function="streamlit.connections.SnowflakeConnection.cursor" />

<Autofunction function="streamlit.connections.SnowflakeConnection.query" />

<Autofunction function="streamlit.connections.SnowflakeConnection.raw_connection" />

<Autofunction function="streamlit.connections.SnowflakeConnection.reset" />

<Autofunction function="streamlit.connections.SnowflakeConnection.session" />

<Autofunction function="streamlit.connections.SnowflakeConnection.write_pandas" />

```

File: api-reference/connections/secrets-toml.md
```

---

title: secrets.toml
slug: /develop/api-reference/connections/secrets.toml

---

## secrets.toml

`secrets.toml` is an optional file you can define for your working directory or global development environment. When `secrets.toml` is defined both globally and in your working directory, Streamlit combines the secrets and gives precendence to the working-directory secrets. For more information, see [Secrets management](/develop/concepts/connections/secrets-management).

### File location

To define your secrets locally or per-project, add `.streamlit/secrets.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linx, this will be `~/.streamlit/secrets.toml`. For Windows, this will be `%userprofile%/.streamlit/secrets.toml`.

### File format

`secrets.toml` is a [TOML](https://toml.io/en/) file.

#### Example

```toml
OpenAI_key = "your OpenAI key"
whitelist = ["sally", "bob", "joe"]

[database]
user = "your username"
password = "your password"
```

In your Streamlit app, the following values would be true:

```python
st.secrets["OpenAI_key"] == "your OpenAI key"
"sally" in st.secrets.whitelist
st.secrets["database"]["user"] == "your username"
st.secrets.database.password == "your password"
```

```

File: api-reference/connections/secrets.md
```

---

title: st.secrets
slug: /develop/api-reference/connections/st.secrets

---

## st.secrets

`st.secrets` provides a dictionary-like interface to access secrets stored in a `secrets.toml` file. It behaves similarly to `st.session_state`. `st.secrets` can be used with both key and attribute notation. For example, `st.secrets.your_key` and `st.secrets["your_key"]` refer to the same value. For more information about using `st.secrets`, see [Secrets management](/develop/concepts/connections/secrets-management).

### secrets.toml

Secrets can be saved globally or per-project. When both types of secrets are saved, Streamlit will combine the saved values but give precedence to per-project secrets if there are duplicate keys. For information on how to format and locate your `secrets.toml` file for your development environment, see [`secrets.toml`](/develop/api-reference/connections/secrets.toml).

#### Example

```toml
OpenAI_key = "your OpenAI key"
whitelist = ["sally", "bob", "joe"]

[database]
user = "your username"
password = "your password"
```

In your Streamlit app, the following values would be true:

```python
st.secrets["OpenAI_key"] == "your OpenAI key"
"sally" in st.secrets.whitelist
st.secrets["database"]["user"] == "your username"
st.secrets.database.password == "your password"
```

```

File: api-reference/connections/connections-baseconnection.md
```

---

title: st.connections.BaseConnection
slug: /develop/api-reference/connections/st.connections.baseconnection

---

<Tip>

This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.BaseConnection" oldName="streamlit.connections.ExperimentalBaseConnection" />

<Autofunction function="streamlit.connections.BaseConnection.reset" oldName="streamlit.connections.ExperimentalBaseConnection.reset" />

```

File: api-reference/connections/connections-snowpark.md
```

---

title: st.connections.SnowparkConnection
slug: /develop/api-reference/connections/st.connections.snowparkconnection

---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Tip>

This page only contains the `st.connections.SnowparkConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.SnowparkConnection" deprecated={true} deprecatedText="<code>st.connections.SnowParkConnection</code> was deprecated in version 1.28.0. Use <a href='/develop/api-reference/connections/st.connections.snowflakeconnection'><code>st.connections.SnowflakeConnection</code></a> instead." />

<Autofunction function="streamlit.connections.SnowparkConnection.query" />

<Autofunction function="streamlit.connections.SnowparkConnection.reset" />

<Autofunction function="streamlit.connections.SnowparkConnection.safe_session" />

<Autofunction function="streamlit.connections.SnowparkConnection.session" />

```

File: api-reference/connections/connections-experimentalbaseconnection.md
```

---

title: st.connections.ExperimentalBaseConnection
slug: /develop/api-reference/connections/st.connections.experimentalbaseconnection

---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Tip>

This page only contains information on the `st.connections.ExperimentalBaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connections.ExperimentalBaseConnection" deprecated={true} deprecatedText="<code>st.connections.ExperimentalBaseConnection</code> was deprecated in version 1.28.0. Use <a href='/develop/api-reference/connections/st.connections.baseconnection'><code>st.connections.BaseConnection</code></a> instead." />

<Autofunction function="streamlit.connections.ExperimentalBaseConnection.reset" />

```

File: api-reference/connections/connection.md
```

---

title: st.connection
slug: /develop/api-reference/connections/st.connection

---

<Tip>

This page only contains the `st.connection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.connection" oldName="streamlit.experimental_connection" />

For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

<YouTube videoId="xQwDfW7UHMo" />

```

File: api-reference/connections/experimental-connection.md
```

---

title: st.experimental_connection
slug: /develop/api-reference/connections/st.experimental_connection

---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Tip>

This page only contains the `st.experimental_connection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

</Tip>

<Autofunction function="streamlit.experimental_connection" deprecated={true} deprecatedText="<code>st.experimental_connection</code> was deprecated in version 1.28.0. Use <a href='/develop/api-reference/connections/st.connection'><code>st.connection</code></a> instead."/>

For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

<YouTube videoId="xQwDfW7UHMo" />

```

File: api-reference/connections/_index.md
```

---

title: Connections and databases
slug: /develop/api-reference/connections

---

# Connections and databases

## Setup your connection

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connection" size="half">

<Image pure alt="screenshot" src="/images/api/connection.svg" />

<h4>Create a connection</h4>

Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

</RefCard>
</TileContainer>

## Built-in connections

<TileContainer>

<RefCard href="/develop/api-reference/connections/st.connections.snowflakeconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SnowflakeConnection.svg" />

<h4>SnowflakeConnection</h4>

A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

</RefCard>

<RefCard href="/develop/api-reference/connections/st.connections.sqlconnection" size="half">

<Image pure alt="screenshot" src="/images/api/connections.SQLConnection.svg" />

<h4>SQLConnection</h4>

A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

</RefCard>
</TileContainer>

## Third-party connections

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.baseconnection" size="half">

<h4>Connection base class</h4>

Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

</RefCard>

</TileContainer>

## Secrets

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.secrets" size="half">

<h4>Secrets singleton</h4>

Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

</RefCard>
<RefCard href="/develop/api-reference/connections/secrets.toml" size="half">

<h4>Secrets file</h4>

Save your secrets in a per-project or per-profile TOML file.

```python
OpenAI_key = "<YOUR_SECRET_KEY>"
```

</RefCard>

</TileContainer>

## Deprecated classes

<TileContainer>
<RefCard href="/develop/api-reference/connections/st.connections.snowparkconnection" size="half" deprecated={true}>

<h4>SnowparkConnection</h4>

A connection to Snowflake.

```python
conn = st.connection("snowpark")
```

</RefCard>

</TileContainer>

```

File: api-reference/write-magic/write_stream.md
```

---

title: st.write_stream
slug: /develop/api-reference/write-magic/st.write_stream
description: st.write_stream writes arguments to the app using a typewriter effect.

---

<Autofunction function="streamlit.write_stream" />

```

File: api-reference/write-magic/write.md
```

---

title: st.write
slug: /develop/api-reference/write-magic/st.write
description: st.write writes arguments to the app.

---

<Autofunction function="streamlit.write" />

### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

<YouTube videoId="wpDuY9I2fDg" />

```

File: api-reference/write-magic/magic.md
```

---

title: Magic
slug: /develop/api-reference/write-magic/magic

---

## Magic

Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data,
charts) without having to type an explicit command at all. Just put the thing you want to show on
its own line of code, and it will appear in your app. Here's an example:

```python
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # ≡ƒæê Draw the dataframe

x = 10
'x', x  # ≡ƒæê Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # ≡ƒæê Draw a Matplotlib chart
```

### How Magic works

Any time Streamlit sees either a variable or literal
value on its own line, it automatically writes that to your app using
[`st.write`](/develop/api-reference/write-magic/st.write) (which you'll learn about later).

Also, magic is smart enough to ignore docstrings. That is, it ignores the
strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn
magic off in your `~/.streamlit/config.toml` with the following setting:

```toml
[runner]
magicEnabled = false
```

<Important>
    <p>Right now, Magic only works in the main Python app file, not in imported files. See GitHub issue #288 for a discussion of the issues.</p>
</Important>

### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

<YouTube videoId="wpDuY9I2fDg" />

```

File: api-reference/write-magic/_index.md
```

---

title: st.write and magic commands
slug: /develop/api-reference/write-magic

---

# st.write and magic commands

Streamlit has two easy ways to display information into your app, which should typically be the
first thing you try: `st.write` and magic.

<TileContainer>
<RefCard href="/develop/api-reference/write-magic/st.write">

<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">

<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">

<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>

```

File: api-reference/status/warning.md
```

---

title: st.warning
slug: /develop/api-reference/status/st.warning
description: st.warning displays warning message.

---

<Autofunction function="streamlit.warning" />

```

File: api-reference/status/progress.md
```

---

title: st.progress
slug: /develop/api-reference/status/st.progress
description: st.progress displays a progress bar.

---

<Autofunction function="streamlit.progress" />

```

File: api-reference/status/snow.md
```

---

title: st.snow
slug: /develop/api-reference/status/st.snow
description: st.snow displays celebratory snowflakes!

---

<Autofunction function="streamlit.snow" />

```

File: api-reference/status/exception.md
```

---

title: st.exception
slug: /develop/api-reference/status/st.exception
description: st.exception displays an exception.

---

<Autofunction function="streamlit.exception" />

```

File: api-reference/status/error.md
```

---

title: st.error
slug: /develop/api-reference/status/st.error
description: st.error displays error message.

---

<Autofunction function="streamlit.error" />

```

File: api-reference/status/spinner.md
```

---

title: st.spinner
slug: /develop/api-reference/status/st.spinner
description: st.spinner temporarily displays a message while executing a block of code.

---

<Autofunction function="streamlit.spinner" />

```

File: api-reference/status/success.md
```

---

title: st.success
slug: /develop/api-reference/status/st.success
description: st.success displays a success message.

---

<Autofunction function="streamlit.success" />

```

File: api-reference/status/toast.md
```

---

title: st.toast
slug: /develop/api-reference/status/st.toast
description: st.toast briefly displays a toast message in the bottom-right corner

---

<Autofunction function="streamlit.toast" />

When multiple toasts are generated, they will stack. Hovering over a toast will
stop it from disappearing. When hovering ends, the toast will disappear after
four more seconds.

```python
import streamlit as st
import time

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='≡ƒÄë')
```

<Cloud src="https://doc-status-toast1.streamlit.app/?embed=true" height="300" />

Toast messages can also be updated. Assign `st.toast(my_message)` to a variable
and use the `.toast()` method to update it. Note: if a toast has already disappeared
or been dismissed, the update will not be seen.

```python
import streamlit as st
import time

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "≡ƒÑ₧")

if st.button('Cook breakfast'):
    cook_breakfast()
```

<Cloud src="https://doc-status-toast2.streamlit.app/?embed=true" height="200" />

```

File: api-reference/status/_index.md
```

---

title: Display progress and status
slug: /develop/api-reference/status

---

# Display progress and status

Streamlit provides a few methods that allow you to add animation to your
apps. These animations include progress bars, status messages (like
warnings), and celebratory balloons.

## Animated status elements

<TileContainer>
<RefCard href="/develop/api-reference/status/st.progress">

<Image pure alt="screenshot" src="/images/api/progress.jpg" />

<h4>Progress bar</h4>

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.spinner">

<Image pure alt="screenshot" src="/images/api/spinner.jpg" />

<h4>Spinner</h4>

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.status">

<Image pure alt="screenshot" src="/images/api/status.jpg" />

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.toast">

<Image pure alt="screenshot" src="/images/api/toast.jpg" />

<h4>Toast</h4>

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='≡ƒºê')
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.balloons">

<Image pure alt="screenshot" src="/images/api/balloons.jpg" />

<h4>Balloons</h4>

Display celebratory balloons!

```python
st.balloons()
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.snow">

<Image pure alt="screenshot" src="/images/api/snow.jpg" />

<h4>Snowflakes</h4>

Display celebratory snowflakes!

```python
st.snow()
```

</RefCard>
</TileContainer>

## Simple callout messages

<TileContainer>
<RefCard href="/develop/api-reference/status/st.success">

<Image pure alt="screenshot" src="/images/api/success.jpg" />

<h4>Success box</h4>

Display a success message.

```python
st.success("Match found!")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.info">

<Image pure alt="screenshot" src="/images/api/info.jpg" />

<h4>Info box</h4>

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.warning">

<Image pure alt="screenshot" src="/images/api/warning.jpg" />

<h4>Warning box</h4>

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.error">

<Image pure alt="screenshot" src="/images/api/error.jpg" />

<h4>Error box</h4>

Display error message.

```python
st.error("We encountered an error")
```

</RefCard>
<RefCard href="/develop/api-reference/status/st.exception">

<Image pure alt="screenshot" src="/images/api/exception.jpg" />

<h4>Exception output</h4>

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/Wirg/stqdm">

<Image pure alt="screenshot" src="/images/api/components/stqdm.jpg" />

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```

</ComponentCard>

<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">

<Image pure alt="screenshot" src="/images/api/components/custom-notification-box.jpg" />

<h4>Custom notification box</h4>

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-emojis.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="≡ƒÄê", font_size=54,
  falling_speed=5, animation_length="infinite",)
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/status/info.md
```

---

title: st.info
slug: /develop/api-reference/status/st.info
description: st.info displays an informational message.

---

<Autofunction function="streamlit.info" />

```

File: api-reference/status/status.md
```

---

title: st.status
slug: /develop/api-reference/status/st.status
description: st.status inserts a mutable expander element

---

<Autofunction function="streamlit.status" />

<Autofunction function="StatusContainer.update" />

```

File: api-reference/status/balloons.md
```

---

title: st.balloons
slug: /develop/api-reference/status/st.balloons
description: st.balloons displays celebratory balloons!

---

<Autofunction function="streamlit.balloons" />

```

File: api-reference/navigation/_index.md
```

---

title: Navigation and pages
slug: /develop/api-reference/navigation

---

# Navigation and pages

<TileContainer>

<RefCard href="/develop/api-reference/widgets/st.page_link">

<Image pure alt="screenshot" src="/images/api/page_link.jpg" />

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="≡ƒÅá")
st.page_link("pages/profile.py", label="Profile")
```

</RefCard>

<RefCard href="/develop/api-reference/navigation/st.switch_page">

<h4>Switch page</h4>

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

</RefCard>

</TileContainer>

```

File: api-reference/navigation/switch_page.md
```

---

title: st.switch_page
slug: /develop/api-reference/navigation/st.switch_page
description: st.switch_page programmatically switches the active page.

---

<Autofunction function="streamlit.switch_page" />

```

File: api-reference/media/video.md
```

---

title: st.video
slug: /develop/api-reference/media/st.video
description: st.video displays a video player.

---

<Autofunction function="streamlit.video" />

```

File: api-reference/media/audio.md
```

---

title: st.audio
slug: /develop/api-reference/media/st.audio
description: st.audio displays an audio player.

---

<Autofunction function="streamlit.audio" />

```

File: api-reference/media/_index.md
```

---

title: Media elements
slug: /develop/api-reference/media

---

# Media elements

It's easy to embed images, videos, and audio files directly into your Streamlit apps.

<TileContainer>
<RefCard href="/develop/api-reference/media/st.image">

<Image pure alt="screenshot" src="/images/api/image.jpg" />

<h4>Image</h4>

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

</RefCard>
<RefCard href="/develop/api-reference/media/st.audio">

<Image pure alt="screenshot" src="/images/api/audio.jpg" />

<h4>Audio</h4>

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```

</RefCard>
<RefCard href="/develop/api-reference/media/st.video">

<Image pure alt="screenshot" src="/images/api/video.jpg" />

<h4>Video</h4>

Display a video player.

```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/whitphx/streamlit-webrtc">

<Image pure alt="screenshot" src="/images/api/components/webrtc.jpg" />

<h4>Streamlit Webrtc</h4>

Handling and transmitting real-time video/audio streams with Streamlit. Created by [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">

<Image pure alt="screenshot" src="/images/api/components/drawable-canvas.jpg" />

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas

st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</ComponentCard>

<ComponentCard href="https://github.com/fcakyon/streamlit-image-comparison">

<Image pure alt="screenshot" src="/images/api/components/image-comparison.jpg" />

<h4>Image Comparison</h4>

Compare images with a slider using [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison

image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

</ComponentCard>

<ComponentCard href="https://github.com/turner-anderson/streamlit-cropper">

<Image pure alt="screenshot" src="/images/api/components/cropper.jpg" />

<h4>Streamlit Cropper</h4>

A simple image cropper for Streamlit. Created by [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper

st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates

streamlit_image_coordinates("https://placekitten.com/200/300")
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/media/image.md
```

---

title: st.image
slug: /develop/api-reference/media/st.image
description: st.image displays an image or list of images.

---

<Autofunction function="streamlit.image" />

```

File: api-reference/data/experimental_data_editor.md
```

---

title: st.experimental_data_editor
slug: /develop/api-reference/data/st.experimental_data_editor
description: st.experimental_data_editor display a data editor widget that allows you to edit dataframes and many other data structures in a table-like UI.

---

<Autofunction function="streamlit.experimental_data_editor" deprecated={true} deprecatedText="<code>st.experimental_data_editor</code> was deprecated in version 1.23.0. Use <a href='/develop/api-reference/data/st.data_editor'><code>st.data_editor</code></a> instead."/>

```

File: api-reference/data/table.md
```

---

title: st.table
slug: /develop/api-reference/data/st.table
description: st.table displays a static table.

---

<Tip>

Static tables with `st.table` are the most basic way to display dataframes. For the majority of cases, we recommend using [`st.dataframe`](/develop/api-reference/data/st.dataframe) to display interactive dataframes, and [`st.data_editor`](/develop/api-reference/data/st.data_editor) to let users edit dataframes.

</Tip>

<Autofunction function="streamlit.table" />

<Autofunction function="DeltaGenerator.add_rows" />

```

File: api-reference/data/dataframe.md
```

---

title: st.dataframe
slug: /develop/api-reference/data/st.dataframe
description: st.dataframe displays a dataframe as an interactive table.

---

<Tip>

This page only contains information on the `st.dataframe` API. For an overview of working with dataframes read [Dataframes](/develop/concepts/design/dataframes). If you want to let users interactively edit dataframes, check out [`st.data_editor`](/develop/api-reference/data/st.data_editor).

</Tip>

<Autofunction function="streamlit.dataframe" />

<br />

`st.dataframe` supports the `use_container_width` parameter to stretch across the full container width:

```python
import pandas as pd
import streamlit as st

# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)
```

<Cloud src="https://doc-dataframe2.streamlit.app/?embed=true" height="350" />

<Autofunction function="DeltaGenerator.add_rows" />

### Interactivity

Dataframes displayed with `st.dataframe` are interactive. End users can sort, resize, search, and copy data to their clipboard. For on overview of features, read our [Dataframes](/develop/concepts/design/dataframes#additional-ui-features) guide.

### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

<Cloud src="https://doc-column-config-overview.streamlit.app/?embed=true&embed_options=disable_scrolling" height="480"/>

```

File: api-reference/data/_index.md
```

---

title: Data elements
slug: /develop/api-reference/data

---

# Data elements

When you're working with data, it is extremely valuable to visualize that
data quickly, interactively, and from multiple different angles. That's what
Streamlit is actually built and optimized for.

You can display data via [charts](#display-charts), and you can display it in
raw form. These are the Streamlit commands you can use to display and interact with raw data.

<TileContainer>
<RefCard href="/develop/api-reference/data/st.dataframe">
<Image pure alt="screenshot" src="/images/api/dataframe.jpg" />

<h4>Dataframes</h4>

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">

<Image pure alt="screenshot" src="/images/api/data_editor.jpg" />

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.column_config">

<Image pure alt="screenshot" src="/images/api/column_config.jpg" />

<h4>Column configuration</h4>

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.table">
<Image pure alt="screenshot" src="/images/api/table.jpg" />

<h4>Static tables</h4>

Display a static table.

```python
st.table(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.metric">
<Image pure alt="screenshot" src="/images/api/metric.jpg" />

<h4>Metrics</h4>

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.json">
<Image pure alt="screenshot" src="/images/api/json.jpg" />

<h4>Dicts and JSON</h4>

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/PablocFonseca/streamlit-aggrid">

<Image pure alt="screenshot" src="/images/api/components/aggrid.jpg" />

<h4>Streamlit Aggrid</h4>

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)

new_df = grid_return['data']
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">

<Image pure alt="screenshot" src="/images/api/components/pandas-profiling.jpg" />

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</ComponentCard>

<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">

<Image pure alt="screenshot" src="/images/api/components/image-coordinates.jpg" />

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])

selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-metric-cards.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)

style_metric_cards()
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/data/data_editor.md
```

---

title: st.data_editor
slug: /develop/api-reference/data/st.data_editor
description: st.data_editor display a data editor widget that allows you to edit dataframes and many other data structures in a table-like UI.

---

<Tip>

This page only contains information on the `st.data_editor` API. For an overview of working with dataframes and to learn more about the data editor's capabilities and limitations, read [Dataframes](/develop/concepts/design/dataframes).

</Tip>

<Autofunction function="streamlit.data_editor" oldName="streamlit.experimental_data_editor" />

### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

<Cloud src="https://doc-column-config-overview.streamlit.app/?embed=true&embed_options=disable_scrolling" height="480"/>

```

File: api-reference/data/metric.md
```

---

title: st.metric
slug: /develop/api-reference/data/st.metric
description: st.metric displays a metric in big bold font, with an optional indicator of how the metric changed.

---

<Autofunction function="streamlit.metric" />

```

File: api-reference/data/json.md
```

---

title: st.json
slug: /develop/api-reference/data/st.json
description: st.json displays object or string as a pretty-printed JSON string.

---

<Autofunction function="streamlit.json" />

```

File: api-reference/data/column_config/barchartcolumn.md
```

---

title: st.column_config.BarChartColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.barchartcolumn

---

<Autofunction function="streamlit.column_config.BarChartColumn" />

```

File: api-reference/data/column_config/checkboxcolumn.md
```

---

title: st.column_config.CheckboxColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn

---

<Autofunction function="streamlit.column_config.CheckboxColumn" />

```

File: api-reference/data/column_config/selectboxcolumn.md
```

---

title: st.column_config.SelectboxColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn

---

<Autofunction function="streamlit.column_config.SelectboxColumn" />

```

File: api-reference/data/column_config/linechartcolumn.md
```

---

title: st.column_config.LineChartColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.linechartcolumn

---

<Autofunction function="streamlit.column_config.LineChartColumn" />

```

File: api-reference/data/column_config/column.md
```

---

title: st.column_config.Column
slug: /develop/api-reference/data/st.column_config/st.column_config.column

---

<Autofunction function="streamlit.column_config.Column" />

```

File: api-reference/data/column_config/datecolumn.md
```

---

title: st.column_config.DateColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.datecolumn

---

<Autofunction function="streamlit.column_config.DateColumn" />

```

File: api-reference/data/column_config/textcolumn.md
```

---

title: st.column_config.TextColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.textcolumn

---

<Autofunction function="streamlit.column_config.TextColumn" />

```

File: api-reference/data/column_config/datetimecolumn.md
```

---

title: st.column_config.DatetimeColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.datetimecolumn

---

<Autofunction function="streamlit.column_config.DatetimeColumn" />

```

File: api-reference/data/column_config/areachartcolumn.md
```

---

title: st.column_config.AreaChartColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.areachartcolumn

---

<Autofunction function="streamlit.column_config.AreaChartColumn" />

```

File: api-reference/data/column_config/linkcolumn.md
```

---

title: st.column_config.LinkColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.linkcolumn

---

<Autofunction function="streamlit.column_config.LinkColumn" />

```

File: api-reference/data/column_config/numbercolumn.md
```

---

title: st.column_config.NumberColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.numbercolumn

---

<Autofunction function="streamlit.column_config.NumberColumn" />

```

File: api-reference/data/column_config/listcolumn.md
```

---

title: st.column_config.ListColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.listcolumn

---

<Autofunction function="streamlit.column_config.ListColumn" />

```

File: api-reference/data/column_config/_index.md
```

---

title: st.column_config
slug: /develop/api-reference/data/st.column_config

---

# Column configuration

When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in [`st.dataframe`](/develop/api-reference/data/st.dataframe) and [`st.data_editor`](/develop/api-reference/data/st.data_editor), it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

<TileContainer>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.column">
<Image pure alt="screenshot" src="/images/api/column_config.column.jpg" />

<h4>Column</h4>

Configure a generic column.

```python
Column("Streamlit Widgets", width="medium", help="Streamlit **widget** commands ≡ƒÄê")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.textcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.textcolumn.jpg" />

<h4>Text column</h4>

Configure a text column.

```python
TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.numbercolumn">
<Image pure alt="screenshot" src="/images/api/column_config.numbercolumn.jpg" />

<h4>Number column</h4>

Configure a number column.

```python
NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.checkboxcolumn.jpg" />

<h4>Checkbox column</h4>

Configure a checkbox column.

```python
CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.selectboxcolumn.jpg" />

<h4>Selectbox column</h4>

Configure a selectbox column.

```python
SelectboxColumn("App Category", options=["≡ƒñû LLM", "≡ƒôê Data Viz"])
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn">
<Image pure alt="screenshot" src="/images/api/column_config.datetimecolumn.jpg" />

<h4>Datetime column</h4>

Configure a datetime column.

```python
DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.datecolumn">
<Image pure alt="screenshot" src="/images/api/column_config.datecolumn.jpg" />

<h4>Date column</h4>

Configure a date column.

```python
DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.timecolumn">
<Image pure alt="screenshot" src="/images/api/column_config.timecolumn.jpg" />

<h4>Time column</h4>

Configure a time column.

```python
TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")
```

</RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.listcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.listcolumn.jpg" />

<h4>List column</h4>

Configure a list column.

```python
ListColumn("Sales (last 6 months)", width="medium")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.linkcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.linkcolumn.jpg" />

<h4>Link column</h4>

Configure a link column.

```python
LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.imagecolumn">
<Image pure alt="screenshot" src="/images/api/column_config.imagecolumn.jpg" />

<h4>Image column</h4>

Configure an image column.

```python
ImageColumn("Preview Image", help="The preview screenshots")
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.areachartcolumn.jpg" />

<h4>Area chart column</h4>

Configure an area chart column.

```python
AreaChartColumn("Sales (last 6 months)" y_min=0, y_max=100)
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.linechartcolumn.jpg" />

<h4>Line chart column</h4>

Configure a line chart column.

```python
LineChartColumn("Sales (last 6 months)" y_min=0, y_max=100)
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn">
<Image pure alt="screenshot" src="/images/api/column_config.barchartcolumn.jpg" />

<h4>Bar chart column</h4>

Configure a bar chart column.

```python
BarChartColumn("Marketing spend" y_min=0, y_max=100)
```

</RefCard>

<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.progresscolumn">
<Image pure alt="screenshot" src="/images/api/column_config.progresscolumn.jpg" />

<h4>Progress column</h4>

Configure a progress column.

```python
ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")
```

</RefCard>

</TileContainer>

```

File: api-reference/data/column_config/timecolumn.md
```

---

title: st.column_config.TimeColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.timecolumn

---

<Autofunction function="streamlit.column_config.TimeColumn" />

```

File: api-reference/data/column_config/progresscolumn.md
```

---

title: st.column_config.ProgressColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.progresscolumn

---

<Autofunction function="streamlit.column_config.ProgressColumn" />

```

File: api-reference/data/column_config/imagecolumn.md
```

---

title: st.column_config.ImageColumn
slug: /develop/api-reference/data/st.column_config/st.column_config.imagecolumn

---

<Autofunction function="streamlit.column_config.ImageColumn" />

```

File: api-reference/utilities/experimental-user.md
```

---

title: st.experimental_user
slug: /develop/api-reference/utilities/st.experimental_user
description: st.experimental_user returns information about the logged-in user of private apps on Streamlit Community Cloud.

---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Autofunction function="streamlit.experimental_user" />

### Examples

The ability to personalize apps for the user viewing the app is a great way to make your app more engaging.

It unlocks a plethora of use-cases for developers, some of which could include: showing additional controls for admins, visualizing a user's Streamlit history, a personalized stock ticker, a chatbot app, and much more. We're excited to see what you build with this feature!

Here's a code snippet that shows extra buttons for admins:

```python
# Show extra buttons for admin users.
ADMIN_USERS = {
    'person1@email.com',
    'person2@email.com',
    'person3@email.com'
}
if st.experimental_user.email in ADMIN_USERS:
    display_the_extra_admin_buttons()
display_the_interface_everyone_sees()
```

Show different content to users based on their email address:

```python
# Show different content based on the user's email address.
if st.experimental_user.email == 'jane@email.com':
    display_jane_content()
elif st.experimental_user.email == 'adam@foocorp.io':
    display_adam_content()
else:
    st.write("Please contact us to get access!")
```

Greet users with their name that's stored in a database:

```python
# Greet the user by their name.
if st.experimental_user.email:
    # Get the user's name from the database.
    name = get_name_from_db(st.experimental_user.email)
    st.write('Hello, %s!' % name)
```

<Autofunction function="streamlit.experimental_user.to_dict" />

```

File: api-reference/utilities/_index.md
```

---

title: Utilities and user info
slug: /develop/api-reference/utilities

---

# Utilities and user info

There are a handful of methods that allow you to create placeholders in your
app, provide help using doc strings, get and modify configuration options and query parameters.

<TileContainer>
<RefCard href="/develop/api-reference/utilities/st.experimental_user" size="half">

<h4>User info</h4>

`st.experimental_user` returns information about the logged-in user of private apps on Streamlit Community Cloud.

```python
if st.experimental_user.email == "foo@corp.com":
  st.write("Welcome back, ", st.experimental_user.email)
else:
  st.write("You are not authorized to view this page.")
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.help" size="half">

<h4>Get help</h4>

Display objectΓÇÖs doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/develop/api-reference/utilities/st.html" size="half">

<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
css = """
<style>
    p { color: red; }
</style>
"""
st.html(css)
```

</RefCard>
</TileContainer>

```

File: api-reference/utilities/html.md
```

---

title: st.html
slug: /develop/api-reference/utilities/st.html
description: st.html renders arbitrary HTML strings to your app

---

<Autofunction function="streamlit.html" />

```

File: api-reference/utilities/help.md
```

---

title: st.help
slug: /develop/api-reference/utilities/st.help
description: st.help displays object's doc string, nicely formatted.

---

<Autofunction function="streamlit.help" />

```

File: api-reference/charts/line_chart.md
```

---

title: st.line_chart
slug: /develop/api-reference/charts/st.line_chart
description: st.line_chart displays a line chart.

---

<Autofunction function="streamlit.line_chart" />

<Autofunction function="DeltaGenerator.add_rows" />

```

File: api-reference/charts/scatter_chart.md
```

---

title: st.scatter_chart
slug: /develop/api-reference/charts/st.scatter_chart
description: st.scatter_chart displays an scatter chart.

---

<Autofunction function="streamlit.scatter_chart" />

<Autofunction function="DeltaGenerator.add_rows" />

```

File: api-reference/charts/graphviz_chart.md
```

---

title: st.graphviz_chart
slug: /develop/api-reference/charts/st.graphviz_chart
description: st.graphviz_chart displays a graph using the dagre-d3 library.

---

<Autofunction function="streamlit.graphviz_chart" />

```

File: api-reference/charts/altair_chart.md
```

---

title: st.altair_chart
slug: /develop/api-reference/charts/st.altair_chart
description: st.altair_chart displays a chart using the Altair library.

---

<Autofunction function="streamlit.altair_chart" />

### Theming

Altair charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Altair's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Altair theme:

```python
import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud src="https://doc-altair-chart.streamlit.app/?embed=true" height="500" />

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Altair chart where manual color passing is done and reflected:

<Collapse title="See the code">

```python
import altair as alt
import streamlit as st
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(date):T", title="Date"),
        alt.Y(
            "temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)

# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
```

</Collapse>

Notice how the custom colors are still reflected in the chart, even when the Streamlit theme is enabled ≡ƒæç

<Cloud src="https://doc-altair-custom-colors.streamlit.app/?embed=true" height="675" />

For many more examples of Altair charts with and without the Streamlit theme, check out the [altair.streamlit.app](https://altair.streamlit.app).

### Annotating charts

Altair also allows you to annotate your charts with text, images, and emojis. You can do this by creating [layered charts](https://altair-viz.github.io/user_guide/compound_charts.html#layered-charts), which let you overlay two different charts on top of each other. The idea is to use the first chart to show the data, and the second chart to show the annotations. The second chart can then be overlaid on top of the first chart using the `+` operator to create a layered chart.

Let's walk through an example of annotating a time-series chart with text and an emoji.

#### Step 1: Create the base chart

In this example, we create a time-series chart to track the evolution of stock prices. The chart is interactive and contains a multi-line tooltip. Click [here](https://altair-viz.github.io/gallery/multiline_tooltip.html) to learn more about multi-line tooltips in Altair.

First, we import the required libraries and load the example stocks dataset using the [`vega_datasets`](https://pypi.org/project/vega-datasets/) package:

```python
import altair as alt
import pandas as pd
import streamlit as st
from vega_datasets import data

# We use @st.cache_data to keep the dataset in cache
@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source

source = get_data()
```

Next, we define a function `get_chart()` to create the interactive time-series chart of the stock prices with a multi-line tooltip. The x-axis represents the date, and the y-axis represents the stock price.

We then invoke `get_chart()` that takes the stock prices dataframe as an input and returns a chart object. This is going to be our base chart on which we will overlay the annotations in [Step 2](/develop/api-reference/charts/st.altair_chart#step-2-annotate-the-chart).

```python
# Define the base time-series chart.
def get_chart(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Evolution of stock prices")
        .mark_line()
        .encode(
            x="date",
            y="price",
            color="symbol",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("price", title="Price (USD)"),
            ],
        )
        .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()

chart = get_chart(source)
```

#### Step 2: Annotate the chart

Now that we have our first chart that shows the data, we can annotate it with text and an emoji. Let's overlay the Γ¼ç emoji on top of the time-series chart at specifc points of interest. We want users to hover over the Γ¼ç emoji to see the associated annotation text.

For simplicity, let's annotate four specific dates and set the height of the annotations at constant value of `10`.

<Tip>

You can vary the horizontal and vertical postions of the annotations by replacing the hard-coded values with the output of Streamlit widgets! Click [here](/develop/api-reference/charts/st.altair_chart#interactive-example) to jump to a live example below, and develop an intuition for the ideal horizontal and vertical positions of the annotations by playing with Streamlit widgets.

</Tip>

To do so, we create a dataframe `annotations_df` containing the dates, annotation text, and the height of the annotations:

```python
# Add annotations
ANNOTATIONS = [
    ("Mar 01, 2008", "Pretty good day for GOOG"),
    ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
    ("Nov 01, 2008", "Market starts again thanks to..."),
    ("Dec 01, 2009", "Small crash for GOOG after..."),
]
annotations_df = pd.DataFrame(ANNOTATIONS, columns=["date", "event"])
annotations_df.date = pd.to_datetime(annotations_df.date)
annotations_df["y"] = 10
```

Using this dataframe, we create a scatter plot with the x-axis representing the date, and the y-axis representing the height of the annotation. The data point at the specific date and height is represented by the Γ¼ç emoji, using Altair's `mark_text()` [mark](https://altair-viz.github.io/user_guide/marks.html).

The annotation text is displayed as a tooltip when users hover over the Γ¼ç emoji. This is achieved using Altair's `encode()` method to map the `event` column containing the annotation text to the visual attribute Γ¼ç of the plot.

```python
annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=20, text="Γ¼ç", dx=-8, dy=-10, align="left")
    .encode(
        x="date:T",
        y=alt.Y("y:Q"),
        tooltip=["event"],
    )
    .interactive()
)
```

Finally, we overlay the annotations on top of the base chart using the `+` operator to create the final layered chart! ≡ƒÄê

```python
st.altair_chart(
    (chart + annotation_layer).interactive(),
    use_container_width=True
)
```

<Image src="/images/api/altair-annotation.png" />

To use images instead of emojis, replace the line containing `.mark_text()` with `.mark_image()`, and replace `image_url` below with the URL of the image:

```python
.mark_image(
    width=12,
    height=12,
    url="image_url",
)
```

#### Interactive example

Now that you've learned how to annotate charts, the sky's the limit! We've extended the above example to let you interactively paste your favorite emoji and set its position on the chart with Streamlit widgets. ≡ƒæç

<Cloud src="https://example-time-series-annotation.streamlit.app/?embed=true" height="700" />

```

File: api-reference/charts/bokeh_chart.md
```

---

title: st.bokeh_chart
slug: /develop/api-reference/charts/st.bokeh_chart
description: st.bokeh_chart displays an interactive Bokeh chart.

---

<Autofunction function="streamlit.bokeh_chart" />

```

File: api-reference/charts/pyplot.md
```

---

title: st.pyplot
slug: /develop/api-reference/charts/st.pyplot
description: st.pyplot displays a matplotlib.pyplot figure.

---

<Autofunction function="streamlit.pyplot" />

```

File: api-reference/charts/plotly_chart.md
```

---

title: st.plotly_chart
slug: /develop/api-reference/charts/st.plotly_chart
description: st.plotly_chart displays an interactive Plotly chart.

---

<Autofunction function="streamlit.plotly_chart" />

### Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud src="https://doc-plotly-chart-theme.streamlit.app/?embed=true" height="525" />

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Plotly chart where a custom color scale is defined and reflected:

```python
import plotly.express as px
import streamlit as st

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Notice how the custom color scale is still reflected in the chart, even when the Streamlit theme is enabled ≡ƒæç

<Cloud src="https://doc-plotly-custom-colors.streamlit.app/?embed=true" height="650" />

For many more examples of Plotly charts with and without the Streamlit theme, check out the [plotly.streamlit.app](https://plotly.streamlit.app).

```

File: api-reference/charts/area_chart.md
```

---

title: st.area_chart
slug: /develop/api-reference/charts/st.area_chart
description: st.area_chart displays an area chart.

---

<Autofunction function="streamlit.area_chart" />

<Autofunction function="DeltaGenerator.add_rows" />

```

File: api-reference/charts/bar_chart.md
```

---

title: st.bar_chart
slug: /develop/api-reference/charts/st.bar_chart
description: st.bar_chart displays a bar chart.

---

<Autofunction function="streamlit.bar_chart" />

<Autofunction function="DeltaGenerator.add_rows" />

```

File: api-reference/charts/map.md
```

---

title: st.map
slug: /develop/api-reference/charts/st.map
description: st.map displays a map with points on it.

---

<Autofunction function="streamlit.map" />

<Autofunction function="DeltaGenerator.add_rows" />

```

File: api-reference/charts/pydeck_chart.md
```

---

title: st.pydeck_chart
slug: /develop/api-reference/charts/st.pydeck_chart
description: st.pydeck_chart displays a chart using the PyDeck library.

---

<Autofunction function="streamlit.pydeck_chart" />

```

File: api-reference/charts/_index.md
```

---

title: Chart elements
slug: /develop/api-reference/charts

---

# Chart elements

Streamlit supports several different charting libraries, and our goal is to
continually add support for more. Right now, the most basic library in our
arsenal is [Matplotlib](https://matplotlib.org/). Then there are also
interactive charting libraries like [Vega
Lite](https://vega.github.io/vega-lite/) (2D charts) and
[deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And
finally we also provide a few chart types that are "native" to Streamlit,
like `st.line_chart` and `st.area_chart`.

## Simple chart elements

<TileContainer>
<RefCard href="/develop/api-reference/charts/st.area_chart">
<Image pure alt="screenshot" src="/images/api/area_chart.jpg" />

<h4>Simple area charts</h4>

Display an area chart.

```python
st.area_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bar_chart">
<Image pure alt="screenshot" src="/images/api/bar_chart.jpg" />

<h4>Simple bar charts</h4>

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.line_chart">
<Image pure alt="screenshot" src="/images/api/line_chart.jpg" />

<h4>Simple line charts</h4>

Display a line chart.

```python
st.line_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.scatter_chart">
<Image pure alt="screenshot" src="/images/api/scatter_chart.svg" />

<h4>Simple scatter charts</h4>

Display a line chart.

```python
st.scatter_chart(my_data_frame)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.map">
<Image pure alt="screenshot" src="/images/api/map.jpg" />

<h4>Scatterplots on maps</h4>

Display a map with points on it.

```python
st.map(my_data_frame)
```

</RefCard>
</TileContainer>

## Advanced chart elements

<TileContainer>
<RefCard href="/develop/api-reference/charts/st.pyplot">
<Image pure alt="screenshot" src="/images/api/pyplot.jpg" />

<h4>Matplotlib</h4>

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.altair_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Altair</h4>

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.vega_lite_chart">
<Image pure alt="screenshot" src="/images/api/vega_lite_chart.jpg" />

<h4>Vega-Lite</h4>

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.plotly_chart">
<Image pure alt="screenshot" src="/images/api/plotly_chart.jpg" />

<h4>Plotly</h4>

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.bokeh_chart">
<Image pure alt="screenshot" src="/images/api/bokeh_chart.jpg" />

<h4>Bokeh</h4>

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.pydeck_chart">
<Image pure alt="screenshot" src="/images/api/pydeck_chart.jpg" />

<h4>PyDeck</h4>

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

</RefCard>
<RefCard href="/develop/api-reference/charts/st.graphviz_chart">
<Image pure alt="screenshot" src="/images/api/graphviz_chart.jpg" />

<h4>GraphViz</h4>

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

</RefCard>
</TileContainer>

<ComponentSlider>

<ComponentCard href="https://github.com/tvst/plost">

<Image pure alt="screenshot" src="/images/api/components/plost.jpg" />

<h4>Plost</h4>

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

</ComponentCard>

<ComponentCard href="https://github.com/facebookresearch/hiplot">

<Image pure alt="screenshot" src="/images/api/components/hiplot.jpg" />

<h4>HiPlot</h4>

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-echarts">

<Image pure alt="screenshot" src="/images/api/components/echarts.jpg" />

<h4>ECharts</h4>

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

</ComponentCard>

<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">

<Image pure alt="screenshot" src="/images/api/components/folium.jpg" />

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

</ComponentCard>

<ComponentCard href="https://github.com/explosion/spacy-streamlit">

<Image pure alt="screenshot" src="/images/api/components/spacy.jpg" />

<h4>Spacy-Streamlit</h4>

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

</ComponentCard>

<ComponentCard href="https://github.com/ChrisDelClea/streamlit-agraph">

<Image pure alt="screenshot" src="/images/api/components/agraph.jpg" />

<h4>Streamlit Agraph</h4>

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
```

</ComponentCard>

<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">

<Image pure alt="screenshot" src="/images/api/components/lottie.jpg" />

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

</ComponentCard>

<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">

<Image pure alt="screenshot" src="/images/api/components/plotly-events.jpg" />

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

</ComponentCard>

<ComponentCard href="https://extras.streamlit.app/">

<Image pure alt="screenshot" src="/images/api/components/extras-chart-annotations.jpg" />

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

</ComponentCard>

</ComponentSlider>

```

File: api-reference/charts/vega_lite_chart.md
```

---

title: st.vega_lite_chart
slug: /develop/api-reference/charts/st.vega_lite_chart
description: st.vega_lite_chart displays a chart using the Vega-Lite library.

---

<Autofunction function="streamlit.vega_lite_chart" />

<Autofunction function="DeltaGenerator.add_rows" />

### Theming

Vega-Lite charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Vega-Lite's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Vega-Lite theme:

```python
import streamlit as st
from vega_datasets import data

source = data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud src="https://doc-vega-lite-theme.streamlit.app/?embed=true" height="500" />

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

```

File: api-reference/configuration/config-toml.md
```

---

title: config.toml
slug: /develop/api-reference/configuration/config.toml

---

## config.toml

`config.toml` is an optional file you can define for your working directory or global development environment. When `config.toml` is defined both globally and in your working directory, Streamlit combines the configuration options and gives precendence to the working-directory configuration. Additionally, you can use environment variables and command-line optionas to override additional configuration options. For more information, see [Configuration options](/develop/concepts/configuration/options).

### File location

To define your configuration locally or per-project, add `.streamlit/config.toml` to your working directory. Your working directory is wherever you call `streamlit run`. If you haven't previously created the `.streamlit` directory, you will need to add it.

To define your configuration globally, you must first locate your global `.streamlit` directory. Streamlit adds this hidden directory to your OS user profile during installation. For MacOS/Linx, this will be `~/.streamlit/config.toml`. For Windows, this will be `%userprofile%/.streamlit/config.toml`.

### File format

`config.toml` is a [TOML](https://toml.io/en/) file.

#### Example

```toml
[client]
showErrorDetails = false

[theme]
primaryColor = "#F63366"
backgroundColor = "black"
```

### Available configuration options

Below are all the sections and options you can have in your `.streamlit/config.toml` file. To see all configurations, use the following command in your terminal or CLI:

```bash
streamlit config show
```

#### Global

```toml
[global]

# ***DEPRECATED***
# global.disableWatchdogWarning has been deprecated has been deprecated and
# will be removed in a future version. This option will be removed on or after
# 2024-01-20.
# ****************
# By default, Streamlit checks if the Python watchdog module is available
# and, if not, prints a warning asking for you to install it. The watchdog
# module is not required, but highly recommended. It improves Streamlit's
# ability to detect changes to files in your filesystem.
# If you'd like to turn off this warning, set this to True.
# Default: false
disableWatchdogWarning = false

# By default, Streamlit displays a warning when a user sets both a widget
# default value in the function defining the widget and a widget value via
# the widget's key in `st.session_state`.
# If you'd like to turn off this warning, set this to True.
# Default: false
disableWidgetStateDuplicationWarning = false

# If True, will show a warning when you run a Streamlit-enabled script
# via "python my_script.py".
# Default: true
showWarningOnDirectExecution = true
```

#### Logger

```toml
[logger]

# Level of logging: 'error', 'warning', 'info', or 'debug'.
# Default: 'info'
level = "info"

# String format for logging messages. If logger.datetimeFormat is set,
# logger messages will default to `%(asctime)s.%(msecs)03d %(message)s`. See
# Python's documentation for available attributes:
# https://docs.python.org/2.6/develop/logging.html#formatter-objects
# Default: "%(asctime)s %(message)s"
messageFormat = "%(asctime)s %(message)s"
```

#### Client

```toml
[client]

# ***DEPRECATED***
# client.caching has been deprecated and is not required anymore for our new
# caching commands. This option will be removed on or after 2024-01-20.
# ****************
# Whether to enable st.cache. This does not affect st.cache_data or
# st.cache_resource.
# Default: true
caching = true

# ***DEPRECATED***
# client.displayEnabled has been deprecated and will be removed in a future
# version. This option will be removed on or after 2024-01-20.
# ****************
# If false, makes your Streamlit script not draw to a Streamlit app.
# Default: true
displayEnabled = true

# Controls whether uncaught app exceptions and deprecation warnings
# are displayed in the browser. By default, this is set to True and
# Streamlit displays app exceptions and associated tracebacks, and
# deprecation warnings, in the browser.
#
# If set to False, deprecation warnings and full exception messages
# will print to the console only. Exceptions will still display in the
# browser with a generic error message. For now, the exception type and
# traceback show in the browser also, but they will be removed in the
# future.
# Default: true
showErrorDetails = true

# Change the visibility of items in the toolbar, options menu,
# and settings dialog (top right of the app).
# Allowed values:
# * "auto"      : Show the developer options if the app is accessed through
#                 localhost or through Streamlit Community Cloud as a developer.
#                 Hide them otherwise.
# * "developer" : Show the developer options.
# * "viewer"    : Hide the developer options.
# * "minimal"   : Show only options set externally (e.g. through
#                 Streamlit Community Cloud) or through st.set_page_config.
#                 If there are no options left, hide the menu.
# Default: "auto"
toolbarMode = "auto"

# Controls whether the default sidebar page navigation in a multipage app is
# displayed.
# Default: true
showSidebarNavigation = true
```

#### Runner

```toml
[runner]

# Allows you to type a variable or string by itself in a single line of
# Python code to write it to the app.
# Default: true
magicEnabled = true

# ***DEPRECATED***
# runner.installTracer has been deprecated and will be removed in a future
# version. This option will be removed on or after 2024-01-20.
# ****************
# Install a Python tracer to allow you to stop or pause your script at
# any point and introspect it. As a side-effect, this slows down your
# script's execution.
# Default: false
installTracer = false

# ***DEPRECATED***
# runner.fixMatplotlib has been deprecated and will be removed in a future
# version. This option will be removed on or after 2024-01-20.
# ****************
# Sets the MPLBACKEND environment variable to Agg inside Streamlit to
# prevent Python crashing.
# Default: true
fixMatplotlib = true

# Handle script rerun requests immediately, rather than waiting for script
# execution to reach a yield point. This makes Streamlit much more
# responsive to user interaction, but it can lead to race conditions in
# apps that mutate session_state data outside of explicit session_state
# assignment statements.
# Default: true
fastReruns = true

# Raise an exception after adding unserializable data to Session State.
# Some execution environments may require serializing all data in Session
# State, so it may be useful to detect incompatibility during development,
# or when the execution environment will stop supporting it in the future.
# Default: false
enforceSerializableSessionState = false

# Adjust how certain 'options' widgets like radio, selectbox, and
# multiselect coerce Enum members when the Enum class gets
# re-defined during a script re-run. For more information, check out the docs:
# https://docs.streamlit.io/develop/concepts/design/custom-classes#enums
#
# Allowed values:
# * "off"          : Disables Enum coercion.
# * "nameOnly"     : Enum classes can be coerced if their member names match.
# * "nameAndValue" : Enum classes can be coerced if their member names AND
#                    member values match.
# Default: "nameOnly"
enumCoercion = "nameOnly"
```

#### Server

```toml
[server]

# List of folders that should not be watched for changes. This
# impacts both "Run on Save" and @st.cache.
# Relative paths will be taken as relative to the current working directory.
# Example: ['/home/user1/env', 'relative/path/to/folder']
# Default: []
folderWatchBlacklist = []

# Change the type of file watcher used by Streamlit, or turn it off
# completely.
# Allowed values:
# * "auto"     : Streamlit will attempt to use the watchdog module, and
#                falls back to polling if watchdog is not available.
# * "watchdog" : Force Streamlit to use the watchdog module.
# * "poll"     : Force Streamlit to always use polling.
# * "none"     : Streamlit will not watch files.
# Default: "auto"
fileWatcherType = "auto"

# Symmetric key used to produce signed cookies. If deploying on multiple
# replicas, this should be set to the same value across all replicas to ensure
# they all share the same secret.
# Default: randomly generated secret key.
cookieSecret = "a-random-key-appears-here"

# If false, will attempt to open a browser window on start.
# Default: false unless (1) we are on a Linux box where DISPLAY is unset, or
# (2) we are running in the Streamlit Atom plugin.
headless = false

# Automatically rerun script when the file is modified on disk.
# Default: false
runOnSave = false

# The address where the server will listen for client and browser
# connections. Use this if you want to bind the server to a specific address.
# If set, the server will only be accessible from this address, and not from
# any aliases (like localhost).
# Default: (unset)
address =

# The port where the server will listen for browser connections.
# Don't use port 3000 which is reserved for internal development.
# Default: 8501
port = 8501

# The base path for the URL where Streamlit should be served from.
# Default: ""
baseUrlPath = ""

# Enables support for Cross-Origin Resource Sharing (CORS) protection, for
# added security.
# Due to conflicts between CORS and XSRF, if `server.enableXsrfProtection` is
# on and `server.enableCORS` is off at the same time, we will prioritize
# `server.enableXsrfProtection`.
# Default: true
enableCORS = true

# Enables support for Cross-Site Request Forgery (XSRF) protection, for added
# security.
# Due to conflicts between CORS and XSRF, if `server.enableXsrfProtection` is
# on and `server.enableCORS` is off at the same time, we will prioritize
# `server.enableXsrfProtection`.
# Default: true
enableXsrfProtection = true

# Max size, in megabytes, for files uploaded with the file_uploader.
# Default: 200
maxUploadSize = 200

# Max size, in megabytes, of messages that can be sent via the WebSocket
# connection.
# Default: 200
maxMessageSize = 200

# Enables support for websocket compression.
# Default: false
enableWebsocketCompression = false

# Enable serving files from a `static` directory in the running app's
# directory.
# Default: false
enableStaticServing = false

# Server certificate file for connecting via HTTPS.
# Must be set at the same time as "server.sslKeyFile".
# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For the production environment, we
# recommend performing SSL termination by the load balancer or the reverse
# proxy.']
# sslCertFile =

# Cryptographic key file for connecting via HTTPS.
# Must be set at the same time as "server.sslCertFile".
# ['DO NOT USE THIS OPTION IN A PRODUCTION ENVIRONMENT. It has not gone through
# security audits or performance tests. For the production environment, we
# recommend performing SSL termination by the load balancer or the reverse
# proxy.']
# sslKeyFile =
```

#### Browser

```toml
[browser]

# Internet address where users should point their browsers in order to
# connect to the app. Can be IP address or DNS name and path.
# This is used to:
# - Set the correct URL for CORS and XSRF protection purposes.
# - Show the URL on the terminal
# - Open the browser
# Default: "localhost"
serverAddress = "localhost"

# Whether to send usage statistics to Streamlit.
# Default: true
gatherUsageStats = true

# Port where users should point their browsers in order to connect to the
# app.
# This is used to:
# - Set the correct URL for XSRF protection purposes.
# - Show the URL on the terminal (part of `streamlit run`).
# - Open the browser automatically (part of `streamlit run`).
# This option is for advanced use cases. To change the port of your app, use
# `server.Port` instead. Don't use port 3000 which is reserved for internal
# development.
# Default: whatever value is set in server.port.
serverPort = 8501
```

#### Mapbox

```toml
[mapbox]

# Configure Streamlit to use a custom Mapbox
# token for elements like st.pydeck_chart and st.map.
# To get a token for yourself, create an account at
# https://mapbox.com. It's free (for moderate usage levels)!
# Default: ""
token = ""
```

#### Deprecation

```toml
[deprecation]

# Set to false to disable the deprecation warning for using the global pyplot
# instance.
# Default: true
showPyplotGlobalUse = true
```

#### Theme

```toml
[theme]

# The preset Streamlit theme that your custom theme inherits from.
# One of "light" or "dark".
# base =

# Primary accent color for interactive elements.
# primaryColor =

# Background color for the main content area.
# backgroundColor =

# Background color used for the sidebar and most interactive widgets.
# secondaryBackgroundColor =

# Color used for almost all text.
# textColor =

# Font family for all text in the app, except code blocks. One of "sans serif",
# "serif", or "monospace".
# font =
```

```

File: api-reference/configuration/_index.md
```

---

title: Configuration
slug: /develop/api-reference/configuration

---

# Configuration

<TileContainer>
<RefCard href="/develop/api-reference/configuration/config.toml">

<h4>Configuration file</h4>

Configures the default settings for your app.

```
your-project/
Γö£ΓöÇΓöÇ .streamlit/
Γöé   ΓööΓöÇΓöÇ config.toml
ΓööΓöÇΓöÇ your_app.py
```

</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_page_config">

<h4>Set page title, favicon, and more</h4>

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```

</RefCard>
</TileContainer>

```

File: api-reference/configuration/set_page_config.md
```

---

title: st.set_page_config
slug: /develop/api-reference/configuration/st.set_page_config
description: st.set_page_config configures the default settings of the page.

---

<Autofunction function="streamlit.set_page_config" />

```

File: api-reference/caching-and-state/experimental_get_query_params.md
```

---

title: st.experimental_get_query_params
slug: /develop/api-reference/caching-and-state/st.experimental_get_query_params
description: st.experimental_get_query_params returns query parameters currently showing in the browser's URL bar.

---

<Autofunction function="streamlit.experimental_get_query_params" deprecated={true} deprecatedText="<code>st.experimental_get_query_params</code> was deprecated in version 1.30.0. Use <a href='/develop/api-reference/caching-and-state/st.query_params'><code>st.query_params</code></a> instead." />

```

File: api-reference/caching-and-state/cache-data.md
```

---

title: st.cache_data
slug: /develop/api-reference/caching-and-state/st.cache_data
description: st.cache_data is used to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

---

<Tip>

This page only contains information on the `st.cache_data` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

</Tip>

<Autofunction function="streamlit.cache_data" oldName="streamlit.experimental_memo" />

<Warning>

`st.cache_data` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

<Autofunction function="streamlit.cache_data.clear" oldName="streamlit.experimental_memo.clear" />

#### Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.cache_data`.

```python
import streamlit as st

@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()
```

## Using Streamlit commands in cached functions

### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

```python
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # ≡ƒæê Show a success message
    return data
```

As we know, Streamlit only runs this function if it hasnΓÇÖt been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

```python
@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)
```

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

```python
@st.cache_data(experimental_allow_widgets=True)  # ≡ƒæê Set the parameter
def get_data():
    num_rows = st.slider("Number of rows to get")  # ≡ƒæê Add a slider
    data = api.get(..., num_rows)
    return data
```

Streamlit treats the slider like an additional input parameter to the cached function. If you change the slider position, Streamlit will see if it has already cached the function for this slider value. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then weΓÇÖll add 100 MB to the cache for _every permutation_ of these five slider values ΓÇô even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

<Warning>

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!
</Warning>

<Note>

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!
</Note>

```

File: api-reference/caching-and-state/cache.md
```

---

title: st.cache
slug: /develop/api-reference/caching-and-state/st.cache
description: st.cache is used to memoize function executions.

---

# st.cache

When you mark a function with StreamlitΓÇÖs cache annotation, it tells Streamlit
that whenever the function is called it should check three things:

1. The name of the function
2. The actual code that makes up the body of the function
3. The input parameters that you called the function with

If this is the first time Streamlit has seen those three items, with those exact
values, and in that exact combination, it runs the function and stores the
result in a local cache.

Then, next time the function is called, if those three values have not changed
Streamlit knows it can skip executing the function altogether. Instead, it just
reads the output from the local cache and passes it on to the caller.

The main limitation is that StreamlitΓÇÖs cache feature doesnΓÇÖt know about
changes that take place outside the body of the annotated function.

For more information about the Streamlit cache, its configuration parameters,
and its limitations, see [Caching](/develop/concepts/architecture/caching).

<Autofunction function="streamlit.cache" deprecated={true} deprecatedText="<code>st.cache</code> was deprecated in version 1.18.0. Use <a href='/develop/api-reference/caching-and-state/st.cache_data'><code>st.cache_data</code></a> or <a href='/develop/api-reference/caching-and-state/st.cache_resource'><code>st.cache_resource</code></a> instead. Learn more in <a href='/develop/concepts/architecture/caching'>Caching</a>."/>

<Warning>

`st.cache` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

```

File: api-reference/caching-and-state/query_params.md
```

---

title: st.query_params
slug: /develop/api-reference/caching-and-state/st.query_params
description: st.query_params reads and manipulates query parameters in the browser's URL bar.

---

## st.query_params

`st.query_params` provides a dictionary-like interface to access query parameters in your app's URL and is available as of Streamlit 1.30.0. It behaves similarly to `st.session_state` with the notable exception that keys may be repeated in an app's URL. Handling of repeated keys requires special consideration as explained below. `st.query_params` can be used with both key and attribute notation. For example, `st.query_params.my_key` and `st.query_params["my_key"]`.

Query parameters can be entered into your app's URL or programatically added through `st.query_params`. For example, the following URL and dictionary show the same key-value pairs:

```javascript
https://your_app.streamlit.app/?first_key=1&second_key=two&third_key=true
```

```python
{
    "first_key" : "1",
    "second_key" : "two",
    "third_key" : "true"
}

```

A key-value pair prefixed with `?` is added to the end of your app's URL. Additional key-value pairs can be added. Each additional pair is prefixed with `&` instead of `?`. All keys and values will be set and returned as strings. Query parameters are cleared when navigating between pages in a multipage app.

### Repeated keys

When a key is repeated in your app's URL (`?a=1&a=2&a=3`), dict-like methods will return only the last value. In this example, `st.query_params["a"]` returns `"3"`. To get all keys as a list, use the [`.get_all()`](/develop/api-reference/caching-and-state/st.query_params#stquery_paramsget_all) method shown below. To set the value of a repeated key, assign the values as a list. For example, `st.query_params.a = ["1", "2", "3"]` produces the repeated key given at the beginning of this paragraph.

### Limitation

`st.query_params` can't get or set embedding settings as described in [Embed your app](/deploy/streamlit-community-cloud/share-your-app/embed-your-app#embed-options). `st.query_params.embed` and `st.query_params.embed_options` will raise an `AttributeError` or `StreamlitAPIException` when trying to get or set their values, respectively.

<Autofunction function="streamlit.query_params.get_all" />

<Autofunction function="streamlit.query_params.clear" />

<Autofunction function="streamlit.query_params.to_dict" />

```

File: api-reference/caching-and-state/experimental-singleton.md
```

---

title: st.experimental_singleton
slug: /develop/api-reference/caching-and-state/st.experimental_singleton
description: st.experimental_singleton is a function decorator used to store singleton objects.

---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Autofunction function="streamlit.experimental_singleton" deprecated={true} deprecatedText="<code>st.experimental_singleton</code> was deprecated in version 1.18.0. Use <a href='/develop/api-reference/caching-and-state/st.cache_resource'><code>st.cache_resource</code></a> instead. Learn more in <a href='/develop/concepts/architecture/caching'>Caching</a>."/>

<Autofunction function="streamlit.experimental_singleton.clear" deprecated={true} deprecatedText="<code>st.experimental_singleton.clear</code> was deprecated in version 1.18.0. Use <a href='/develop/api-reference/caching-and-state/st.cache_resource#stcache_resourceclear'><code>st.cache_resource.clear</code></a> instead. Learn more in <a href='/develop/concepts/architecture/caching'>Caching</a>."/>

#### Example

In the example below, pressing the "Clear All" button will clear _all_ singleton caches. i.e. Clears cached singleton objects from all functions decorated with `@st.experimental_singleton`.

```python
import streamlit as st
from transformers import BertModel

@st.experimental_singleton
 def get_database_session(url):
     # Create a database session object that points to the URL.
     return session

@st.experimental_singleton
def get_model(model_type):
    # Create a model of the specified type.
    return BertModel.from_pretrained(model_type)

if st.button("Clear All"):
    # Clears all singleton caches:
    st.experimental_singleton.clear()
```

## Validating the cache

The `@st.experimental_singleton` decorator is used to cache the output of a function, so that it only needs to be executed once. This can improve performance in certain situations, such as when a function takes a long time to execute or makes a network request.

However, in some cases, the cached output may become invalid over time, such as when a database connection times out. To handle this, the `@st.experimental_singleton` decorator supports an optional `validate` parameter, which accepts a validation function that is called each time the cached output is accessed. If the validation function returns False, the cached output is discarded and the decorated function is executed again.

### Best Practices

- Use the `validate` parameter when the cached output may become invalid over time, such as when a database connection or an API key expires.
- Use the `validate` parameter judiciously, as it will add an additional overhead of calling the validation function each time the cached output is accessed.
- Make sure that the validation function is as fast as possible, as it will be called each time the cached output is accessed.
- Consider to validate cached data periodically, instead of each time it is accessed, to mitigate the performance impact.
- Handle errors that may occur during validation and provide a fallback mechanism if the validation fails.

## Replay static `st` elements in cache-decorated functions

Functions decorated with `@st.experimental_singleton` can contain static `st` elements. When a cache-decorated function is executed, we record the element and block messages produced, so the elements will appear in the app even when execution of the function is skipped because the result was cached.

In the example below, the `@st.experimental_singleton` decorator is used to cache the execution of the `get_model` function, that returns a ≡ƒñù Hugging Face Transformers model. Notice the cached function also contains a `st.bar_chart` command, which will be replayed when the function is skipped because the result was cached.

```python
import numpy as np
import pandas as pd
import streamlit as st
from transformers import AutoModel

@st.experimental_singleton
def get_model(model_type):
    # Contains a static element st.bar_chart
    st.bar_chart(
        np.random.rand(10, 1)
    )  # This will be recorded and displayed even when the function is skipped

    # Create a model of the specified type
    return AutoModel.from_pretrained(model_type)

bert_model = get_model("distilbert-base-uncased")
st.help(bert_model) # Display the model's docstring
```

<Image src="/images/replay-cached-elements-singleton.png" clean />

Supported static `st` elements in cache-decorated functions include:

- `st.alert`
- `st.altair_chart`
- `st.area_chart`
- `st.audio`
- `st.bar_chart`
- `st.ballons`
- `st.bokeh_chart`
- `st.caption`
- `st.code`
- `st.components.v1.html`
- `st.components.v1.iframe`
- `st.container`
- `st.dataframe`
- `st.echo`
- `st.empty`
- `st.error`
- `st.exception`
- `st.expander`
- `st.experimental_get_query_params`
- `st.experimental_set_query_params`
- `st.form`
- `st.form_submit_button`
- `st.graphviz_chart`
- `st.help`
- `st.image`
- `st.info`
- `st.json`
- `st.latex`
- `st.line_chart`
- `st.markdown`
- `st.metric`
- `st.plotly_chart`
- `st.progress`
- `st.pydeck_chart`
- `st.snow`
- `st.spinner`
- `st.success`
- `st.table`
- `st.text`
- `st.vega_lite_chart`
- `st.video`
- `st.warning`

## Replay input widgets in cache-decorated functions

In addition to static elements, functions decorated with `@st.experimental_singleton` can also contain [input widgets](/develop/api-reference/widgets)! Replaying input widgets is disabled by default. To enable it, you can set the `experimental_allow_widgets` parameter for `@st.experimental_singleton` to `True`. The example below enables widget replaying, and shows the use of a checkbox widget within a cache-decorated function.

```python
import streamlit as st

# Enable widget replay
@st.experimental_singleton(experimental_allow_widgets=True)
def func():
    # Contains an input widget
    st.checkbox("Works!")

func()
```

If the cache decorated function contains input widgets, but `experimental_allow_widgets` is set to `False` or unset, Streamlit will throw a `CachedStFunctionWarning`, like the one below:

```python
import streamlit as st

# Widget replay is disabled by default
@st.experimental_singleton
def func():
    # Streamlit will throw a CachedStFunctionWarning
    st.checkbox("Doesn't work")

func()
```

<Image src="/images/cached-st-function-warning-widgets.png" clean />

### How widget replay works

Let's demystify how widget replay in cache-decorated functions works and gain a conceptual understanding. Widget values are treated as additional inputs to the function, and are used to determine whether the function should be executed or not. Consider the following example:

```python
import streamlit as st

@st.experimental_singleton(experimental_allow_widgets=True)
def plus_one(x):
    y = x + 1
    if st.checkbox("Nuke the value ≡ƒÆÑ"):
        st.write("Value was nuked, returning 0")
        y = 0
    return y

st.write(plus_one(2))
```

The `plus_one` function takes an integer `x` as input, and returns `x + 1`. The function also contains a checkbox widget, which is used to "nuke" the value of `x`. i.e. the return value of `plus_one` depends on the state of the checkbox: if it is checked, the function returns `0`, otherwise it returns `3`.

In order to know which value the cache should return (in case of a cache hit), Streamlit treats the checkbox state (checked / unchecked) as an additional input to the function `plus_one` (just like `x`). If the user checks the checkbox (thereby changing its state), we look up the cache for the same value of `x` (2) and the same checkbox state (checked). If the cache contains a value for this combination of inputs, we return it. Otherwise, we execute the function and store the result in the cache.

Let's now understand how enabling and disabling widget replay changes the behavior of the function.

### Widget replay disabled

- Widgets in cached functions throw a `CachedStFunctionWarning` and are ignored.
- Other static elements in cached functions replay as expected.

### Widget replay enabled

- Widgets in cached functions don't lead to a warning, and are replayed as expected.
- Interacting with a widget in a cached function will cause the function to be executed again, and the cache to be updated.
- Widgets in cached functions retain their state across reruns.
- Each unique combination of widget values is treated as a separate input to the function, and is used to determine whether the function should be executed or not. i.e. Each unique combination of widget values has its own cache entry; the cached function runs the first time and the saved value is used afterwards.
- Calling a cached function multiple times in one script run with the same arguments triggers a `DuplicateWidgetID` error.
- If the arguments to a cached function change, widgets from that function that render again retain their state.
- Changing the source code of a cached function invalidates the cache.
- Both [`st.experimental_singleton`](/develop/api-reference/caching-and-state/st.experimental_singleton) and [`st.experimental_memo`](/develop/api-reference/caching-and-state/st.experimental_memo) support widget replay.
- Fundamentally, the behavior of a function with (supported) widgets in it doesn't change when it is decorated with `@st.experimental_singleton` or `@st.experimental_memo`. The only difference is that the function is only executed when we detect a cache "miss".

### Supported widgets

All input widgets are supported in cache-decorated functions. The following is an exhaustive list of supported widgets:

- `st.button`
- `st.camera_input`
- `st.checkbox`
- `st.color_picker`
- `st.date_input`
- `st.download_button`
- `st.file_uploader`
- `st.multiselect`
- `st.number_input`
- `st.radio`
- `st.selectbox`
- `st.select_slider`
- `st.slider`
- `st.text_area`
- `st.text_input`
- `st.time_input`

```

File: api-reference/caching-and-state/cache-resource.md
```

---

title: st.cache_resource
slug: /develop/api-reference/caching-and-state/st.cache_resource
description: st.cache_resource is used to cache functions that return shared global resources (e.g. database connections, ML models).

---

<Tip>

This page only contains information on the `st.cache_resource` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

</Tip>

<Autofunction function="streamlit.cache_resource" oldName="streamlit.experimental_singleton" />

<Autofunction function="streamlit.cache_resource.clear" oldName="streamlit.experimental_singleton.clear" />

#### Example

In the example below, pressing the "Clear All" button will clear _all_ cache_resource caches. i.e. Clears cached global resources from all functions decorated with `@st.cache_resource`.

```python
import streamlit as st
from transformers import BertModel

@st.cache_resource
 def get_database_session(url):
     # Create a database session object that points to the URL.
     return session

@st.cache_resource
def get_model(model_type):
    # Create a model of the specified type.
    return BertModel.from_pretrained(model_type)

if st.button("Clear All"):
    # Clears all st.cache_resource caches:
    st.cache_resource.clear()
```

## Using Streamlit commands in cached functions

### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

```python
from transformers import pipeline

@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis")
    st.success("Loaded NLP model from Hugging Face!")  # ≡ƒæê Show a success message
    return model
```

As we know, Streamlit only runs this function if it hasnΓÇÖt been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

```python
@st.cache_resource
def load_model():
    st.header("Data analysis")
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
    st.success("Loaded model!")
    st.write("Turning on evaluation mode...")
    model.eval()
    st.write("Here's the model:")
    return model
```

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

```python
@st.cache_resource(experimental_allow_widgets=True)  # ≡ƒæê Set the parameter
def load_model():
    pretrained = st.checkbox("Use pre-trained model:")  # ≡ƒæê Add a checkbox
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT, pretrained=pretrained)
    return model
```

Streamlit treats the checkbox like an additional input parameter to the cached function. If you uncheck it, Streamlit will see if it has already cached the function for this checkbox state. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then weΓÇÖll add 100 MB to the cache for _every permutation_ of these five slider values ΓÇô even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

<Warning>

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!
</Warning>

<Note>

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!
</Note>

```

File: api-reference/caching-and-state/experimental-memo.md
```

---

title: st.experimental_memo
slug: /develop/api-reference/caching-and-state/st.experimental_memo
description: st.experimental_memo is used to memoize function executions.

---

<Important>

This is an experimental feature. Experimental features and their APIs may change or be removed at any time. To learn more, click [here](/develop/quick-reference/prerelease#experimental-features).

</Important>

<Autofunction function="streamlit.experimental_memo" deprecated={true} deprecatedText="<code>st.experimental_memo</code> was deprecated in version 1.18.0. Use <a href='/develop/api-reference/caching-and-state/st.cache_data'><code>st.cache_data</code></a> instead. Learn more in <a href='/develop/concepts/architecture/caching'>Caching</a>."/>

Persistent memo caches currently don't support TTL. `ttl` will be ignored if `persist` is specified:

```python
import streamlit as st

@st.experimental_memo(ttl=60, persist="disk")
def load_data():
    return 42

st.write(load_data())
```

And a warning will be logged to your terminal:

```bash
streamlit run app.py

  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.1:8501

2022-09-22 13:35:41.587 The memoized function 'load_data' has a TTL that will be ignored. Persistent memo caches currently don't support TTL.
```

<Autofunction function="streamlit.experimental_memo.clear" deprecated={true} deprecatedText="<code>st.experimental_memo.clear</code> was deprecated in version 1.18.0. Use <a href='/develop/api-reference/caching-and-state/st.cache_data#stcache_dataclear'><code>st.cache_data.clear</code></a> instead. Learn more in <a href='/develop/concepts/architecture/caching'>Caching</a>."/>

#### Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.experimental_memo`.

```python
import streamlit as st

@st.experimental_memo
def square(x):
    return x**2

@st.experimental_memo
def cube(x):
    return x**3

if st.button("Clear All"):
    # Clear values from *all* memoized functions:
    # i.e. clear values from both square and cube
    st.experimental_memo.clear()
```

## Replay static `st` elements in cache-decorated functions

Functions decorated with `@st.experimental_memo` can contain static `st` elements. When a cache-decorated function is executed, we record the element and block messages produced, so the elements will appear in the app even when execution of the function is skipped because the result was cached.

In the example below, the `@st.experimental_memo` decorator is used to cache the execution of the `load_data` function, that returns a pandas DataFrame. Notice the cached function also contains a `st.area_chart` command, which will be replayed when the function is skipped because the result was cached.

```python
import numpy as np
import pandas as pd
import streamlit as st

@st.experimental_memo
def load_data(rows):
    chart_data = pd.DataFrame(
        np.random.randn(rows, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )
    # Contains a static element st.area_chart
    st.area_chart(chart_data) # This will be recorded and displayed even when the function is skipped
    return chart_data

df = load_data(20)
st.dataframe(df)
```

<Image src="/images/replay-cached-elements.png" clean />

Supported static `st` elements in cache-decorated functions include:

- `st.alert`
- `st.altair_chart`
- `st.area_chart`
- `st.audio`
- `st.bar_chart`
- `st.ballons`
- `st.bokeh_chart`
- `st.caption`
- `st.code`
- `st.components.v1.html`
- `st.components.v1.iframe`
- `st.container`
- `st.dataframe`
- `st.echo`
- `st.empty`
- `st.error`
- `st.exception`
- `st.expander`
- `st.experimental_get_query_params`
- `st.experimental_set_query_params`
- `st.form`
- `st.form_submit_button`
- `st.graphviz_chart`
- `st.help`
- `st.image`
- `st.info`
- `st.json`
- `st.latex`
- `st.line_chart`
- `st.markdown`
- `st.metric`
- `st.plotly_chart`
- `st.progress`
- `st.pydeck_chart`
- `st.snow`
- `st.spinner`
- `st.success`
- `st.table`
- `st.text`
- `st.vega_lite_chart`
- `st.video`
- `st.warning`

## Replay input widgets in cache-decorated functions

In addition to static elements, functions decorated with `@st.experimental_memo` can also contain [input widgets](/develop/api-reference/widgets)! Replaying input widgets is disabled by default. To enable it, you can set the `experimental_allow_widgets` parameter for `@st.experimental_memo` to `True`. The example below enables widget replaying, and shows the use of a checkbox widget within a cache-decorated function.

```python
import streamlit as st

# Enable widget replay
@st.experimental_memo(experimental_allow_widgets=True)
def func():
    # Contains an input widget
    st.checkbox("Works!")

func()
```

If the cache decorated function contains input widgets, but `experimental_allow_widgets` is set to `False` or unset, Streamlit will throw a `CachedStFunctionWarning`, like the one below:

```python
import streamlit as st

# Widget replay is disabled by default
@st.experimental_memo
def func():
    # Streamlit will throw a CachedStFunctionWarning
    st.checkbox("Doesn't work")

func()
```

<Image src="/images/cached-st-function-warning-widgets.png" clean />

### How widget replay works

Let's demystify how widget replay in cache-decorated functions works and gain a conceptual understanding. Widget values are treated as additional inputs to the function, and are used to determine whether the function should be executed or not. Consider the following example:

```python
import streamlit as st

@st.experimental_memo(experimental_allow_widgets=True)
def plus_one(x):
    y = x + 1
    if st.checkbox("Nuke the value ≡ƒÆÑ"):
        st.write("Value was nuked, returning 0")
        y = 0
    return y

st.write(plus_one(2))
```

The `plus_one` function takes an integer `x` as input, and returns `x + 1`. The function also contains a checkbox widget, which is used to "nuke" the value of `x`. i.e. the return value of `plus_one` depends on the state of the checkbox: if it is checked, the function returns `0`, otherwise it returns `3`.

In order to know which value the cache should return (in case of a cache hit), Streamlit treats the checkbox state (checked / unchecked) as an additional input to the function `plus_one` (just like `x`). If the user checks the checkbox (thereby changing its state), we look up the cache for the same value of `x` (2) and the same checkbox state (checked). If the cache contains a value for this combination of inputs, we return it. Otherwise, we execute the function and store the result in the cache.

Let's now understand how enabling and disabling widget replay changes the behavior of the function.

### Widget replay disabled

- Widgets in cached functions throw a `CachedStFunctionWarning` and are ignored.
- Other static elements in cached functions replay as expected.

### Widget replay enabled

- Widgets in cached functions don't lead to a warning, and are replayed as expected.
- Interacting with a widget in a cached function will cause the function to be executed again, and the cache to be updated.
- Widgets in cached functions retain their state across reruns.
- Each unique combination of widget values is treated as a separate input to the function, and is used to determine whether the function should be executed or not. i.e. Each unique combination of widget values has its own cache entry; the cached function runs the first time and the saved value is used afterwards.
- Calling a cached function multiple times in one script run with the same arguments triggers a `DuplicateWidgetID` error.
- If the arguments to a cached function change, widgets from that function that render again retain their state.
- Changing the source code of a cached function invalidates the cache.
- Both [`st.experimental_memo`](/develop/api-reference/caching-and-state/st.experimental_memo) and [`st.experimental_singleton`](/develop/api-reference/caching-and-state/st.experimental_singleton) support widget replay.
- Fundamentally, the behavior of a function with (supported) widgets in it doesn't change when it is decorated with `@st.experimental_memo` or `@st.experimental_singleton`. The only difference is that the function is only executed when we detect a cache "miss".

### Supported widgets

All input widgets are supported in cache-decorated functions. The following is an exhaustive list of supported widgets:

- `st.button`
- `st.camera_input`
- `st.checkbox`
- `st.color_picker`
- `st.date_input`
- `st.download_button`
- `st.file_uploader`
- `st.multiselect`
- `st.number_input`
- `st.radio`
- `st.selectbox`
- `st.select_slider`
- `st.slider`
- `st.text_area`
- `st.text_input`
- `st.time_input`

```

File: api-reference/caching-and-state/_index.md
```

---

title: Caching and state
slug: /develop/api-reference/caching-and-state

---

# Caching and state

Optimize performance and add statefulness to your app!

## Caching

Streamlit provides powerful [cache primitives](/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

<TileContainer>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_data" size="half">

<h4>Cache data</h4>

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.cache_resource" size="half">

<h4>Cache resource</h4>

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>

</TileContainer>

## Manage state

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.session_state" size="half" >

<h4>Session State</h4>

Save data between reruns and across pages.

```python
st.session_state["foo"] = "bar"
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.query_params" size="half">

<h4>Query parameters</h4>

Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

</RefCard>

</TileContainer>

## Deprecated commands

<TileContainer>

<RefCard href="/develop/api-reference/caching-and-state/st.cache" deprecated={true}>

> This command was deprecated in version 1.18.0. Use `st.cache_data` or `st.cache_resource` instead.

<h4>Caching</h4>

Function decorator to memoize function executions.

```python
@st.cache(ttl=3600)
def run_long_computation(arg1, arg2):
  # Do stuff here
  return computation_output
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.experimental_memo" deprecated={true}>

> This command was deprecated in version 1.18.0. Use `st.cache_data` instead.

<h4>Memo</h4>

Experimental function decorator to memoize function executions.

```python
@st.experimental_memo
def fetch_and_clean_data(url):
  # Fetch data from URL here, and then clean it up.
  return data
```

</RefCard>

<RefCard href="/develop/api-reference/caching-and-state/st.experimental_singleton" deprecated={true}>

> This command was deprecated in version 1.18.0. Use `st.cache_resource` instead.

<h4>Singleton</h4>

Experimental function decorator to store singleton objects.

```python
@st.experimental_singleton
def get_database_session(url):
  # Create a database session object that points to the URL.
  return session
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_get_query_params" size="half" deprecated={true}>

<h4>Get query parameters</h4>

Get query parameters that are shown in the browser's URL bar.

```python
param_dict = st.experimental_get_query_params()
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_set_query_params" size="half" deprecated={true}>

<h4>Set query parameters</h4>

Set query parameters that are shown in the browser's URL bar.

```python
st.experimental_set_query_params(
  {"show_all"=True, "selected"=["asia", "america"]}
)
```

</RefCard>
</TileContainer>

```

File: api-reference/caching-and-state/session_state.md
```

---

title: Session State
slug: /develop/api-reference/caching-and-state/st.session_state
description: st.session_state is a way to share variables between reruns, for each user session.

---

# Session State

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks. Session state also persists across apps inside a [multipage app](/develop/concepts/multipage-apps).

Check out this Session State basics tutorial video by Streamlit Developer Advocate Dr. Marisa Smith to get started:

<YouTube videoId="92jUAXBmZyU" />

### Initialize values in Session State

The Session State API follows a field-based API, which is very similar to Python dictionaries:

```python
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
```

### Reads and updates

Read the value of an item in Session State and display it by passing to `st.write` :

```python
# Read
st.write(st.session_state.key)

# Outputs: value
```

Update an item in Session State by assigning it a value:

```python
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API
```

Curious about what is in Session State? Use `st.write` or magic:

```python
st.write(st.session_state)

# With magic:
st.session_state
```

Streamlit throws a handy exception if an uninitialized variable is accessed:

```python
st.write(st.session_state['value'])

# Throws an exception!
```

![state-uninitialized-exception](/images/state_uninitialized_exception.png)

### Delete items

Delete items in Session State using the syntax to delete items in any Python dictionary:

```python
# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]
```

Session State can also be cleared by going to Settings ΓåÆ Clear Cache, followed by Rerunning the app.

![state-clear-cache](/images/clear_cache.png)

### Session State and Widget State association

Every widget with a key is automatically added to Session State:

```python
st.text_input("Your name", key="name")

# This exists now:
st.session_state.name
```

### Use Callbacks to update Session State

A callback is a python function which gets called when an input widget changes.

**Order of execution**: When updating Session state in response to **events**, a callback function gets executed first, and then the app is executed from top to bottom.

Callbacks can be used with widgets using the parameters `on_change` (or `on_click`), `args`, and `kwargs`:

**Parameters**

- **on_change** or **on_click** - The function name to be used as a callback
- **args** (_tuple_) - List of arguments to be passed to the callback function
- **kwargs** (_dict_) - Named arguments to be passed to the callback function

Widgets which support the `on_change` event:

- `st.checkbox`
- `st.color_picker`
- `st.date_input`
- `st.data_editor`
- `st.file_uploader`
- `st.multiselect`
- `st.number_input`
- `st.radio`
- `st.select_slider`
- `st.selectbox`
- `st.slider`
- `st.text_area`
- `st.text_input`
- `st.time_input`
- `st.toggle`

Widgets which support the `on_click` event:

- `st.button`
- `st.download_button`
- `st.form_submit_button`

To add a callback, define a callback function **above** the widget declaration and pass it to the widget via the `on_change` (or `on_click` ) parameter.

### Forms and Callbacks

Widgets inside a form can have their values be accessed and set via the Session State API. `st.form_submit_button` can have a callback associated with it. The callback gets executed upon clicking on the submit button. For example:

```python
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
```

### Serializable Session State

Serialization refers to the process of converting an object or data structure into a format that can be persisted and shared, and allowing you to recover the dataΓÇÖs original structure. PythonΓÇÖs built-in [pickle](https://docs.python.org/3/develop/pickle.html) module serializes Python objects to a byte stream ("pickling") and deserializes the stream into an object ("unpickling").

By default, StreamlitΓÇÖs [Session State](/develop/concepts/architecture/session-state) allows you to persist any Python object for the duration of the session, irrespective of the objectΓÇÖs pickle-serializability. This property lets you store Python primitives such as integers, floating-point numbers, complex numbers and booleans, dataframes, and even [lambdas](https://docs.python.org/3/reference/expressions.html#lambda) returned by functions. However, some execution environments may require serializing all data in Session State, so it may be useful to detect incompatibility during development, or when the execution environment will stop supporting it in the future.

To that end, Streamlit provides a `runner.enforceSerializableSessionState` [configuration option](/develop/concepts/configuration) that, when set to `true`, only allows pickle-serializable objects in Session State. To enable the option, either create a global or project config file with the following or use it as a command-line flag:

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

By "_pickle-serializable_", we mean calling `pickle.dumps(obj)` should not raise a [`PicklingError`](https://docs.python.org/3/develop/pickle.html#pickle.PicklingError) exception. When the config option is enabled, adding unserializable data to session state should result in an exception. E.g.,

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#≡ƒæç results in an exception when enforceSerializableSessionState is on
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png" clean />

<Warning>

When `runner.enforceSerializableSessionState` is set to `true`, Session State implicitly uses the `pickle` module, which is known to be insecure. Ensure all data saved and retrieved from Session State is trusted because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

### Caveats and limitations

- Only the `st.form_submit_button` has a callback in forms. Other widgets inside a form are not allowed to have callbacks.
- `on_change` and `on_click` events are only supported on input type widgets.
- Modifying the value of a widget via the Session state API, after instantiating it, is not allowed and will raise a `StreamlitAPIException`. For example:

  ```python
  slider = st.slider(
      label='My Slider', min_value=1,
      max_value=10, value=5, key='my_slider')

  st.session_state.my_slider = 7

  # Throws an exception!
  ```

  ![state-modified-instantiated-exception](/images/state_modified_instantiated_exception.png)

- Setting the widget state via the Session State API and using the `value` parameter in the widget declaration is not recommended, and will throw a warning on the first run. For example:

  ```python
  st.session_state.my_slider = 7

  slider = st.slider(
      label='Choose a Value', min_value=1,
      max_value=10, value=5, key='my_slider')
  ```

  ![state-value-api-exception](/images/state_value_api_exception.png)

- Setting the state of button-like widgets: `st.button`, `st.download_button`, and `st.file_uploader` via the Session State API is not allowed. Such type of widgets are by default _False_ and have ephemeral _True_ states which are only valid for a single run. For example:

  ```python
  if 'my_button' not in st.session_state:
      st.session_state.my_button = True

  st.button('My button', key='my_button')

  # Throws an exception!
  ```

  ![state-button-exception](/images/state_button_exception.png)

```

File: api-reference/caching-and-state/experimental_set_query_params.md
```

---

title: st.experimental_set_query_params
slug: /develop/api-reference/caching-and-state/st.experimental_set_query_params
description: st.experimental_set_query_params sets query parameters shown in the browser's URL bar.

---

<Autofunction function="streamlit.experimental_set_query_params" deprecated={true} deprecatedText="<code>st.experimental_set_query_params</code> was deprecated in version 1.30.0. Use <a href='/develop/api-reference/caching-and-state/st.query_params'><code>st.query_params</code></a> instead." />

```

File: api-reference/custom-components/iframe.md
```

---

title: st.components.v1.iframe
slug: /develop/api-reference/custom-components/st.components.v1.iframe

---

<Autofunction function="streamlit.components.v1.iframe" />

#### Example

```python
import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://example.com", height=500)
```

```

File: api-reference/custom-components/declare_component.md
```

---

title: st.components.v1.declare_component
slug: /develop/api-reference/custom-components/st.components.v1.declare_component

---

<Autofunction function="streamlit.components.v1.declare_component" />

```

File: api-reference/custom-components/_index.md
```

---

title: Custom components
slug: /develop/api-reference/custom-components

---

# Custom components

<TileContainer>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.declare_component">

<h4>Declare a component</h4>

Create and register a custom component.

```python
st.components.v1.declare_component(
    "custom_slider",
    "/frontend",
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.html">

<h4>HTML</h4>

Display an HTML string in an iframe.

```python
st.components.v1.html(
    "<p>Foo bar.</p>"
)
```

</RefCard>

<RefCard href="/develop/api-reference/custom-components/st.components.v1.iframe">

<h4>iframe</h4>

Load a remote URL in an iframe.

```python
st.components.v1.iframe(
    "docs.streamlit.io"
)
```

</RefCard>

</TileContainer>

```

File: api-reference/custom-components/html.md
```

---

title: st.components.v1.html
slug: /develop/api-reference/custom-components/st.components.v1.html

---

<Autofunction function="streamlit.components.v1.html" />

#### Example

```python
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
```

```

File: concepts/_index.md
```

---

title: Development concepts
slug: /develop/concepts

---

# Development concepts

This section gives you background on how different parts of Streamlit work.

<TileContainer>

<RefCard href="/develop/concepts/architecture" size="half">

<h5>Streamlit's architecture and execution model</h5>

Streamlit's execution model makes it easy to turn your scripts into beautiful, interactive web apps.

- Understand how to run your app.
- Understand Streamlit's execution and client-server model.
- Understand the primary tools to work with Streamlit reruns.

</RefCard>

<RefCard href="/develop/concepts/multipage-apps" size="half">

<h5>Multipage apps</h5>

Streamlit provides an automated way to build multipage apps through directory structure.

- Learn how to structure and configure your multipage app.

</RefCard>

<RefCard href="/develop/concepts/design" size="half">

<h5>App design considerations</h5>

Bring together Streamlit's architecture and execution model to design your app. Work with Streamlit commands to render dynamic and
interactic content for your users.

- Learn how to make your apps performant and easy-to-manage.
- Learn how to structure and design your project.

</RefCard>

<RefCard href="/develop/concepts/connections" size="half">

<h5>Connections and secrets</h5>

- Learn how to manage connections and secrets with Streamlit's convenient, built-in features.

</RefCard>

<RefCard href="/develop/concepts/custom-components" size="half">

<h5>Creating custom components</h5>

Custom components extend Streamlit's functionality.

- Learn how to build your own custom component.
- Learn how install a third-party component.

</RefCard>

<RefCard href="/develop/concepts/configuration" size="half">

<h5>Configuration and theming</h5>

Streamlit provides a variety options to customize and configure your app.

- Learn how to work with configuration options, including server settings, client settings, and theming.

</RefCard>

<RefCard href="/develop/concepts/app-testing" size="half">

<h5>App testing</h5>

Streamlit app testing enables developers to build and run automated tests. Bring your favorite test automation software and enjoy simple syntax to simulate user input and inspect rendered output.

</RefCard>
</TileContainer>

```

File: concepts/multipage-apps/_index.md
```

---

title: Multipage apps
slug: /develop/concepts/multipage-apps
description: Streamlit provides a simple way to create multipage apps.

---

# Multipage apps

<TileContainer layout="list">

<RefCard href="/develop/concepts/multipage-apps/pages-directory">

<h5>Creating multipage apps using the <code>pages/</code> directory (MPA v1)</h5>

Streamlit provides a frictionless way to create multipage apps. Place additional Python files in a `pages/` directory alongside your entrypoint file and pages are automatically shown in a navigation widget inside your app's sidebar.

</RefCard>

</TileContainer>

```

File: concepts/multipage-apps/page_directory.md
```

---

title: Creating multipage apps using the `pages/` directory
slug: /develop/concepts/multipage-apps/pages-directory
description: Streamlit provides a simple way to create multipage apps.

---

# Creating multipage apps using the `pages/` directory

As your app grows large, it becomes useful to organize your script into multiple pages. This makes your app easier to manage as a developer and easier to navigate as a user. Streamlit provides a frictionless way to create multipage apps. Pages are automatically shown in a navigation widget inside your app's sidebar. If a user clicks on a page in the sidebar, Streamlit navigates to that page without reloading the frontend ΓÇö making app browsing incredibly fast! In this guide, letΓÇÖs learn how to create multipage apps.

## Structuring your multipage app

Streamlit identifies pages in a multipage app by directory structure and filenames. The file you pass to `streamlit run` is called your entrypoint file. This is your app's homepage. When you have a `pages/` directory next to your entrypoint file, Streamlit will identify each Python file within it as a page. The following example has three pages. `your_homepage.py` is the entrypoint file and homepage.

```
your_working_directory/
Γö£ΓöÇΓöÇ pages/
Γöé   Γö£ΓöÇΓöÇ a_page.py
Γöé   ΓööΓöÇΓöÇ another_page.py
ΓööΓöÇΓöÇ your_homepage.py
```

Run your multipage app just like you would for a single-page app. Pass your entrypoint file to `streamlit run`.

```
streamlit run your_homepage.py
```

Only `.py` files in the `pages/` directory will be identified as pages. Streamlit ignores all other files in the `pages/` directory and its subdirectories. Streamlit also ignores Python files in subdirectories of `pages/`.

Keep reading to learn how filenames are displayed and ordered in your app's navigation.

## Naming and ordering your pages

The entrypoint file is your app's homepage and the first page users will see when visiting your app. Once you've added pages to your app, the entrypoint file appears as the topmost page in the sidebar. Streamlit determines the page label and ordering of each page from your filenames. Labels may differ from the page title set in [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config).

### Filenames for pages

Filenames are composed of four different parts as follows:

1. `number`. A non-negative integer.
2. `separator`. Any combination of underscore (`"_"`), dash (`"-"`), and space (`" "`).
3. `label`. Everything up to, but not including, `".py"`.
4. `".py"`

### How Streamlit converts filenames into page labels

Streamlit displays page labels as follows:

1. If your filename contains a `label`, Streamlit displays the `label` in the left navigation. Any underscores within the page's `label` are treated as spaces.
2. If your filename contains a `number` but does not contain a `label`, Streamlit displays the `number` instead.
3. If your filename contains only a `separator` with no `number` and no `label`, Streamlit will not display the page in the sidebar navigation.

The following filenames would all display as "Awesome homepage" in the sidebar navigation.

- `"Awesome homepage.py"`
- `"Awesome_homepage.py"`
- `"02Awesome_homepage.py"`
- `"--Awesome_homepage.py"`
- `"1_Awesome_homepage.py"`
- `"33 - Awesome homepage.py"`

### How pages are sorted in the sidebar

The entrypoint file is always displayed first. The remaining pages are sorted as follows:

- Files that have a `number` appear before files without a `number`.
- Files are sorted based on the `number` (if any), followed by the `label` (if any).
- When files are sorted, Streamlit treats the `number` as an actual number rather than a string. So `03` is the same as `3`.

This table shows examples of filenames and their corresponding labels, sorted by the order in which they appear in the sidebar.

**Examples**:

| **Filename**              | **Rendered label** |
| :------------------------ | :----------------- |
| `1 - first page.py`       | first page         |
| `12 monkeys.py`           | monkeys            |
| `123.py`                  | 123                |
| `123_hello_dear_world.py` | hello dear world   |
| `_12 monkeys.py`          | 12 monkeys         |

<Tip>

Emojis can be used to make your page names more fun! For example, a file named `≡ƒÅá_Home.py` will create a page titled "≡ƒÅá Home" in the sidebar. When adding emojis to filenames, itΓÇÖs best practice to include a numbered prefix to make autocompletion in your terminal easier. Terminal-autocomplete can get confused by unicode (which is how emojis are represented).

</Tip>

## Navigating between pages

Pages are automatically shown in a sidebar navigation UI. When a user clicks on a page in the sidebar UI, Streamlit navigates to that page without reloading the entire frontend ΓÇö making app browsing incredibly fast! Optionally, you can hide the default navigation UI and build your own with [`st.page_link`](/develop/api-reference/widgets/st.page_link). For more information, see [Build a custom navigation menu with `st.page_link`](/develop/tutorials/multipage/st.page_link-nav).

If you need to programmatically switch pages, use [`st.switch_page`](/develop/api-reference/navigation/st.switch_page).

Users can also navigate between pages using URLs. Pages have their own URLs, defined by the file's `label`. When multiple files have the same `label`, Streamlit picks the first one (based on the ordering [described above](#how-pages-are-sorted-in-the-sidebar)). Users can view a specific page by visiting the page's URL.

<Important>

Navigating between pages by URL creates a new browser session and clears `st.session_state`. In particular, clicking markdown links to other
pages resets `st.session_state`. In order to retain values in `st.session_state`, a user must use the sidebar navigation or other Streamlit
widgets to switch pages.

</Important>

If a user tries to access a URL for a page that does not exist, they will see a modal like the one below, saying the user has requested a page that was not found in the appΓÇÖs `pages/` directory.

<Image src="/images/mpa-page-not-found.png" />

## Notes and limitations

- Pages support run-on-save.
  - When you update a page while your app is running, this causes a rerun for users currently viewing that exact page.
  - When you update a page while your app is running, the app will not automatically rerun for users currently viewing a different page.
- While your app is running, adding or deleting a page updates the sidebar navigation immediately.
- [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) works at the page level.
  - When you set `title` or `favicon` using `st.set_page_config`, this applies to the current page only.
  - When you set `layout` using `st.set_page_config`, the setting will remain for the session until changed by another call to `st.set_page_config`. If you use `st.set_page_config` to set `layout`, it's recommended to call it on _all_ pages.
- Pages share the same Python modules globally:

  ```python
  # page1.py
  import foo
  foo.hello = 123

  # page2.py
  import foo
  st.write(foo.hello)  # If page1 already executed, this writes 123
  ```

- Pages share the same [st.session_state](/develop/concepts/architecture/session-state):

  ```python
  # page1.py
  import streamlit as st
  if "shared" not in st.session_state:
     st.session_state["shared"] = True

  # page2.py
  import streamlit as st
  st.write(st.session_state["shared"]) # If page1 already executed, this writes True
  ```

You now have a solid understanding of multipage apps. You've learned how to structure apps, define pages, and navigate between pages in the user interface. It's time to [create your first multipage app](/get-started/tutorials/create-a-multipage-app)! ≡ƒÑ│

```

File: concepts/connections/secrets-management.md
```

---

title: Secrets management
slug: /develop/concepts/connections/secrets-management

---

# Secrets management

Storing unencrypted secrets in a git repository is a bad practice. For applications that require access to sensitive credentials, the recommended solution is to store those credentials outside the repository - such as using a credentials file not committed to the repository or passing them as environment variables.

Streamlit provides native file-based secrets management to easily store and securely access your secrets in your Streamlit app.

<Note>

Existing secrets management tools, such as [dotenv files](https://pypi.org/project/python-dotenv/), [AWS credentials files](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials), [Google Cloud Secret Manager](https://pypi.org/project/google-cloud-secret-manager/), or [Hashicorp Vault](https://www.vaultproject.io/use-cases/secrets-management), will work fine in Streamlit. We just add native secrets management for times when it's useful.

</Note>

## How to use secrets management

### Develop locally and set up secrets

Streamlit provides two ways to set up secrets locally using┬á[TOML](https://toml.io/en/latest)┬áformat:

1. In a **global secrets file** at `~/.streamlit/secrets.toml` for macOS/Linux or `%userprofile%/.streamlit/secrets.toml` for Windows:

   ```toml
   # Everything in this section will be available as an environment variable
   db_username = "Jane"
   db_password = "mypassword"

   # You can also add other sections if you like.
   # The contents of sections as shown below will not become environment variables,
   # but they'll be easily accessible from within Streamlit anyway as we show
   # later in this doc.
   [my_other_secrets]
   things_i_like = ["Streamlit", "Python"]
   ```

   If you use the global secrets file, you don't have to duplicate secrets across several project-level files if multiple Streamlit apps share the same secrets.

2. In a **per-project secrets file** at `$CWD/.streamlit/secrets.toml`, where `$CWD` is the folder you're running Streamlit from. If both a global secrets file and a per-project secrets file exist, _secrets in the per-project file overwrite those defined in the global file_.

<Important>

Add this file to your `.gitignore` so you don't commit your secrets!

</Important>

### Use secrets in your app

Access your secrets by querying the┬á`st.secrets`┬ádict, or as environment variables. For example, if you enter the secrets from the section above, the code below shows you how to access them within your Streamlit app.

```python
import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
```

<Tip>

You can access `st.secrets` via attribute notation (e.g. `st.secrets.key`), in addition to key notation (e.g. `st.secrets["key"]`) ΓÇö like [st.session_state](/develop/api-reference/caching-and-state/st.session_state).

</Tip>

You can even compactly use TOML sections to pass multiple secrets as a single attribute. Consider the following secrets:

```toml
[db_credentials]
username = "my_username"
password = "my_password"
```

Rather than passing each secret as attributes in a function, you can more compactly pass the section to achieve the same result. See the notional code below, which uses the secrets above:

```python
# Verbose version
my_db.connect(username=st.secrets.db_credentials.username, password=st.secrets.db_credentials.password)

# Far more compact version!
my_db.connect(**st.secrets.db_credentials)
```

### Error handling

Here are some common errors you might encounter when using secrets management.

- If a `.streamlit/secrets.toml` is created _while_ the app is running, the server needs to be restarted for changes to be reflected in the app.
- If you try accessing a secret, but no `secrets.toml` file exists, Streamlit will raise a `FileNotFoundError` exception:
  <Image alt="Secrets management FileNotFoundError" src="/images/secrets-filenotfounderror.png" clean />
- If you try accessing a secret that doesn't exist, Streamlit will raise a `KeyError` exception:

  ```python
  import streamlit as st

  st.write(st.secrets["nonexistent_key"])
  ```

    <Image alt="Secrets management KeyError" src="/images/secrets-keyerror.png" clean />

### Use secrets on Streamlit Community Cloud

When you deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud), you can use the same secrets management workflow as you would locally. However, you'll need to also set up your secrets in the Community Cloud Secrets Management console. Learn how to do so via the Cloud-specific [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) documentation.

```

File: concepts/connections/_index.md
```

---

title: Working with connections and secrets
slug: /develop/concepts/connections

---

# Working with connections and secrets

<TileContainer layout="list">

<RefCard href="/develop/concepts/connections/connecting-to-data">

<h5>Connecting to data</h5>

Connect your app to remote data or a third-party API.

</RefCard>

<RefCard href="/develop/concepts/connections/secrets-management">

<h5>Secrets managements</h5>

Set up your development environement and design your app to handle secrets securely.

</RefCard>

<RefCard href="/develop/concepts/connections/security-reminders">

<h5>Security reminders</h5>

Check out a few reminders to follow best practices and avoid security mistakes.

</RefCard>

</TileContainer>

```

File: concepts/connections/connecting-to-data.md
```

---

title: Connecting to data
slug: /develop/concepts/connections/connecting-to-data

---

# Connecting to data

Most Streamlit apps need some kind of data or API access to be useful - either retrieving data to view or saving the results of some user action. This data or API is often part of some remote service, database, or other data source.

**Anything you can do with Python, including data connections, will generally work in Streamlit**. Streamlit's [tutorials](/develop/tutorials/databases) are a great starting place for many data sources. However:

- Connecting to data in a Python application is often tedious and annoying.
- There are specific considerations for connecting to data from streamlit apps, such as caching and secrets management.

**Streamlit provides [`st.connection()`](/develop/api-reference/connections/st.connection) to more easily connect your Streamlit apps to data and APIs with just a few lines of code**. This page provides a basic example of using the feature and then focuses on advanced usage.

For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience. You'll learn about the feature's utility in creating and managing data connections within your apps by using real-world examples.

<YouTube videoId="xQwDfW7UHMo" />

## Basic usage

For basic startup and usage examples, read up on the relevant [data source tutorial](/develop/tutorials/databases). Streamlit has built-in connections to SQL dialects and Snowflake. We also maintain installable connections for [Cloud File Storage](https://github.com/streamlit/files-connection) and [Google Sheets](https://github.com/streamlit/gsheets-connection).

If you are just starting, the best way to learn is to pick a data source you can access and get a minimal example working from one of the pages above ≡ƒæå. Here, we will provide an ultra-minimal usage example for using a SQLite database. From there, the rest of this page will focus on advanced usage.

### A simple starting point - using a local SQLite database

A [local SQLite database](https://sqlite.org/index.html) could be useful for your app's semi-persistent data storage.

<Note>

Community Cloud apps do not guarantee the persistence of local file storage, so the platform may delete data stored using this technique at any time.

</Note>

To see the example below running live, check out the interactive demo below:

<Cloud src="https://experimental-connection.streamlit.app/SQL?embed=true" />

#### Step 1: Install prerequisite library - SQLAlchemy

All SQLConnections in Streamlit use SQLAlchemy. For most other SQL dialects, you also need to install the driver. But the [SQLite driver ships with python3](https://docs.python.org/3/develop/sqlite3.html), so it isn't necessary.

```bash
pip install SQLAlchemy==1.4.0
```

#### Step 2: Set a database URL in your Streamlit secrets.toml file

Create a directory and file `.streamlit/secrets.toml` in the same directory your app will run from. Add the following to the file.

```toml
# .streamlit/secrets.toml

[connections.pets_db]
url = "sqlite:///pets.db"
```

#### Step 3: Use the connection in your app

The following app creates a connection to the database, uses it to create a table and insert some data, then queries the data back and displays it in a data frame.

```python
# streamlit_app.py

import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
    s.execute('DELETE FROM pet_owners;')
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(
            'INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);',
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

In this example, we didn't set a `ttl=` value on the call to [`conn.query()`](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionquery), meaning Streamlit caches the result indefinitely as long as the app server runs.

Now, on to more advanced topics! ≡ƒÜÇ

## Advanced topics

### Global secrets, managing multiple apps and multiple data stores

Streamlit [supports a global secrets file](/develop/concepts/connections/secrets-management) specified in the user's home directory, such as `~/.streamlit/secrets.toml`. If you build or manage multiple apps, we recommend using a global credential or secret file for local development across apps. With this approach, you only need to set up and manage your credentials in one place, and connecting a new app to your existing data sources is effectively a one-liner. It also reduces the risk of accidentally checking in your credentials to git since they don't need to exist in the project repository.

For cases where you have multiple similar data sources that you connect to during local development (such as a local vs. staging database), you can define different connection sections in your secrets or credentials file for different environments and then decide which to use at runtime. `st.connection` supports this with the _`name=env:<MY_NAME_VARIABLE>`_ syntax.

E.g., say I have a local and a staging MySQL database and want to connect my app to either at different times. I could create a global secrets file like this:

```toml
# ~/.streamlit/secrets.toml

[connections.local]
url = "mysql://me:****@localhost:3306/local_db"

[connections.staging]
url = "mysql://jdoe:******@staging.acmecorp.com:3306/staging_db"
```

Then I can configure my app connection to take its name from a specified environment variable

```python
# streamlit_app.py
import streamlit as st

conn = st.connection("env:DB_CONN", "sql")
df = conn.query("select * from mytable")
# ...
```

Now I can specify whether to connect to local or staging at runtime by setting the `DB_CONN` environment variable.

```bash
# connect to local
DB_CONN=local streamlit run streamlit_app.py

# connect to staging
DB_CONN=staging streamlit run streamlit_app.py
```

### Advanced SQLConnection configuration

The [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) configuration uses SQLAlchemy `create_engine()` function. It will take a single URL argument or attempt to construct a URL from several parts (username, database, host, and so on) using [`SQLAlchemy.engine.URL.create()`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.engine.URL.create).

Several popular SQLAlchemy dialects, such as Snowflake and Google BigQuery, can be configured using additional arguments to `create_engine()` besides the URL. These can be passed as `**kwargs` to the [st.connection](/develop/api-reference/connections/st.connection) call directly or specified in an additional secrets section called `create_engine_kwargs`.

E.g. snowflake-sqlalchemy takes an additional [`connect_args`](https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine.params.connect_args) argument as a dictionary for configuration that isnΓÇÖt supported in the URL. These could be specified as follows:

```toml
# .streamlit/secrets.toml

[connections.snowflake]
url = "snowflake://<user_login_name>@<account_identifier>/"

[connections.snowflake.create_engine_kwargs.connect_args]
authenticator = "externalbrowser"
warehouse = "xxx"
role = "xxx"
```

```python
# streamlit_app.py

import streamlit as st

# url and connect_args from secrets.toml above are picked up and used here
conn = st.connection("snowflake", "sql")
# ...
```

Alternatively, this could be specified entirely in `**kwargs`.

```python
# streamlit_app.py

import streamlit as st

# secrets.toml is not needed
conn = st.connection(
    "snowflake",
    "sql",
    url = "snowflake://<user_login_name>@<account_identifier>/",
    connect_args = dict(
        authenticator = "externalbrowser",
        warehouse = "xxx",
        role = "xxx",
    )
)
# ...
```

You can also provide both kwargs and secrets.toml values, and they will be merged (typically, kwargs take precedence).

### Connection considerations in frequently used or long-running apps

By default, connection objects are cached without expiration using [`st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource). In most cases this is desired. You can do `st.connection('myconn', type=MyConnection, ttl=<N>)` if you want the connection object to expire after some time.

Many connection types are expected to be long-running or completely stateless, so expiration is unnecessary. Suppose a connection becomes stale (such as a cached token expiring or a server-side connection being closed). In that case, every connection has a `reset()` method, which will invalidate the cached version and cause Streamlit to recreate the connection the next time it is retrieved

Convenience methods like `query()` and `read()` will typically cache results by default using [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) without an expiration. When an app can run many different read operations with large results, it can cause high memory usage over time and results to become stale in a long-running app, the same as with any other usage of `st.cache_data`. For production use cases, we recommend setting an appropriate `ttl` on these read operations, such as `conn.read('path/to/file', ttl="1d")`. Refer to [Caching](/develop/concepts/architecture/caching) for more information.

For apps that could get significant concurrent usage, ensure that you understand any thread safety implications of your connection, particularly when using a connection built by a third party. Connections built by Streamlit should provide thread-safe operations by default.

### Build your own connection

Building your own basic connection implementation using an existing driver or SDK is quite straightforward in most cases. However, you can add more complex functionality with further effort. This custom implementation can be a great way to extend support to a new data source and contribute to the Streamlit ecosystem.

Maintaining a tailored internal Connection implementation across many apps can be a powerful practice for organizations with frequently used access patterns and data sources.

Check out the [Build your own Connection page](https://experimental-connection.streamlit.app/Build_your_own) in the st.experimental connection demo app below for a quick tutorial and working implementation. This demo builds a minimal but very functional Connection on top of DuckDB.

<Cloud src="https://experimental-connection.streamlit.app/Build_your_own?embed=true" />

The typical steps are:

1. Declare the Connection class, extending [`ExperimentalBaseConnection`](/develop/api-reference/connections/st.connections.experimentalbaseconnection) with the type parameter bound to the underlying connection object:

   ```python
   from streamlit.connections import ExperimentalBaseConnection
   import duckdb

   class DuckDBConnection(ExperimentalBaseConnection[duckdb.DuckDBPyConnection])
   ```

2. Implement the `_connect` method that reads any kwargs, external config/credential locations, and Streamlit secrets to initialize the underlying connection:

   ```python
   def _connect(self, **kwargs) -> duckdb.DuckDBPyConnection:
       if 'database' in kwargs:
           db = kwargs.pop('database')
       else:
           db = self._secrets['database']
       return duckdb.connect(database=db, **kwargs)
   ```

3. Add useful helper methods that make sense for your connection (wrapping them in `st.cache_data` where caching is desired)

### Connection-building best practices

We recommend applying the following best practices to make your Connection consistent with the Connections built into Streamlit and the wider Streamlit ecosystem. These practices are especially important for Connections that you intend to distribute publicly.

1. **Extend existing drivers or SDKs, and default to semantics that makes sense for their existing users.**

   You should rarely need to implement complex data access logic from scratch when building a Connection. Use existing popular Python drivers and clients whenever possible. Doing so makes your Connection easier to maintain, more secure, and enables users to get the latest features. E.g. [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection) extends SQLAlchemy, [FileConnection](https://github.com/streamlit/files-connection) extends [fsspec](https://filesystem-spec.readthedocs.io/en/latest/), [GsheetsConnection](https://github.com/streamlit/gsheets-connection) extends [gspread](https://docs.gspread.org/en/latest/), etc.

   Consider using access patterns, method/argument naming, and return values that are consistent with the underlying package and familiar to existing users of that package.

2. **Intuitive, easy to use read methods.**

   Much of the power of st.connection is providing intuitive, easy-to-use read methods that enable app developers to get started quickly. Most connections should expose at least one read method that is:

   - Named with a simple verb, like `read()`, `query()`, or `get()`
   - Wrapped by `st.cache_data` by default, with at least `ttl=` argument supported
   - If the result is in a tabular format, it returns a pandas DataFrame
   - Provides commonly used keyword arguments (such as paging or formatting) with sensible defaults - ideally, the common case requires only 1-2 arguments.

3. **Config, secrets, and precedence in `_connect` method.**

   Every Connection should support commonly used connection parameters provided via Streamlit secrets and keyword arguments. The names should match the ones used when initializing or configuring the underlying package.

   Additionally, where relevant, Connections should support data source specific configuration through existing standard environment variables or config / credential files. In many cases, the underlying package provides constructors or factory functions that already handle this easily.

   When you can specify the same connection parameters in multiple places, we recommend using the following precedence order when possible (highest to lowest):

   - Keyword arguments specified in the code
   - Streamlit secrets
   - data source specific configuration (if relevant)

4. **Handling thread safety and stale connections.**

   Connections should provide thread-safe operations when practical (which should be most of the time) and clearly document any considerations around this. Most underlying drivers or SDKs should provide thread-safe objects or methods - use these when possible.

   If the underlying driver or SDK has a risk of stateful connection objects becoming stale or invalid, consider building a low impact health check or reset/retry pattern into the access methods. The SQLConnection built into Streamlit has a good example of this pattern using [tenacity](https://tenacity.readthedocs.io/) and the built-in [Connection.reset()](/develop/api-reference/connections/st.connections.sqlconnection#sqlconnectionreset) method. An alternate approach is to encourage developers to set an appropriate TTL on the `st.connection()` call to ensure it periodically reinitializes the connection object.

```

File: concepts/connections/security-reminders.md
```

---

title: Security reminders
slug: /develop/concepts/connections/security-reminders

---

# Security reminders

## Protect your secrets

Never save usernames, passwords, or security keys directly in your code or commit them to your repository.

### Use environment variables

Avoid putting sensitve information in your code by using environment variables. Be sure to check out [`st.secrets`](/develop/concepts/connections/secrets-management). Research any platform you use to follow their security best practices. If you use Streamlit Community Cloud, [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) allows you save environment variables and store secrets outside of your code.

### Keep `.gitignore` updated

If you use any sensitive or private information during development, make sure that information is saved in separate files from your code. Ensure `.gitignore` is properly configured to prevent saving private information to your repository.

## Pickle warning

Streamlit's [`st.cache_data`](/develop/concepts/architecture/caching#stcache_data) and [`st.session_state`](/develop/concepts/architecture/session-state#serializable-session-state) implicitly use the `pickle` module, which is known to be insecure. It is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

- When using `st.cache_data`, anything your function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values. This warning also applies to [`st.cache`](/develop/api-reference/caching-and-state/st.cache) (deprecated).
- When the `runner.enforceSerializableSessionState` [configuration option](<(/develop/concepts/configuration#runner)>) is set to `true`, ensure all data saved and retrieved from Session State is trusted.

```

File: concepts/architecture/app-chrome.md
```

---

title: The app chrome
slug: /develop/concepts/architecture/app-chrome

---

# The app chrome

Your Streamlit app has a few widgets in the top right to help you as you develop. These widgets also help your viewers as they use your app. We call this things ΓÇ£the app chromeΓÇ¥. The chrome includes a status area, toolbar, and app menu.

Your app menu is configurable. By default, you can access developer options from the app menu when viewing an app locally or on Streamlit Community Cloud while logged into an account with administrative access. While viewing an app, click the icon in the upper-right corner to access the menu.

![App menu](/images/app-menu/app-menu-developer.png)

## Menu options

The menu is split into two sections. The upper section contains options available to all viewers and the lower section contains options for developers. Read more about [customizing this menu](#customize-the-menu) at the end of this page.

### Rerun

You can manually trigger a rerun of your app by clicking "**Rerun**" from the app menu. This rerun will not reset your session. Your widget states and values stored in [`st.session_state`](/develop/concepts/architecture/session-state) will be preserved. As a shortcut, without opening the app menu, you can rerun your app by pressing "**R**" on your keyboard (if you aren't currently focused on an input element).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-rerun-XL.png" alt="Rerun" clean />
</div>

### Settings

With the "**Settings**" option, you can control the appearance of your app while it is running. If viewing the app locally, you can set how your app responds to changes in your source code. See more about development flow in [Basic concepts](/get-started/fundamentals/main-concepts#development-flow). You can also force your app to appear in wide mode, even if not set within the script using [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-settings-XL.png" alt="Settings" clean />
</div>

#### Theme settings

After clicking "**Settings**" from the app menu, you can choose between "**Light**", "**Dark**", or "**Use system setting**" for the app's base theme. Click on "**Edit active theme**" to modify the theme, color-by-color.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-settings-modal.png" alt="Settings" clean />
</div>

<br />

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-settings-theme.png" alt="Theme" clean />
</div>

### Print

Click "**Print**" to open a print dialog. This option uses your browser's built-in print-to-pdf function.

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-print-XL.png" alt="Print" clean />
</div>

### Record a screencast

You can easily make screen recordings right from your app! Screen recording is supported in the latest versions of Chrome, Edge, and Firefox. Ensure your browser is up-to-date for compatibility. Depending on your current settings, you may need to grant permission to your browser to record your screen or to use your microphone if recording a voiceover.

1. While viewing your app, open the app menu from the upper-right corner.
2. Click "**Record a screencast**."

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-record-XL.png" alt="Record" clean />
</div>

3. If you want to record audio through your microphone, check "**Also record audio**."
4. Click "**Start recording**." (You may be prompted by your OS to permit your browser to record your screen or use your microphone.)

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-2.png" alt="Record" />
</div>

5. Select which tab, window, or monitor you want to record from the listed options. The interface will vary depending on your browser.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-3.png" alt="Record" />
</div>

6. Click "**Share**."

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-4.png" alt="Record" />
</div>

7. While recording, you will see a red circle on your app's tab and on the app menu icon. If you want to cancel the recording, click "**Stop sharing**" at the bottom of your app.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-5.png" alt="Record" />
</div>

8. When you are done recording, press "**Esc**" on your keyboard or click "**Stop recording**" from your app's menu.

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record-6.png" alt="Record" />
</div>

9. Follow your browser's instructions to save your recording. Your saved recording will be available where your browser saves downloads.

The whole process looks like this:

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-record.gif" alt="Record" />
</div>

### About

You can conveniently check what version of Streamlit is running from the "**About**" option. Developers also have the option to customize the message shown here using [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-about-XL.png" alt="Rerun" clean />
</div>

## Developer options

By default, developer options only show when viewing an app locally or when viewing a Community Cloud app while logged in with administrative permission. You can [customize the menu](#customize-the-menu) if you want to make these options available for all users.

### Clear cache

Reset your app's cache by clicking "**Clear cache**" from the app's menu or by pressing "**C**" on your keyboard while not focused on an input element. This will remove all cached entries for [`@st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) and [`@st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource).

<div style={{ maxWidth: '30%', margin: 'auto' }}>
    <Image src="/images/app-menu/app-menu-clear-XL.png" alt="Rerun" clean />
</div>

### Deploy this app

If you are running an app locally from within a git repo, you can deploy your app to Streamlit Community Cloud in a few easy clicks! Make sure your work has been pushed to your online GitHub repository before beginning. For the greatest convenience, make sure you have already created your [Community Cloud account](/deploy/streamlit-community-cloud/get-started/create-your-account) and are signed in.

1. Click "**Deploy**" next to the app menu icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>more_vert</i>).

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-deploy.png" alt="Settings" />
</div>

2. Click "**Deploy now**".

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/app-menu-deploy-1.png" alt="Settings" />
</div>

3. You will be taken to Community Cloud's "Deploy an app" page. Your app's repository, branch, and file name will be prefilled to match your current app! Learn more about [deploying an app](/deploy/streamlit-community-cloud/deploy-your-app) on Streamlit Community Cloud.

The whole process looks like this:

<div style={{ maxWidth: '90%', margin: '0 2em 0 2em' }}>
    <Image src="/images/app-menu/deploy-from-local.gif" alt="Settings" />
</div>

## Customize the menu

Using `client.toolbarMode` in your app's [configuration](/develop/concepts/configuration), you can make the app menu appear in the following ways:

- `"developer"` &mdash; Show the developer options to all viewers.
- `"viewer"` &mdash; Hide the developer options from all viewers.
- `"minimal"` &mdash; Show only those options set externally. These options can be declared through [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) or populated through Streamlit Community Cloud.
- `"auto"` &mdash; This is the default and will show the developer options when accessed through localhost or through Streamlit Community Cloud when logged into an administrative account for the app. Otherwise, the developer options will not show.

```

File: concepts/architecture/old_caching.md
```

---

title: Optimize performance with st.cache
slug: /develop/concepts/architecture/st.cache

---

<Deprecation>

`st.cache` was deprecated in version 1.18.0. Use [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) or [`st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource) instead. Learn more in [Caching](/develop/concepts/architecture/caching).

</Deprecation>

# Optimize performance with st.cache

Streamlit provides a caching mechanism that allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations. This is done with the [`@st.cache`](/develop/api-reference/caching-and-state/st.cache) decorator.

When you mark a function with the [`@st.cache`](/develop/api-reference/caching-and-state/st.cache) decorator, it tells Streamlit that whenever the function is called it needs to check a few things:

1. The input parameters that you called the function with
2. The value of any external variable used in the function
3. The body of the function
4. The body of any function used inside the cached function

If this is the first time Streamlit has seen these four components with these exact values and in this exact combination and order, it runs the function and stores the result in a local cache. Then, next time the cached function is called, if none of these components changed, Streamlit will just skip executing the function altogether and, instead, return the output previously stored in the cache.

The way Streamlit keeps track of changes in these components is through hashing. Think of the cache as an in-memory key-value store, where the key is a hash of all of the above and the value is the actual output object passed by reference.

Finally, [`@st.cache`](/develop/api-reference/caching-and-state/st.cache) supports arguments to configure the cache's behavior. You can find more information on those in our [API reference](/develop/api-reference).

Let's take a look at a few examples that illustrate how caching works in a Streamlit app.

## Example 1: Basic usage

For starters, let's take a look at a sample app that has a function that performs an expensive, long-running computation. Without caching, this function is rerun each time the app is refreshed, leading to a poor user experience. Copy this code into a new app and try it out yourself:

```python
import streamlit as st
import time

def expensive_computation(a, b):
    time.sleep(2)  # ≡ƒæê This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)
```

Try pressing **R** to rerun the app, and notice how long it takes for the result to show up. This is because `expensive_computation(a, b)` is being re-executed every time the app runs. This isn't a great experience.

Let's add the [`@st.cache`](/develop/api-reference/caching-and-state/st.cache) decorator:

```python
import streamlit as st
import time

@st.cache  # ≡ƒæê Added this
def expensive_computation(a, b):
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)
```

Now run the app again and you'll notice that it is much faster every time you press R to rerun. To understand what is happening, let's add an st.write inside the function:

```python
import streamlit as st
import time

@st.cache(suppress_st_warning=True)  # ≡ƒæê Changed this
def expensive_computation(a, b):
    # ≡ƒæç Added this
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)
```

Now when you rerun the app the text "Cache miss" appears on the first run, but not on any subsequent runs. That's because the cached function is only being executed once, and every time after that you're actually hitting the cache.

<Note>

You may have noticed that we've added the `suppress_st_warning` keyword to the `@st.cache` decorators. That's because the cached function above uses a Streamlit command itself (`st.write` in this case), and when Streamlit sees that, it shows a warning that your command will only execute when you get a cache miss. More often than not, when you see that warning it's because there's a bug in your code. However, in our case we're using the `st.write` command to demonstrate when the cache is being missed, so the behavior Streamlit is warning us about is exactly what we want. As a result, we are passing in `suppress_st_warning=True` to turn that warning off.

</Note>

## Example 2: When the function arguments change

Without stopping the previous app server, let's change one of the arguments to our cached function:

```python
import streamlit as st
import time

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 210  # ≡ƒæê Changed this
res = expensive_computation(a, b)

st.write("Result:", res)
```

Now the first time you rerun the app it's a cache miss. This is evidenced by the "Cache miss" text showing up and the app taking 2s to finish running. After that, if you press **R** to rerun, it's always a cache hit. That is, no such text shows up and the app is fast again.

This is because Streamlit notices whenever the arguments **a** and **b** change and determines whether the function should be re-executed and re-cached.

## Example 3: When the function body changes

Without stopping and restarting your Streamlit server, let's remove the widget from our app and modify the function's code by adding a `+ 1` to the return value.

```python
import streamlit as st
import time

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b + 1  # ≡ƒæê Added a +1 at the end here

a = 2
b = 210
res = expensive_computation(a, b)

st.write("Result:", res)
```

The first run is a "Cache miss", but when you press **R** each subsequent run is a cache hit. This is because on first run, Streamlit detected that the function body changed, reran the function, and put the result in the cache.

<Tip>

If you change the function back the result will already be in the Streamlit cache from a previous run. Try it out!

</Tip>

## Example 4: When an inner function changes

Let's make our cached function depend on another function internally:

```python
import streamlit as st
import time

def inner_func(a, b):
    st.write("inner_func(", a, ",", b, ") ran")
    return a * b

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return inner_func(a, b) + 1

a = 2
b = 210
res = expensive_computation(a, b)

st.write("Result:", res)
```

What you see is the usual:

1. The first run results in a cache miss.
1. Every subsequent rerun results in a cache hit.

But now let's try modifying the `inner_func()`:

```python
import streamlit as st
import time

def inner_func(a, b):
    st.write("inner_func(", a, ",", b, ") ran")
    return a ** b  # ≡ƒæê Changed the * to ** here

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return inner_func(a, b) + 1

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)
```

Even though `inner_func()` is not annotated with [`@st.cache`](/develop/api-reference/caching-and-state/st.cache), when we edit its body we cause a "Cache miss" in the outer `expensive_computation()`.

That's because Streamlit always traverses your code and its dependencies to verify that the cached values are still valid. This means that while developing your app you can edit your code freely without worrying about the cache. Any change you make to your app, Streamlit should do the right thing!

Streamlit is also smart enough to only traverse dependencies that belong to your app, and skip over any dependency that comes from an installed Python library.

## Example 5: Use caching to speed up your app across users

Going back to our original function, let's add a widget to control the value of `b`:

```python
import streamlit as st
import time

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = st.slider("Pick a number", 0, 10)  # ≡ƒæê Changed this
res = expensive_computation(a, b)

st.write("Result:", res)
```

What you'll see:

- If you move the slider to a number Streamlit hasn't seen before, you'll have a cache miss again. And every subsequent rerun with the same number will be a cache hit, of course.
- If you move the slider back to a number Streamlit has seen before, the cache is hit and the app is fast as expected.

In computer science terms, what is happening here is that [`@st.cache`](/develop/api-reference/caching-and-state/st.cache) is [memoizing](https://en.wikipedia.org/wiki/Memoization) `expensive_computation(a, b)`.

But now let's go one step further! Try the following:

1. Move the slider to a number you haven't tried before, such as 9.
2. Pretend you're another user by opening another browser tab pointing to your Streamlit app (usually at http://localhost:8501)
3. In the new tab, move the slider to 9.

Notice how this is actually a cache hit! That is, you don't actually see the "Cache miss" text on the second tab even though that second user never moved the slider to 9 at any point prior to this.

This happens because the Streamlit cache is global to all users. So everyone contributes to everyone else's performance.

## Example 6: Mutating cached values

As mentioned in the [overview](#optimize-performance-with-stcache) section, the Streamlit cache stores items by reference. This allows the Streamlit cache to support structures that aren't memory-managed by Python, such as TensorFlow objects. However, it can also lead to unexpected behavior ΓÇö which is why Streamlit has a few checks to guide developers in the right direction. Let's look into those checks now.

Let's write an app that has a cached function which returns a mutable object, and then let's follow up by mutating that object:

```python
import streamlit as st
import time

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return {"output": a * b}  # ≡ƒæê Mutable object

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)

res["output"] = "result was manually mutated"  # ≡ƒæê Mutated cached value

st.write("Mutated result:", res)
```

When you run this app for the first time, you should see three messages on the screen:

```
Cache miss: expensive_computation(...) ran
Result: {output: 42}
Mutated result: {output: "result was manually mutated"}
```

No surprises here. But now notice what happens when you rerun you app (i.e. press **R**):

```
Result: {output: "result was manually mutated"}
Mutated result: {output: "result was manually mutated"}
Cached object mutated. (...)
```

So what's up?

What's going on here is that Streamlit caches the output `res` by reference. When you mutated `res["output"]` outside the cached function you ended up inadvertently modifying the cache. This means every subsequent call to `expensive_computation(2, 21)` will return the wrong value!

Since this behavior is usually not what you'd expect, Streamlit tries to be helpful and show you a warning, along with some ideas about how to fix your code.

In this specific case, the fix is just to not mutate `res["output"]` outside the cached function. There was no good reason for us to do that anyway! Another solution would be to clone the result value with `res = deepcopy(expensive_computation(2, 21))`. Check out the section entitled [Fixing caching issues](/knowledge-base/using-streamlit/caching-issues) for more information on these approaches and more.

## Advanced caching

In [caching](/develop/concepts/architecture/caching), you learned about the Streamlit cache, which is accessed with the [`@st.cache`](/develop/api-reference/caching-and-state/st.cache) decorator. In this article you'll see how Streamlit's caching functionality is implemented, so that you can use it to improve the performance of your Streamlit apps.

The cache is a key-value store, where the key is a hash of:

1. The input parameters that you called the function with
1. The value of any external variable used in the function
1. The body of the function
1. The body of any function used inside the cached function

And the value is a tuple of:

- The cached output
- A hash of the cached output (you'll see why soon)

For both the key and the output hash, Streamlit uses a specialized hash function that knows how to traverse code, hash special objects, and can have its [behavior customized by the user](#the-hash_funcs-parameter).

For example, when the function `expensive_computation(a, b)`, decorated with [`@st.cache`](/develop/api-reference/caching-and-state/st.cache), is executed with `a=2` and `b=21`, Streamlit does the following:

1. Computes the cache key
1. If the key is found in the cache, then:
   - Extracts the previously-cached (output, output_hash) tuple.
   - Performs an **Output Mutation Check**, where a fresh hash of the output is computed and compared to the stored `output_hash`.
     - If the two hashes are different, shows a **Cached Object Mutated** warning. (Note: Setting `allow_output_mutation=True` disables this step).
1. If the input key is not found in the cache, then:
   - Executes the cached function (i.e. `output = expensive_computation(2, 21)`).
   - Calculates the `output_hash` from the function's `output`.
   - Stores `key ΓåÆ (output, output_hash)` in the cache.
1. Returns the output.

If an error is encountered an exception is raised. If the error occurs while hashing either the key or the output an `UnhashableTypeError` error is thrown. If you run into any issues, see [fixing caching issues](/knowledge-base/using-streamlit/caching-issues).

### The hash_funcs parameter

As described above, Streamlit's caching functionality relies on hashing to calculate the key for cached objects, and to detect unexpected mutations in the cached result.

For added expressive power, Streamlit lets you override this hashing process using the `hash_funcs` argument. Suppose you define a type called `FileReference` which points to a file in the filesystem:

```python
class FileReference:
    def __init__(self, filename):
        self.filename = filename


@st.cache
def func(file_reference):
    ...
```

By default, Streamlit hashes custom classes like `FileReference` by recursively navigating their structure. In this case, its hash is the hash of the filename property. As long as the file name doesn't change, the hash will remain constant.

However, what if you wanted to have the hasher check for changes to the file's modification time, not just its name? This is possible with [`@st.cache`](/develop/api-reference/caching-and-state/st.cache)'s `hash_funcs` parameter:

```python
class FileReference:
    def __init__(self, filename):
        self.filename = filename

def hash_file_reference(file_reference):
    filename = file_reference.filename
    return (filename, os.path.getmtime(filename))

@st.cache(hash_funcs={FileReference: hash_file_reference})
def func(file_reference):
    ...
```

Additionally, you can hash `FileReference` objects by the file's contents:

```python
class FileReference:
    def __init__(self, filename):
        self.filename = filename

def hash_file_reference(file_reference):
    with open(file_reference.filename) as f:
      return f.read()

@st.cache(hash_funcs={FileReference: hash_file_reference})
def func(file_reference):
    ...
```

<Note>

Because Streamlit's hash function works recursively, you don't have to hash the contents inside `hash_file_reference` Instead, you can return a primitive type, in this case the contents of the file, and Streamlit's internal hasher will compute the actual hash from it.

</Note>

### Typical hash functions

While it's possible to write custom hash functions, let's take a look at some of the tools that Python provides out of the box. Here's a list of some hash functions and when it makes sense to use them.

Python's [`id`](https://docs.python.org/3/library/functions.html#id) function | [Example](#example-1-pass-a-database-connection-around)

- Speed: Fast
- Use case: If you're hashing a singleton object, like an open database connection or a TensorFlow session. These are objects that will only be instantiated once, no matter how many times your script reruns.

`lambda _: None` | [Example](#example-2-turn-off-hashing-for-a-specific-type)

- Speed: Fast
- Use case: If you want to turn off hashing of this type. This is useful if you know the object is not going to change.

Python's [`hash()`](https://docs.python.org/3/library/functions.html#hash) function | [Example](#example-3-use-pythons-hash-function)

- Speed: Can be slow based the size of the object being cached
- Use case: If Python already knows how to hash this type correctly.

Custom hash function | [Example](#the-hash_funcs-parameter)

- Speed: N/a
- Use case: If you'd like to override how Streamlit hashes a particular type.

### Example 1: Pass a database connection around

Suppose we want to open a database connection that can be reused across multiple runs of a Streamlit app. For this you can make use of the fact that cached objects are stored by reference to automatically initialize and reuse the connection:

```python
@st.cache(allow_output_mutation=True)
def get_database_connection():
    return db.get_connection()
```

With just 3 lines of code, the database connection is created once and stored in the cache. Then, every subsequent time `get_database_connection` is called, the already-created connection object is reused automatically. In other words, it becomes a singleton.

<Tip>

Use the `allow_output_mutation=True` flag to suppress the immutability check. This prevents Streamlit from trying to hash the output connection, and also turns off Streamlit's mutation warning in the process.

</Tip>

What if you want to write a function that receives a database connection as input? For that, you'll use `hash_funcs`:

```python
@st.cache(hash_funcs={DBConnection: id})
def get_users(connection):
    # Note: We assume that connection is of type DBConnection.
    return connection.execute_sql('SELECT * from Users')
```

Here, we use Python's built-in `id` function, because the connection object is coming from the Streamlit cache via the `get_database_connection` function. This means that the same connection instance is passed around every time, and therefore it always has the same id. However, if you happened to have a second connection object around that pointed to an entirely different database, it would still be safe to pass it to `get_users` because its id is guaranteed to be different than the first id.

These design patterns apply any time you have an object that points to an external resource, such as a database connection or Tensorflow session.

### Example 2: Turn off hashing for a specific type

You can turn off hashing entirely for a particular type by giving it a custom hash function that returns a constant. One reason that you might do this is to avoid hashing large, slow-to-hash objects that you know are not going to change. For example:

```python
@st.cache(hash_funcs={pd.DataFrame: lambda _: None})
def func(huge_constant_dataframe):
    ...
```

When Streamlit encounters an object of this type, it always converts the object into `None`, no matter which instance of `FooType` its looking at. This means all instances are hash to the same value, which effectively cancels out the hashing mechanism.

### Example 3: Use Python's hash() function

Sometimes, you might want to use PythonΓÇÖs default hashing instead of Streamlit's. For example, maybe you've encountered a type that Streamlit is unable to hash, but it's hashable with Python's built-in `hash()` function:

```python
@st.cache(hash_funcs={FooType: hash})
def func(...):
    ...
```

```

File: concepts/architecture/fragments.md
```

---

title: Working with fragments and partial reruns
slug: /develop/concepts/architecture/fragments

---

# Working with fragments and partial reruns

Reruns are a central part of every Streamlit app. When users interact with widgets, your script reruns from top to bottom, and your app's frontend is updated. Streamlit provides several features to help you develop your app within this execution model. Streamlit version 1.33.0 introduced fragments to allow rerunning a portion of your code instead of your full script. As your app grows larger and more complex, these partial reruns help your app be efficient and performant. Fragments give you finer, easy-to-understand control over your app's execution flow.

Before you read about fragments, we recommend having a basic understanding of [caching](/develop/concepts/architecture/caching), [Session State](/concepts/architecture/session-state), and [forms](/develop/concepts/architecture/forms).

## Use cases for fragments

Fragments are versatile and applicable to a wide variety of circumstances. Here are just a few, common scenarios where fragments are useful:

- Your app has multiple visualizations and each one takes time to load, but you have a filter input that only updates one of them.
- You have a dynamic form that doesn't need to update the rest of your app (until the form is complete).
- You want to automatically update a single component or group of components to stream data.

## Defining and calling a fragment

Streamlit provides a decorator ([`st.experimental_fragment`](/develop/api-reference/execution-flow/st.fragment)) to turn any function into a fragment function. When you call a fragment function that contains a widget function, a user triggers a _partial rerun_ instead of a full rerun when they interact with that fragment's widget. During a partial rerun, your fragment function is re-executed. Anything within the main body of your fragment is updated on the frontend, while the rest of your app remains the same. We'll describe fragments written across multiple containers later on.

Here is a basic example of defining and calling a fragment function. Just like with caching, remember to call your function after defining it.

```python
import streamlit as st

@st.experimental_fragment
def fragment_function():
    if st.button("Hi!"):
        st.write("Hi back!")

fragment_function()
```

If you want the main body of your fragment to appear in the sidebar or another container, call your fragment function inside a context manager.

```python
with st.sidebar:
    fragment_function()
```

### Partial rerun execution flow

Consider the following code with the explanation and diagram below.

```python
import streamlit as st

st.title("My Awesome App")

@st.experimental_fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.experimental_fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()
```

When a user interacts with an input widget inside a fragment, only the fragment reruns instead of the full script. When a user interacts with an input widget outside a fragment, the full script reruns as usual.

If you run the code above, the full script will run top to bottom on your app's initial load. If you flip the toggle button in your running app, the first fragment (`toggle_and_text()`) will rerun, redrawing the toggle and text area while leaving everything else unchanged. If you click the checkbox, the second fragment (`filter_and_file()`) will rerun and consequently redraw the checkbox and file uploader. Everything else remains unchanged. Finally, if you click the update button, the full script will rerun, and Streamlit will redraw everything.

![Diagram of fragment execution flow](/images/concepts/fragment_diagram.png)

## Fragment return values and interacting with the rest of your app

Streamlit ignores fragment return values during fragment reruns, so defining return values for your fragment functions is not recommended. Instead, if your fragment needs to share data with the rest of your app, use Session State. Fragments are just functions in your script, so they can access Session State, imported modules, and other Streamlit elements like containers. If your fragment writes to any container created outside of itself, note the following difference in behavior:

- Elements drawn in the main body of your fragment are cleared and redrawn in place during a fragment rerun. Repeated fragment reruns will not cause additional elements to appear.
- Elements drawn to containers outside the main body of fragment will not be cleared with each fragment rerun. Instead, Streamlit will draw them additively and these elements will accumulate until the next full-script rerun.

To prevent elements from accumulating in outside containers, use [`st.empty`](/develop/api-reference/layout/st.empty) containers. For a related tutorial, see [Create a fragment across multiple containers](/develop/tutorials/execution-flow/create-a-multiple-container-fragment).

If you need to trigger a full-script rerun from inside a fragment, call [`st.rerun`](/develop/api-reference/execution-flow/st.rerun). For a related tutorial, see [Trigger a full-script rerun from inside a fragment](/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment).

## Automate fragment reruns

`st.experimental_fragment` includes a convenient `run_every` parameter that causes the fragment to rerun automatically at the specified time interval. These reruns are in addition to any reruns (fragment or full-script) triggered by your user. The automatic fragment reruns will continue even if your user is not interacting with your app. This is a great way to show a live data stream or status on a running background job, efficiently updating your rendered data and _only_ your rendered data.

```python
@st.experimental_fragment(run_every="10s")
def auto_function():
		# This will update every 10 seconds!
		df = get_latest_updates()
		st.line_chart(df)

auto_function()
```

For a related tutorial, see [Start and stop a streaming fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns).

## Compare fragments to other Streamlit features

### Fragments vs forms

Here is a comparison between fragments and forms:

- **Forms** allow users to interact with widgets without rerunning your app. Streamlit does not send user actions within a form to your app's Python backend until the form is submitted. Widgets within a form can not dynamically update other widgets (in or out of the form) in real-time.
- **Fragments** run independently from the rest of your code. As your users interact with fragment widgets, their actions are immediately processed by your app's Python backend and your fragment code is rerun. Widgets within a fragment can dynamically update other widgets within the same fragment in real-time.

A form batches user input without interaction between any widgets. A fragment immediately processes user input but limits the scope of the rerun.

### Fragments vs callbacks

Here is a comparison between fragments and callbacks:

- **Callbacks** allow you to execute a function at the beginning of a script rerun. A callback is a _single prefix_ to your script rerun.
- **Fragments** allow you to rerun a portion of your script. A fragment is a _repeatable postfix_ to your script, running each time a user interacts with a fragment widget, or automatically in sequence when `run_every` is set.

When callbacks render elements to your page, they are rendered before the rest of your page elements. When fragments render elements to your page, they are updated with each fragment rerun (unless they are written to containers outside of the fragment, in which case they accumulate there).

### Fragments vs custom components

Here is a comparison between fragments and custom components:

- **Components** are custom frontend code that can interact with the Python code, native elements, and widgets in your Streamlit app. Custom components extend whatΓÇÖs possible with Streamlit. They follow the normal Streamlit execution flow.
- **Fragments** are parts of your app that can rerun independently of the full app. Fragments can be composed of multiple Streamlit elements, widgets, or any Python code.

A fragment can include one or more custom components. A custom component could not easily include a fragment!

### Fragments vs caching

Here is a comparison between fragments and caching:

- **Caching:** allows you to skip over a function and return a previously computed value. When you use caching, you execute everything except the cached function (if you've already run it before).
- **Fragments:** allow you to freeze most of your app and just execute the fragment. When you use fragments, you execute only the fragment (when triggering a fragment rerun).

Caching saves you from unnecessarily running a piece of your app while the rest runs. Fragments save you from running your full app when you only want to run one piece.

## Limitations and unsupported behavior

- Fragments can't detect a change in input values. It is best to use Session State for dynamic input and output for fragment functions.
- Calling fragments within fragments is unsupported.
- Using caching and fragments on the same function is unsupported.

```

File: concepts/architecture/caching.md
```

---

title: Caching overview
slug: /develop/concepts/architecture/caching

---

<Note>

Documentation for the deprecated `@st.cache` decorator can be found in [Optimize performance with st.cache](/develop/concepts/architecture/st.cache).

</Note>

# Caching overview

Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes development super easy. But it comes with two major challenges:

1. Long-running functions run again and again, which slows down your app.
2. Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.

But don't worry! Streamlit lets you tackle both issues with its built-in caching mechanism. Caching stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns.

<Collapse title="Table of contents" expanded={true}>

1. [Minimal example](#minimal-example)
2. [Basic usage](#basic-usage)
3. [Advanced usage](#advanced-usage)
4. [Migrating from st.cache](#migrating-from-stcache)

</Collapse>

## Minimal example

To cache a function in Streamlit, you must decorate it with one of two decorators (`st.cache_data` or `st.cache_resource`):

```python
@st.cache_data
def long_running_function(param1, param2):
    return ΓÇª
```

In this example, decorating `long_running_function` with `@st.cache_data` tells Streamlit that whenever the function is called, it checks two things:

1. The values of the input parameters (in this case, `param1` and `param2`).
2. The code inside the function.

If this is the first time Streamlit sees these parameter values and function code, it runs the function and stores the return value in a cache. The next time the function is called with the same parameters and code (e.g., when a user interacts with the app), Streamlit will skip executing the function altogether and return the cached value instead. During development, the cache updates automatically as the function code changes, ensuring that the latest changes are reflected in the cache.

As mentioned, there are two caching decorators:

- `st.cache_data`┬áis the recommended way to cache computations that return data: loading a DataFrame from CSV, transforming a NumPy array, querying an API, or any other function that returns a serializable data object (str, int, float, DataFrame, array, list, ΓÇª). It creates a new copy of the data at each function call, making it safe against [mutations and race conditions](#mutation-and-concurrency-issues). The behavior of `st.cache_data` is what you want in most cases ΓÇô so if you're unsure, start with┬á`st.cache_data`┬áand see if it works!
- `st.cache_resource`┬áis the recommended way to cache global resources like ML models or database connections ΓÇô unserializable objects that you don't want to load multiple times. Using it, you can share these resources across all reruns and sessions of an app without copying or duplication. Note that any mutations to the cached return value directly mutate the object in the cache (more details below).

<Image src="/images/caching-high-level-diagram.png" caption="Streamlit's two caching decorators and their use cases." alt="Streamlit's two caching decorators and their use cases. Use st.cache_data for anything you'd store in a database. Use st.cache_resource for anything you can't store in a database, like a connection to a database or a machine learning model." />

## Basic usage

### st.cache_data

`st.cache_data` is your go-to command for all functions that return data ΓÇô whether DataFrames, NumPy arrays, str, int, float, or other serializable types. It's the right command for almost all use cases!

#### Usage

<br />

Let's look at an example of using┬á`st.cache_data`. Suppose your app loads the [Uber ride-sharing dataset](https://github.com/plotly/datasets/blob/master/uber-rides-data1.csv) ΓÇô a CSV file of 50 MB ΓÇô from the internet into a DataFrame:

```python
def load_data(url):
    df = pd.read_csv(url)  # ≡ƒæê Download the data
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
```

Running the `load_data` function takes 2 to 30 seconds, depending on your internet connection. (Tip: if you are on a slow connection, use [this 5 MB dataset instead](https://github.com/plotly/datasets/blob/master/26k-consumer-complaints.csv)). Without caching, the download is rerun each time the app is loaded or with user interaction. Try it yourself by clicking the button we added! Not a great experienceΓÇª ≡ƒÿò

Now let's add the┬á`@st.cache_data`┬ádecorator on `load_data`:

```python
@st.cache_data  # ≡ƒæê Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
```

Run the app again. You'll notice that the slow download only happens on the first run. Every subsequent rerun should be almost instant! ≡ƒÆ¿

#### Behavior

<br />

How does this work? Let's go through the behavior of `st.cache_data` step by step:

- On the first run, Streamlit recognizes that it has never called the `load_data` function with the specified parameter value (the URL of the CSV file) So it runs the function and downloads the data.
- Now our caching mechanism becomes active: the returned DataFrame is serialized (converted to bytes) via┬á[pickle](https://docs.python.org/3/library/pickle.html)┬áand stored in the cache (together with the value of the `url` parameter).
- On the next run, Streamlit checks the cache for an entry of `load_data` with the specific `url`. There is one! So it retrieves the cached object, deserializes it to a DataFrame, and returns it instead of re-running the function and downloading the data again.

This process of serializing and deserializing the cached object creates a copy of our original DataFrame. While this copying behavior may seem unnecessary, it's what we want when caching data objects since it effectively prevents mutation and concurrency issues. Read the section ΓÇ£[Mutation and concurrency issues](#mutation-and-concurrency-issues)" below to understand this in more detail.

<Warning>

`st.cache_data` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

#### Examples

<br/>

**DataFrame transformations**

In the example above, we already showed how to cache loading a DataFrame. It can also be useful to cache DataFrame transformations such as `df.filter`, `df.apply`, or `df.sort_values`. Especially with large DataFrames, these operations can be slow.

```python
@st.cache_data
def transform(df):
    df = df.filter(items=['one', 'three'])
    df = df.apply(np.sum, axis=0)
	return df
```

**Array computations**

Similarly, it can make sense to cache computations on NumPy arrays:

```python
@st.cache_data
def add(arr1, arr2):
	return arr1 + arr2
```

**Database queries**

You usually make SQL queries to load data into your app when working with databases. Repeatedly running these queries can be slow, cost money, and degrade the performance of your database. We strongly recommend caching any database queries in your app. See also [our guides on connecting Streamlit to different databases](/develop/tutorials/databases) for in-depth examples.

```python
connection = database.connect()

@st.cache_data
def query():
    return pd.read_sql_query("SELECT * from table", connection)
```

<Tip>

You should set a `ttl` (time to live) to get new results from your database. If you set `st.cache_data(ttl=3600)`, Streamlit invalidates any cached values after 1 hour (3600 seconds) and runs the cached function again. See details in [Controlling cache size and duration](#controlling-cache-size-and-duration).

</Tip>

**API calls**

Similarly, it makes sense to cache API calls. Doing so also avoids rate limits.

```python
@st.cache_data
def api_call():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return response.json()
```

**Running ML models (inference)**

Running complex machine learning models can use significant time and memory. To avoid rerunning the same computations over and over, use caching.

```python
@st.cache_data
def run_model(inputs):
    return model(inputs)
```

### st.cache_resource

`st.cache_resource` is the right command to cache ΓÇ£resources" that should be available globally across all users, sessions, and reruns. It has more limited use cases than `st.cache_data`, especially for caching database connections and ML models.

#### Usage

As an example for `st.cache_resource`, let's look at a typical machine learning app. As a first step, we need to load an ML model. We do this with [Hugging Face's transformers library](https://huggingface.co/docs/transformers/index):

```python
from transformers import pipeline
model = pipeline("sentiment-analysis")  # ≡ƒæê Load the model
```

If we put this code into a Streamlit app directly, the app will load the model at each rerun or user interaction. Repeatedly loading the model poses two problems:

- Loading the model takes time and slows down the app.
- Each session loads the model from scratch, which takes up a huge amount of memory.

Instead, it would make much more sense to load the model once and use that same object across all users and sessions. That's exactly the use case for `st.cache_resource`! Let's add it to our app and process some text the user entered:

```python
from transformers import pipeline

@st.cache_resource  # ≡ƒæê Add the caching decorator
def load_model():
    return pipeline("sentiment-analysis")

model = load_model()

query = st.text_input("Your query", value="I love Streamlit! ≡ƒÄê")
if query:
    result = model(query)[0]  # ≡ƒæê Classify the query text
    st.write(result)
```

If you run this app, you'll see that the app calls `load_model` only once ΓÇô right when the app starts. Subsequent runs will reuse that same model stored in the cache, saving time and memory!

#### Behavior

<br />

Using `st.cache_resource` is very similar to using `st.cache_data`. But there are a few important differences in behavior:

- `st.cache_resource` does **not** create a copy of the cached return value but instead stores the object itself in the cache. All mutations on the function's return value directly affect the object in the cache, so you must ensure that mutations from multiple sessions do not cause problems. In short, the return value must be thread-safe.

    <Warning>

  Using `st.cache_resource` on objects that are not thread-safe might lead to crashes or corrupted data. Learn more below under [Mutation and concurrency issues](#mutation-and-concurrency-issues).
  </Warning>

- Not creating a copy means there's just one global instance of the cached return object, which saves memory, e.g. when using a large ML model. In computer science terms, we create a [singleton](https://en.wikipedia.org/wiki/Singleton_pattern).
- Return values of functions do not need to be serializable. This behavior is great for types not serializable by nature, e.g., database connections, file handles, or threads. Caching these objects with `st.cache_data` is not possible.

#### Examples

<br />

**Database connections**

`st.cache_resource` is useful for connecting to databases. Usually, you're creating a connection object that you want to reuse globally for every query. Creating a new connection object at each run would be inefficient and might lead to connection errors. That's exactly what `st.cache_resource` can do, e.g., for a Postgres database:

```python
@st.cache_resource
def init_connection():
    host = "hh-pgsql-public.ebi.ac.uk"
    database = "pfmegrnargs"
    user = "reader"
    password = "NWDMCE5xdipIjRrp"
    return psycopg2.connect(host=host, database=database, user=user, password=password)

conn = init_connection()
```

Of course, you can do the same for any other database. Have a look at [our guides on how to connect Streamlit to databases](/develop/tutorials/databases) for in-depth examples.

**Loading ML models**

Your app should always cache ML models, so they are not loaded into memory again for every new session. See the [example](#usage-1) above for how this works with ≡ƒñù┬áHugging Face models. You can do the same thing for PyTorch, TensorFlow, etc. Here's an example for PyTorch:

```python
@st.cache_resource
def load_model():
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
    model.eval()
    return model

model = load_model()
```

### Deciding which caching decorator to use

<br />

The sections above showed many common examples for each caching decorator. But there are edge cases for which it's less trivial to decide which caching decorator to use. Eventually, it all comes down to the difference between ΓÇ£data" and ΓÇ£resource":

- Data are serializable objects (objects that can be converted to bytes via┬á[pickle](https://docs.python.org/3/library/pickle.html)) that you could easily save to disk. Imagine all the types you would usually store in a database or on a file system ΓÇô basic types like str, int, and float, but also arrays, DataFrames, images, or combinations of these types (lists, tuples, dicts, and so on).
- Resources are unserializable objects that you usually would not save to disk or a database. They are often more complex, non-permanent objects like database connections, ML models, file handles, threads, etc.

From the types listed above, it should be obvious that most objects in Python are ΓÇ£data." That's also why `st.cache_data` is the correct command for almost all use cases. `st.cache_resource` is a more exotic command that you should only use in specific situations.

Or if you're lazy and don't want to think too much, look up your use case or return type in the table below ≡ƒÿë:

| Use case                             |                                                                                                       Typical return types |                                                                                                                                              Caching decorator |
| :----------------------------------- | -------------------------------------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Reading a CSV file with pd.read_csv  |                                                                                                           pandas.DataFrame |                                                                                                                                                  st.cache_data |
| Reading a text file                  |                                                                                                           str, list of str |                                                                                                                                                  st.cache_data |
| Transforming pandas dataframes       |                                                                                            pandas.DataFrame, pandas.Series |                                                                                                                                                  st.cache_data |
| Computing with numpy arrays          |                                                                                                              numpy.ndarray |                                                                                                                                                  st.cache_data |
| Simple computations with basic types |                                                                                                       str, int, float, ΓÇª |                                                                                                                                                  st.cache_data |
| Querying a database                  |                                                                                                           pandas.DataFrame |                                                                                                                                                  st.cache_data |
| Querying an API                      |                                                                                                pandas.DataFrame, str, dict |                                                                                                                                                  st.cache_data |
| Running an ML model (inference)      |                                                                                     pandas.DataFrame, str, int, dict, list |                                                                                                                                                  st.cache_data |
| Creating or processing images        |                                                                                             PIL.Image.Image, numpy.ndarray |                                                                                                                                                  st.cache_data |
| Creating charts                      |                                                        matplotlib.figure.Figure, plotly.graph_objects.Figure, altair.Chart | st.cache_data (but some libraries require st.cache_resource, since the chart object is not serializable ΓÇô make sure not to mutate the chart after creation!) |
| Loading ML models                    |                                                             transformers.Pipeline, torch.nn.Module, tensorflow.keras.Model |                                                                                                                                              st.cache_resource |
| Initializing database connections    | pyodbc.Connection, sqlalchemy.engine.base.Engine, psycopg2.connection, mysql.connector.MySQLConnection, sqlite3.Connection |                                                                                                                                              st.cache_resource |
| Opening persistent file handles      |                                                                                                         \_io.TextIOWrapper |                                                                                                                                              st.cache_resource |
| Opening persistent threads           |                                                                                                           threading.thread |                                                                                                                                              st.cache_resource |

## Advanced usage

### Controlling cache size and duration

If your app runs for a long time and constantly caches functions, you might run into two problems:

1. The app runs out of memory because the cache is too large.
2. Objects in the cache become stale, e.g. because you cached old data from a database.

You can combat these problems with the `ttl` and `max_entries` parameters, which are available for both caching decorators.

**The `ttl` (time-to-live) parameter**

`ttl` sets a time to live on a cached function. If that time is up and you call the function again, the app will discard any old, cached values, and the function will be rerun. The newly computed value will then be stored in the cache. This behavior is useful for preventing stale data (problem 2) and the cache from growing too large (problem 1). Especially when pulling data from a database or API, you should always set a `ttl` so you are not using old data. Here's an example:

```python
@st.cache_data(ttl=3600)  # ≡ƒæê Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = api.get(...)
    return data
```

<Tip>

You can also set `ttl` values using `timedelta`, e.g., `ttl=datetime.timedelta(hours=1)`.

</Tip>

**The `max_entries` parameter**

`max_entries` sets the maximum number of entries in the cache. An upper bound on the number of cache entries is useful for limiting memory (problem 1), especially when caching large objects. The oldest entry will be removed when a new entry is added to a full cache. Here's an example:

```python
@st.cache_data(max_entries=1000)  # ≡ƒæê Maximum 1000 entries in the cache
def get_large_array(seed):
    np.random.seed(seed)
    arr = np.random.rand(100000)
    return arr
```

### Customizing the spinner

By default, Streamlit shows a small loading spinner in the app when a cached function is running. You can modify it easily with the `show_spinner` parameter, which is available for both caching decorators:

```python
@st.cache_data(show_spinner=False)  # ≡ƒæê Disable the spinner
def get_api_data():
    data = api.get(...)
    return data

@st.cache_data(show_spinner="Fetching data from API...")  # ≡ƒæê Use custom text for spinner
def get_api_data():
    data = api.get(...)
    return data
```

### Excluding input parameters

In a cached function, all input parameters must be hashable. Let's quickly explain why and what it means. When the function is called, Streamlit looks at its parameter values to determine if it was cached before. Therefore, it needs a reliable way to compare the parameter values across function calls. Trivial for a string or int ΓÇô but complex for arbitrary objects! Streamlit uses [hashing](https://en.wikipedia.org/wiki/Hash_function) to solve that. It converts the parameter to a stable key and stores that key. At the next function call, it hashes the parameter again and compares it with the stored hash key.

Unfortunately, not all parameters are hashable! E.g., you might pass an unhashable database connection or ML model to your cached function. In this case, you can exclude input parameters from caching. Simply prepend the parameter name with an underscore (e.g., `_param1`), and it will not be used for caching. Even if it changes, Streamlit will return a cached result if all the other parameters match up.

Here's an example:

```python
@st.cache_data
def fetch_data(_db_connection, num_rows):  # ≡ƒæê Don't hash _db_connection
    data = _db_connection.fetch(num_rows)
    return data

connection = init_connection()
fetch_data(connection, 10)
```

But what if you want to cache a function that takes an unhashable parameter? For example, you might want to cache a function that takes an ML model as input and returns the layer names of that model. Since the model is the only input parameter, you cannot exclude it from caching. In this case you can use the `hash_funcs` parameter to specify a custom hashing function for the model.

### The `hash_funcs` parameter

As described above, Streamlit's caching decorators hash the input parameters and cached function's signature to determine whether the function has been run before and has a return value stored ("cache hit") or needs to be run ("cache miss"). Input parameters that are not hashable by Streamlit's hashing implementation can be ignored by prepending an underscore to their name. But there two rare cases where this is undesirable. i.e. where you want to hash the parameter that Streamlit is unable to hash:

1. When Streamlit's hashing mechanism fails to hash a parameter, resulting in a `UnhashableParamError` being raised.
2. When you want to override Streamlit's default hashing mechanism for a parameter.

Let's discuss each of these cases in turn with examples.

#### Example 1: Hashing a custom class

Streamlit does not know how to hash custom classes. If you pass a custom class to a cached function, Streamlit will raise a `UnhashableParamError`. For example, let's define a custom class `MyCustomClass` that accepts an initial integer score. Let's also define a cached function `multiply_score` that multiplies the score by a multiplier:

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

@st.cache_data
def multiply_score(obj: MyCustomClass, multiplier: int) -> int:
    return obj.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(multiply_score(score, multiplier))
```

If you run this app, you'll see that Streamlit raises a `UnhashableParamError` since it does not know how to hash `MyCustomClass`:

```python
UnhashableParamError: Cannot hash argument 'obj' (of type __main__.MyCustomClass) in 'multiply_score'.
```

To fix this, we can use the `hash_funcs` parameter to tell Streamlit how to hash `MyCustomClass`. We do this by passing a dictionary to `hash_funcs` that maps the name of the parameter to a hash function. The choice of hash function is up to the developer. In this case, let's define a custom hash function `hash_func` that takes the custom class as input and returns the score. We want the score to be the unique identifier of the object, so we can use it to deterministically hash the object:

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

def hash_func(obj: MyCustomClass) -> int:
    return obj.my_score  # or any other value that uniquely identifies the object

@st.cache_data(hash_funcs={MyCustomClass: hash_func})
def multiply_score(obj: MyCustomClass, multiplier: int) -> int:
    return obj.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(multiply_score(score, multiplier))
```

Now if you run the app, you'll see that Streamlit no longer raises a `UnhashableParamError` and the app runs as expected.

Let's now consider the case where `multiply_score` is an attribute of `MyCustomClass` and we want to hash the entire object:

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
```

If you run this app, you'll see that Streamlit raises a `UnhashableParamError` since it cannot hash the argument `'self' (of type __main__.MyCustomClass) in 'multiply_score'`. A simple fix here could be to use Python's `hash()` function to hash the object:

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data(hash_funcs={"__main__.MyCustomClass": lambda x: hash(x.my_score)})
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
```

Above, the hash function is defined as `lambda x: hash(x.my_score)`. This creates a hash based on the `my_score` attribute of the `MyCustomClass` instance. As long as `my_score` remains the same, the hash remains the same. Thus, the result of `multiply_score` can be retrieved from the cache without recomputation.

As an astute Pythonista, you may have been tempted to use Python's `id()` function to hash the object like so:

```python
import streamlit as st

class MyCustomClass:
    def __init__(self, initial_score: int):
        self.my_score = initial_score

    @st.cache_data(hash_funcs={"__main__.MyCustomClass": id})
    def multiply_score(self, multiplier: int) -> int:
        return self.my_score * multiplier

initial_score = st.number_input("Enter initial score", value=15)

score = MyCustomClass(initial_score)
multiplier = 2

st.write(score.multiply_score(multiplier))
```

If you run the app, you'll notice that Streamlit recomputes `multiply_score` each time even if `my_score` hasn't changed! Puzzled? In Python, `id()` returns the identity of an object, which is unique and constant for the object during its lifetime. This means that even if the `my_score` value is the same between two instances of `MyCustomClass`, `id()` will return different values for these two instances, leading to different hash values. As a result, Streamlit considers these two different instances as needing separate cached values, thus it recomputes the `multiply_score` each time even if `my_score` hasn't changed.

This is why we discourage using it as hash func, and instead encourage functions that return deterministic, true hash values. That said, if you know what you're doing, you can use `id()` as a hash function. Just be aware of the consequences. For example, `id` is often the _correct_ hash func when you're passing the result of an `@st.cache_resource` function as the input param to another cached function. There's a whole class of object types that arenΓÇÖt otherwise hashable.

#### Example 2: Hashing a Pydantic model

Let's consider another example where we want to hash a Pydantic model:

```python
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_data
def identity(person: Person):
    return person

person = identity(Person(name="Lee"))
st.write(f"The person is {person.name}")
```

Above, we define a custom class `Person` using Pydantic's `BaseModel` with a single attribute name. We also define an `identity` function which accepts an instance of `Person` as an arg and returns it without modification. This function is intended to cache the result, therefore, if called multiple times with the same `Person` instance, it won't recompute but return the cached instance.

If you run the app, however, you'll run into a `UnhashableParamError: Cannot hash argument 'person' (of type __main__.Person) in 'identity'.` error. This is because Streamlit does not know how to hash the `Person` class. To fix this, we can use the `hash_funcs` kwarg to tell Streamlit how to hash `Person`.

In the version below, we define a custom hash function `hash_func` that takes the `Person` instance as input and returns the name attribute. We want the name to be the unique identifier of the object, so we can use it to deterministically hash the object:

```python
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_data(hash_funcs={Person: lambda p: p.name})
def identity(person: Person):
    return person

person = identity(Person(name="Lee"))
st.write(f"The person is {person.name}")
```

#### Example 3: Hashing a ML model

There may be cases where you want to pass your favorite machine learning model to a cached function. For example, let's say you want to pass a TensorFlow model to a cached function, based on what model the user selects in the app. You might try something like this:

```python
import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_base_model(option):
    if option == 1:
        return tf.keras.applications.ResNet50(include_top=False, weights="imagenet")
    else:
        return tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet")

@st.cache_resource
def load_layers(base_model):
    return [layer.name for layer in base_model.layers]

option = st.radio("Model 1 or 2", [1, 2])

base_model = load_base_model(option)

layers = load_layers(base_model)

st.write(layers)
```

In the above app, the user can select one of two models. Based on the selection, the app loads the corresponding model and passes it to `load_layers`. This function then returns the names of the layers in the model. If you run the app, you'll see that Streamlit raises a `UnhashableParamError` since it cannot hash the argument `'base_model' (of type keras.engine.functional.Functional) in 'load_layers'`.

If you disable hashing for `base_model` by prepending an underscore to its name, you'll observe that regardless of which base model is chosen, the layers displayed are same. This subtle bug is due to the fact that the `load_layers` function is not re-run when the base model changes. This is because Streamlit does not hash the `base_model` argument, so it does not know that the function needs to be re-run when the base model changes.

To fix this, we can use the `hash_funcs` kwarg to tell Streamlit how to hash the `base_model` argument. In the version below, we define a custom hash function `hash_func`: `Functional: lambda x: x.name`. Our choice of hash func is informed by our knowledge that the `name` attribute of a `Functional` object or model uniquely identifies it. As long as the `name` attribute remains the same, the hash remains the same. Thus, the result of `load_layers` can be retrieved from the cache without recomputation.

```python
import streamlit as st
import tensorflow as tf
from keras.engine.functional import Functional

@st.cache_resource
def load_base_model(option):
    if option == 1:
        return tf.keras.applications.ResNet50(include_top=False, weights="imagenet")
    else:
        return tf.keras.applications.MobileNetV2(include_top=False, weights="imagenet")

@st.cache_resource(hash_funcs={Functional: lambda x: x.name})
def load_layers(base_model):
    return [layer.name for layer in base_model.layers]

option = st.radio("Model 1 or 2", [1, 2])

base_model = load_base_model(option)

layers = load_layers(base_model)

st.write(layers)
```

In the above case, we could also have used `hash_funcs={Functional: id}` as the hash function. This is because `id` is often the _correct_ hash func when you're passing the result of an `@st.cache_resource` function as the input param to another cached function.

#### Example 4: Overriding Streamlit's default hashing mechanism

Let's consider another example where we want to override Streamlit's default hashing mechanism for a pytz-localized datetime object:

```python
from datetime import datetime
import pytz
import streamlit as st

tz = pytz.timezone("Europe/Berlin")

@st.cache_data
def load_data(dt):
    return dt

now = datetime.now()
st.text(load_data(dt=now))

now_tz = tz.localize(datetime.now())
st.text(load_data(dt=now_tz))
```

It may be surprising to see that although `now` and `now_tz` are of the same `<class 'datetime.datetime'>` type, Streamlit does not how to hash `now_tz` and raises a `UnhashableParamError`. In this case, we can override Streamlit's default hashing mechanism for `datetime` objects by passing a custom hash function to the `hash_funcs` kwarg:

```python
from datetime import datetime

import pytz
import streamlit as st

tz = pytz.timezone("Europe/Berlin")

@st.cache_data(hash_funcs={datetime: lambda x: x.strftime("%a %d %b %Y, %I:%M%p")})
def load_data(dt):
    return dt

now = datetime.now()
st.text(load_data(dt=now))

now_tz = tz.localize(datetime.now())
st.text(load_data(dt=now_tz))
```

Let's now consider a case where we want to override Streamlit's default hashing mechanism for NumPy arrays. While Streamlit natively hashes Pandas and NumPy objects, there may be cases where you want to override Streamlit's default hashing mechanism for these objects.

For example, let's say we create a cache-decorated `show_data` function that accepts a NumPy array and returns it without modification. In the bellow app, `data = df["str"].unique()` (which is a NumPy array) is passed to the `show_data` function.

```python
import time
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
    return df

@st.cache_data
def show_data(data):
    time.sleep(2)  # This makes the function take 2s to run
    return data

df = get_data()
data = df["str"].unique()

st.dataframe(show_data(data))
st.button("Re-run")
```

Since `data` is always the same, we expect the `show_data` function to return the cached value. However, if you run the app, and click the `Re-run` button, you'll notice that the `show_data` function is re-run each time. We can assume this behavior is a consequence of Streamlit's default hashing mechanism for NumPy arrays.

To work around this, let's define a custom hash function `hash_func` that takes a NumPy array as input and returns a string representation of the array:

```python
import time
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    df = pd.DataFrame({"num": [112, 112, 2, 3], "str": ["be", "a", "be", "c"]})
    return df

@st.cache_data(hash_funcs={np.ndarray: str})
def show_data(data):
    time.sleep(2)  # This makes the function take 2s to run
    return data

df = get_data()
data = df["str"].unique()

st.dataframe(show_data(data))
st.button("Re-run")
```

Now if you run the app, and click the `Re-run` button, you'll notice that the `show_data` function is no longer re-run each time. It's important to note here that our choice of hash function was very naive and not necessarily the best choice. For example, if the NumPy array is large, converting it to a string representation may be expensive. In such cases, it is up to you as the developer to define what a good hash function is for your use case.

#### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

```python
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # ≡ƒæê Show a success message
    return data
```

As we know, Streamlit only runs this function if it hasn't been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

```python
@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)
```

#### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

```python
@st.cache_data(experimental_allow_widgets=True)  # ≡ƒæê Set the parameter
def get_data():
    num_rows = st.slider("Number of rows to get")  # ≡ƒæê Add a slider
    data = api.get(..., num_rows)
    return data
```

Streamlit treats the slider like an additional input parameter to the cached function. If you change the slider position, Streamlit will see if it has already cached the function for this slider value. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we'll add 100 MB to the cache for _every permutation_ of these five slider values ΓÇô even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

<Warning>

Support for widgets in cached functions is experimental. We may change or remove it anytime without warning. Please use it with care!
</Warning>

<Note>

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!
</Note>

### Dealing with large data

As we explained, you should cache data objects with `st.cache_data`. But this can be slow for extremely large data, e.g., DataFrames or arrays with >100 million rows. That's because of the [copying behavior](#copying-behavior) of `st.cache_data`: on the first run, it serializes the return value to bytes and deserializes it on subsequent runs. Both operations take time.

If you're dealing with extremely large data, it can make sense to use `st.cache_resource` instead. It does not create a copy of the return value via serialization/deserialization and is almost instant. But watch out: any mutation to the function's return value (such as dropping a column from a DataFrame or setting a value in an array) directly manipulates the object in the cache. You must ensure this doesn't corrupt your data or lead to crashes. See the section on [Mutation and concurrency issues](#mutation-and-concurrency-issues) below.

When benchmarking `st.cache_data` on pandas DataFrames with four columns, we found that it becomes slow when going beyond 100 million rows. The table shows runtimes for both caching decorators at different numbers of rows (all with four columns):

|                   |                 | 10M rows | 50M rows | 100M rows | 200M rows |
| ----------------- | --------------- | :------: | :------: | :-------: | :-------: |
| st.cache_data     | First run\*     |  0.4 s   |   3 s    |   14 s    |   28 s    |
|                   | Subsequent runs |  0.2 s   |   1 s    |    2 s    |    7 s    |
| st.cache_resource | First run\*     |  0.01 s  |  0.1 s   |   0.2 s   |    1 s    |
|                   | Subsequent runs |   0 s    |   0 s    |    0 s    |    0 s    |

|                                                                                                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _\*For the first run, the table only shows the overhead time of using the caching decorator. It does not include the runtime of the cached function itself._ |

### Mutation and concurrency issues

In the sections above, we talked a lot about issues when mutating return objects of cached functions. This topic is complicated! But it's central to understanding the behavior differences between `st.cache_data` and `st.cache_resource`. So let's dive in a bit deeper.

First, we should clearly define what we mean by mutations and concurrency:

- By **mutations**, we mean any changes made to a cached function's return value _after_ that function has been called. I.e. something like this:

  ```python
  @st.cache_data
  def create_list():
      l = [1, 2, 3]

  l = create_list()  # ≡ƒæê Call the function
  l[0] = 2  # ≡ƒæê Mutate its return value
  ```

- By **concurrency**, we mean that multiple sessions can cause these mutations at the same time. Streamlit is a web framework that needs to handle many users and sessions connecting to an app. If two people view an app at the same time, they will both cause the Python script to rerun, which may manipulate cached return objects at the same time ΓÇô concurrently.

Mutating cached return objects can be dangerous. It can lead to exceptions in your app and even corrupt your data (which can be worse than a crashed app!). Below, we'll first explain the copying behavior of `st.cache_data` and show how it can avoid mutation issues. Then, we'll show how concurrent mutations can lead to data corruption and how to prevent it.

#### Copying behavior

`st.cache_data` creates a copy of the cached return value each time the function is called. This avoids most mutations and concurrency issues. To understand it in detail, let's go back to the [Uber ridesharing example](#usage) from the section on `st.cache_data` above. We are making two modifications to it:

1. We are using `st.cache_resource` instead of `st.cache_data`. `st.cache_resource` does **not** create a copy of the cached object, so we can see what happens without the copying behavior.
2. After loading the data, we manipulate the returned DataFrame (in place!) by dropping the column `"Lat"`.

Here's the code:

```python
@st.cache_resource   # ≡ƒæê Turn off copying behavior
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv")
st.dataframe(df)

df.drop(columns=['Lat'], inplace=True)  # ≡ƒæê Mutate the dataframe inplace

st.button("Rerun")
```

Let's run it and see what happens! The first run should work fine. But in the second run, you see an exception: `KeyError: "['Lat'] not found in axis"`. Why is that happening? Let's go step by step:

- On the first run, Streamlit runs `load_data` and stores the resulting DataFrame in the cache. Since we're using `st.cache_resource`, it does **not** create a copy but stores the original DataFrame.
- Then we drop the column `"Lat"` from the DataFrame. Note that this is dropping the column from the _original_ DataFrame stored in the cache. We are manipulating it!
- On the second run, Streamlit returns that exact same manipulated DataFrame from the cache. It does not have the column `"Lat"` anymore! So our call to `df.drop` results in an exception. Pandas cannot drop a column that doesn't exist.

The copying behavior of `st.cache_data` prevents this kind of mutation error. Mutations can only affect a specific copy and not the underlying object in the cache. The next rerun will get its own, unmutated copy of the DataFrame. You can try it yourself, just replace `st.cache_resource` with `st.cache_data` above, and you'll see that everything works.

Because of this copying behavior,┬á`st.cache_data`┬áis the recommended way to cache data transforms and computations ΓÇô anything that returns a serializable object.

#### Concurrency issues

Now let's look at what can happen when multiple users concurrently mutate an object in the cache. Let's say you have a function that returns a list. Again, we are using `st.cache_resource` to cache it so that we are not creating a copy:

```python
@st.cache_resource
def create_list():
    l = [1, 2, 3]
    return l

l = create_list()
first_list_value = l[0]
l[0] = first_list_value + 1

st.write("l[0] is:", l[0])
```

Let's say user A runs the app. They will see the following output:

```python
l[0] is: 2
```

Let's say another user, B, visits the app right after. In contrast to user A, they will see the following output:

```python
l[0] is: 3
```

Now, user A reruns the app immediately after user B. They will see the following output:

```python
l[0] is: 4
```

What is happening here? Why are all outputs different?

- When user A visits the app,┬á`create_list()`┬áis called, and the list┬á`[1, 2, 3]`┬áis stored in the cache. This list is then returned to user A. The first value of the list, `1`, is assigned to `first_list_value` , and `l[0]`┬áis changed to `2`.
- When user B visits the app,┬á`create_list()`┬áreturns the mutated list from the cache:┬á`[2, 2, 3]`. The first value of the list, `2`, is assigned to `first_list_value` and `l[0]`┬áis changed to `3`.
- When user A reruns the app,┬á`create_list()`┬áreturns the mutated list again:┬á`[3, 2, 3]`. The first value of the list, `3`, is assigned to `first_list_value,` and `l[0]`┬áis changed to 4.

If you think about it, this makes sense. Users A and B use the same list object (the one stored in the cache). And since the list object is mutated, user A's change to the list object is also reflected in user B's app.

This is why you must be careful about mutating objects cached with `st.cache_resource`, especially when multiple users access the app concurrently. If we had used┬á`st.cache_data`┬áinstead of┬á`st.cache_resource`, the app would have copied the list object for each user, and the above example would have worked as expected ΓÇô users A and B would have both seen:

```python
l[0] is: 2
```

<Note>

This toy example might seem benign. But data corruption can be extremely dangerous! Imagine we had worked with the financial records of a large bank here. You surely don't want to wake up with less money on your account just because someone used the wrong caching decorator ≡ƒÿë

</Note>

## Migrating from st.cache

We introduced the caching commands described above in Streamlit 1.18.0. Before that, we had one catch-all command `st.cache`. Using it was often confusing, resulted in weird exceptions, and was slow. That's why we replaced `st.cache` with the new commands in 1.18.0 (read more in this [blog post](https://blog.streamlit.io/introducing-two-new-caching-commands-to-replace-st-cache/)). The new commands provide a more intuitive and efficient way to cache your data and resources and are intended to replace `st.cache` in all new development.

If your app is still using `st.cache`, don't despair! Here are a few notes on migrating:

- Streamlit will show a deprecation warning if your app uses `st.cache`.
- We will not remove `st.cache` soon, so you don't need to worry about your 2-year-old app breaking. But we encourage you to try the new commands going forward ΓÇô they will be way less annoying!
- Switching code to the new commands should be easy in most cases. To decide whether to use `st.cache_data` or `st.cache_resource`, read [Deciding which caching decorator to use](#deciding-which-caching-decorator-to-use). Streamlit will also recognize common use cases and show hints right in the deprecation warnings.
- Most parameters from `st.cache` are also present in the new commands, with a few exceptions:
  - `allow_output_mutation` does not exist anymore. You can safely delete it. Just make sure you use the right caching command for your use case.
  - `suppress_st_warning` does not exist anymore. You can safely delete it. Cached functions can now contain Streamlit commands and will replay them. If you want to use widgets inside cached functions, set `experimental_allow_widgets=True`. See [Input widgets](#input-widgets) for an example.

If you have any questions or issues during the migration process, please contact us on the [forum](https://discuss.streamlit.io/), and we will be happy to assist you. ≡ƒÄê

```

File: concepts/architecture/old_cache_primitives.md
```

---

title: Experimental cache primitives
slug: /develop/concepts/architecture/experimental-cache-primitives

---

<Deprecation>

The experimental cache primitives described on this page were deprecated in version 1.18.0. Use [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) or [`st.cache_resource`](/develop/api-reference/caching-and-state/st.cache_resource) instead. Learn more in [Caching](/develop/concepts/architecture/caching).

</Deprecation>

# Experimental cache primitives

## Overview

Streamlit's unique execution model is a part of what makes it a joy to use: your code executes from top to bottom like a simple script for every interaction. There's no need to think about models, views, controllers, or anything of the sort.

Whenever your code re-executes, a decorator called [`@st.cache`](/develop/api-reference/caching-and-state/st.cache)ΓÇöwhich is a powerful primitive for memoization and state storage capabilitiesΓÇöprovides a caching mechanism that allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

However, we've found that [`@st.cache`](/develop/concepts/architecture/caching) is hard to use and not fast. You're either faced with cryptic errors like `InternalHashError` or `UnhashableTypeError`. Or you need to understand concepts like [`hash_funcs`](/develop/concepts/architecture/caching#the-hash_funcs-parameter) and [`allow_output_mutation`](/develop/concepts/architecture/caching#example-1-pass-a-database-connection-around).

Our solutions include two new primitives: [**`st.experimental_memo`**](/develop/api-reference/caching-and-state/st.experimental_memo) and [**`st.experimental_singleton`**](/develop/api-reference/caching-and-state/st.experimental_singleton). They're conceptually simpler and much, much faster. In some of our internal tests on caching large dataframes, `@st.experimental_memo` has outperformed `@st.cache` by an order of magnitude. That's over 10X faster! ≡ƒÜÇ

Let's take a look at the use-cases these _two_ experimental APIs serve, and how they're a significant improvement over `@st.cache`.

## Problem

`@st.cache` was serving the following use-cases:

1. Storing computation results given different kinds of inputs. In Computer Science literature, this is called [**memoization**](https://en.wikipedia.org/wiki/Memoization).
2. Initializing an object exactly once, and reusing that same instance on each rerun for the Streamlit server's lifetime. This is called the [**singleton pattern**](https://en.wikipedia.org/wiki/Singleton_pattern).
3. Storing global state to be shared and modified across multiple Streamlit sessions (and, since Streamlit is threaded, you need to pay special attention to thread-safety).

As a result of `@st.cache` trying to cover too many use-cases under a single unified API, it's both slow and complex.

## Solution

While `@st.cache` tries to solve two very different problems simultaneously (caching data and sharing global singleton objects), these new primitives simplify things by dividing the problem across two different APIs. As a result, they are faster and simpler.

### `@st.experimental_memo`

Use [`@st.experimental_memo`](/develop/api-reference/caching-and-state/st.experimental_memo) to store expensive computation which can be "cached" or "memoized" in the traditional sense. It has almost the exact same API as the existing `@st.cache`, so you can often blindly replace one for the other:

```python
import streamlit as st

@st.experimental_memo
def factorial(n):
	if n < 1:
		return 1
	return n * factorial(n - 1)

f10 = factorial(10)
f9 = factorial(9)  # Returns instantly!
```

#### Properties

- Unlike `@st.cache`, this returns cached items by value, not by reference. This means that you no longer have to worry about accidentally mutating the items stored in the cache. Behind the scenes, this is done by using Python's `pickle()` function to serialize/deserialize cached values.
- Although this uses a custom hashing solution for generating cache keys (like `@st.cache`), it does **_not_** use `hash_funcs` as an escape hatch for unhashable parameters. Instead, we allow you to ignore unhashable parameters (e.g. database connections) by prefixing them with an underscore.

For example:

```python
import streamlit as st
import pandas as pd
from sqlalchemy.orm import sessionmaker

@st.experimental_memo
def get_page(_sessionmaker, page_size, page):
	"""Retrieve rows from the RNA database, and cache them.

	Parameters
	----------
	_sessionmaker : a SQLAlchemy session factory. Because this arg name is
	                prefixed with "_", it won't be hashed.
	page_size : the number of rows in a page of result
	page : the page number to retrieve

	Returns
	-------
	pandas.DataFrame
	A DataFrame containing the retrieved rows. Mutating it won't affect
	the cache.
	"""
	with _sessionmaker() as session:
		query = (
			session
				.query(RNA.id, RNA.seq_short, RNA.seq_long, RNA.len, RNA.upi)
				.order_by(RNA.id)
				.offset(page_size * page)
				.limit(page_size)
		)

		return pd.read_sql(query.statement, query.session.bind)
```

### `@st.experimental_singleton`

[`@st.experimental_singleton`](/develop/api-reference/caching-and-state/st.experimental_singleton) is a key-value store that's shared across all sessions of a Streamlit app. It's great for storing heavyweight singleton objects across sessions (like TensorFlow/Torch/Keras sessions and/or database connections).

Example usage:

```python
import streamlit as st
from sqlalchemy.orm import sessionmaker

@st.experimental_singleton
def get_db_sessionmaker():
	# This is for illustration purposes only
	DB_URL = "your-db-url"
	engine = create_engine(DB_URL)
	return sessionmaker(engine)

dbsm = get_db_sessionmaker()
```

#### How this compares to `@st.cache`:

- Like `@st.cache`, **this returns items by reference.**
- You can return any object type, including objects that are not serializable.
- Unlike `@st.cache`, this decorator does not have additional logic to check whether you are unexpectedly mutating the cached object. That logic was slow and produced confusing error messages. So, instead, we're hoping that by calling this decorator "singleton," we're nudging you to the correct behavior.
- This does not follow the computation graph.
- You don't have to worry about `hash_funcs`! Just prefix your arguments with an underscore to ignore them.

<Warning>

Singleton objects can be used concurrently by every user connected to your app, and _you are responsible for ensuring that `@st.singleton` objects are thread-safe_. (Most objects you'd want to stick inside an `@st.singleton` annotation are probably already safeΓÇöbut you should verify this.)

</Warning>

### Which to use: memo or singleton?

Decide between `@st.experimental_memo` and `@st.experimental_singleton` based on your function's _return type_. Functions that return _data_ should use `memo`. Functions that return _non-data objects_ should use `singleton`.

For example:

- Dataframe computation (pandas, numpy, etc): this is *dataΓÇö*use `memo`
- Storing downloaded data: `memo`
- Calculating pi to n digits: `memo`
- Tensorflow session: this is a *non-data objectΓÇö*use `singleton`
- Database connection: `singleton`

### Clear memo and singleton caches procedurally

You can clear caches of functions decorated with `@st.experimental_memo` and `@st.experimental_singleton` _in code_. For example, you can do the following:

```python
@st.experimental_memo
def square(x):
    return x**2

if st.button("Clear Square"):
    # Clear square's memoized values:
    square.clear()

if st.button("Clear All"):
    # Clear values from *all* memoized functions:
    st.experimental_memo.clear()
```

Pressing the "Clear Square" button will clear `square()`'s memoized values. Pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.experimental_memo`.

In summary:

- Any function annotated with `@st.experimental_memo` or `@st.experimental_singleton` gets its own `clear()` function automatically.
- Additionally, you can use [`st.experimental_memo.clear()`](/develop/api-reference/caching-and-state/st.experimental_memo.clear) and [`st.experimental_singleton.clear()`](/develop/api-reference/caching-and-state/st.experimental_singleton.clear) to clear _all_ memo and singleton caches, respectively.

<Note>

The commands are **experimental**, so they're governed by our [experimental API process](/develop/quick-reference/prerelease#experimental).

</Note>

These specialized **memoization** and **singleton** commands represent a big step in Streamlit's evolution, with the potential to _entirely replace_ `@st.cache` at some point in 2022.

Yes, today you may use `@st.cache` for storing data you pulled in from a database connection (for a Tensorflow session, for caching the results of a long computation like changing the datetime values on a pandas dataframe, etc.). But these are very different things, so we made two new functions that will make it much faster! ≡ƒÆ¿

Please help us out by testing these commands in real apps and leaving comments in [the Streamlit forums](https://discuss.streamlit.io/).

```

File: concepts/architecture/run-your-app.md
```

---

title: Run your Streamlit app
slug: /develop/concepts/architecture/run-your-app

---

# Run your Streamlit app

Working with Streamlit is simple. First you sprinkle a few Streamlit commands into a normal Python script, and then you run it. We list few ways to run your script, depending on your use case.

## Use streamlit run

Once you've created your script, say `your_script.py`, the easiest way to run it is with `streamlit run`:

```bash
streamlit run your_script.py
```

As soon as you run the script as shown above, a local Streamlit server will spin up and your app will open in a new tab in your default web browser.

### Pass arguments to your script

When passing your script some custom arguments, they must be passed after two dashes. Otherwise the arguments get interpreted as arguments to Streamlit itself:

```bash
streamlit run your_script.py [-- script args]
```

### Pass a URL to streamlit run

You can also pass a URL to `streamlit run`! This is great when your script is hosted remotely, such as a GitHub Gist. For example:

```bash
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

## Run Streamlit as a Python module

Another way of running Streamlit is to run it as a Python module. This is useful when configuring an IDE like PyCharm to work with Streamlit:

```bash
# Running
python -m streamlit run your_script.py
```

```bash
# is equivalent to:
streamlit run your_script.py
```

```

File: concepts/architecture/session-state.md
```

---

title: Add statefulness to apps
slug: /develop/concepts/architecture/session-state

---

# Add statefulness to apps

## What is State?

We define access to a Streamlit app in a browser tab as a **session**. For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app. Each reruns takes place in a blank slate: no variables are shared between runs.

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks. Session state also persists across pages inside a [multipage app](/develop/concepts/multipage-apps).

In this guide, we will illustrate the usage of **Session State** and **Callbacks** as we build a stateful Counter app.

For details on the Session State and Callbacks API, please refer to our [Session State API Reference Guide](/develop/api-reference/caching-and-state/st.session_state).

Also, check out this Session State basics tutorial video by Streamlit Developer Advocate Dr. Marisa Smith to get started:

<YouTube videoId="92jUAXBmZyU" />

## Build a Counter

Let's call our script `counter.py`. It initializes a `count` variable and has a button to increment the value stored in the `count` variable:

```python
import streamlit as st

st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)
```

No matter how many times we press the **_Increment_** button in the above app, the `count` remains at 1. Let's understand why:

- Each time we press the **_Increment_** button, Streamlit reruns `counter.py` from top to bottom, and with every run, `count` gets initialized to `0` .
- Pressing **_Increment_** subsequently adds 1 to 0, thus `count=1` no matter how many times we press **_Increment_**.

As we'll see later, we can avoid this issue by storing `count` as a Session State variable. By doing so, we're indicating to Streamlit that it should maintain the value stored inside a Session State variable across app reruns.

Let's learn more about the API to use Session State.

### Initialization

The Session State API follows a field-based API, which is very similar to Python dictionaries:

```python
import streamlit as st

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
```

### Reads and updates

Read the value of an item in Session State by passing the item to `st.write` :

```python
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Reads
st.write(st.session_state.key)

# Outputs: value
```

Update an item in Session State by assigning it a value:

```python
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Updates
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API
```

Streamlit throws an exception if an uninitialized variable is accessed:

```python
import streamlit as st

st.write(st.session_state['value'])

# Throws an exception!
```

![state-uninitialized-exception](/images/state_uninitialized_exception.png)

Let's now take a look at a few examples that illustrate how to add Session State to our Counter app.

### Example 1: Add Session State

Now that we've got a hang of the Session State API, let's update our Counter app to use Session State:

```python
import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)
```

As you can see in the above example, pressing the **_Increment_** button updates the `count` each time.

### Example 2: Session State and Callbacks

Now that we've built a basic Counter app using Session State, let's move on to something a little more complex. The next example uses Callbacks with Session State.

**Callbacks**: A callback is a Python function which gets called when an input widget changes. Callbacks can be used with widgets using the parameters `on_change` (or `on_click`), `args`, and `kwargs`. The full Callbacks API can be found in our [Session State API Reference Guide](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state).

```python
import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)
```

Now, pressing the **_Increment_** button updates the count each time by calling the `increment_counter()` function.

### Example 3: Use args and kwargs in Callbacks

Callbacks also support passing arguments using the `args` parameter in a widget:

```python
import streamlit as st

st.title('Counter Example using Callbacks with args')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('Increment', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count = ', st.session_state.count)
```

Additionally, we can also use the `kwargs` parameter in a widget to pass named arguments to the callback function as shown below:

```python
import streamlit as st

st.title('Counter Example using Callbacks with kwargs')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.button('Increment', on_click=increment_counter,
	kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
	kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.count)
```

### Example 4: Forms and Callbacks

Say we now want to not only increment the `count`, but also store when it was last updated. We illustrate doing this using Callbacks and `st.form`:

```python
import streamlit as st
import datetime

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Current Count = ', st.session_state.count)
st.write('Last Updated = ', st.session_state.last_updated)
```

## Advanced concepts

### Session State and Widget State association

Session State provides the functionality to store variables across reruns. Widget state (i.e. the value of a widget) is also stored in a session.

For simplicity, we have _unified_ this information in one place. i.e. the Session State. This convenience feature makes it super easy to read or write to the widget's state anywhere in the app's code. Session State variables mirror the widget value using the `key` argument.

We illustrate this with the following example. Let's say we have an app with a slider to represent temperature in Celsius. We can **set** and **get** the value of the temperature widget by using the Session State API, as follows:

```python
import streamlit as st

if "celsius" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = 50.0

st.slider(
    "Temperature in Celsius",
    min_value=-100.0,
    max_value=100.0,
    key="celsius"
)

# This will get the value of the slider widget
st.write(st.session_state.celsius)
```

There is a limitation to setting widget values using the Session State API.

<Important>

Streamlit **does not allow** setting widget values via the Session State API for `st.button` and `st.file_uploader`.

</Important>

The following example will raise a `StreamlitAPIException` on trying to set the state of `st.button` via the Session State API:

```python
import streamlit as st

if 'my_button' not in st.session_state:
    st.session_state.my_button = True
    # Streamlit will raise an Exception on trying to set the state of button

st.button('Submit', key='my_button')
```

<Image alt="state-button-exception" src="/images/state_button_exception.png" clean />

### Serializable Session State

Serialization refers to the process of converting an object or data structure into a format that can be persisted and shared, and allowing you to recover the dataΓÇÖs original structure. PythonΓÇÖs built-in [pickle](https://docs.python.org/3/library/pickle.html) module serializes Python objects to a byte stream ("pickling") and deserializes the stream into an object ("unpickling").

By default, StreamlitΓÇÖs [Session State](/develop/concepts/architecture/session-state) allows you to persist any Python object for the duration of the session, irrespective of the objectΓÇÖs pickle-serializability. This property lets you store Python primitives such as integers, floating-point numbers, complex numbers and booleans, dataframes, and even [lambdas](https://docs.python.org/3/reference/expressions.html#lambda) returned by functions. However, some execution environments may require serializing all data in Session State, so it may be useful to detect incompatibility during development, or when the execution environment will stop supporting it in the future.

To that end, Streamlit provides a `runner.enforceSerializableSessionState` [configuration option](/develop/concepts/configuration) that, when set to `true`, only allows pickle-serializable objects in Session State. To enable the option, either create a global or project config file with the following or use it as a command-line flag:

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

By "_pickle-serializable_", we mean calling `pickle.dumps(obj)` should not raise a [`PicklingError`](https://docs.python.org/3/library/pickle.html#pickle.PicklingError) exception. When the config option is enabled, adding unserializable data to session state should result in an exception. E.g.,

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#≡ƒæç results in an exception when enforceSerializableSessionState is on
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png" clean />

<Warning>

When `runner.enforceSerializableSessionState` is set to `true`, Session State implicitly uses the `pickle` module, which is known to be insecure. Ensure all data saved and retrieved from Session State is trusted because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

### Caveats and limitations

Here are some limitations to keep in mind when using Session State:

- Session State exists for as long as the tab is open and connected to the Streamlit server. As soon as you close the tab, everything stored in Session State is lost.
- Session State is not persisted. If the Streamlit server crashes, then everything stored in Session State gets wiped
- For caveats and limitations with the Session State API, please see the [API limitations](/develop/api-reference/caching-and-state/st.session_state#caveats-and-limitations).

```

File: concepts/architecture/architecture.md
```

---

title: Understanding Streamlit's client-server architecture
slug: /develop/concepts/architecture/architecture

---

# Understanding Streamlit's client-server architecture

Streamlit apps have a client-server structure. The Python backend of your app is the server. The frontend you view through a browswer is the client. When you develop an app locally, your computer runs both the server and the client. If someone views your app across a local or global network, the server and client run on different machines. If you intend to share or deploy your app, it's important to understand this client-server structure to avoid common pitfalls.

## Python backend (server)

When you execute the command `streamlit run your_app.py`, your computer uses Python to start up a Streamlit server. This server is the brains of your app and performs the computations for all users who view your app. Whether users view your app across a local network or the internet, the Streamlit server runs on the one machine where the app was initialized with `streamlit run`. The machine running your Streamlit server is also called a host.

## Browser frontend (client)

When someone views your app through a browser, their device is a Streamlit client. When you view your app from the same computer where you are running or developing your app, then server and client are coincidentally running on the same machine. However, when users view your app across a local network or the internet, the client runs on a different machine from the server.

## Server-client impact on app design

Keep in mind the following considerations when building your Streamlit app:

- The computer running or hosting your Streamlit app is responsible for providing the compute and storage necessary to run your app for all users and must be sized appropriately to handle concurrent users.
- Your app will not have access to a user's files, directories, or OS. Your app can only work with specific files a user has uploaded to your app through a widget like `st.file_uploader`.
- If your app communicates with any peripheral devices (like cameras), you must use Streamlit commands or custom components that will access those devices _through the user's browser_ and correctly communicate between the client (frontend) and server (backend).
- If your app opens or uses any program or process outside of Python, they will run on the server. For example, you may want to use `webrowser` to open a browser for the user, but this will not work as expected when viewing your app over a network; it will open a browser on the Streamlit server, unseen by the user.

```

File: concepts/architecture/forms.md
```

---

title: Using forms
slug: /develop/concepts/architecture/forms

---

# Using forms

When you don't want to rerun your script with each input made by a user, [`st.form`](/develop/api-reference/execution-flow/st.form) is here to help! Forms make it easy to batch user input into a single rerun. This guide to using forms provides examples and explains how users interact with forms.

## Example

In the following example, a user can set multiple parameters to update the map. As the user changes the parameters, the script will not rerun and the map will not update. When the user submits the form with the button labeled "**Update map**", the script reruns and the map updates.

If at any time the user clicks "**Generate new points**" which is outside of the form, the script will rerun. If the user has any unsubmitted changes within the form, these will _not_ be sent with the rerun. All changes made to a form will only be sent to the Python backend when the form itself is submitted.

<Collapse title="View source code" expanded={false} >

```python
import streamlit as st
import pandas as pd
import numpy as np

def get_data():
    df = pd.DataFrame({
        "lat": np.random.randn(200) / 50 + 37.76,
        "lon": np.random.randn(200) / 50 + -122.4,
        "team": ['A','B']*100
    })
    return df

if st.button('Generate new points'):
    st.session_state.df = get_data()
if 'df' not in st.session_state:
    st.session_state.df = get_data()
df = st.session_state.df

with st.form("my_form"):
    header = st.columns([1,2,2])
    header[0].subheader('Color')
    header[1].subheader('Opacity')
    header[2].subheader('Size')

    row1 = st.columns([1,2,2])
    colorA = row1[0].color_picker('Team A', '#0000FF')
    opacityA = row1[1].slider('A opacity', 20, 100, 50, label_visibility='hidden')
    sizeA = row1[2].slider('A size', 50, 200, 100, step=10, label_visibility='hidden')

    row2 = st.columns([1,2,2])
    colorB = row2[0].color_picker('Team B', '#FF0000')
    opacityB = row2[1].slider('B opacity', 20, 100, 50, label_visibility='hidden')
    sizeB = row2[2].slider('B size', 50, 200, 100, step=10, label_visibility='hidden')

    st.form_submit_button('Update map')

alphaA = int(opacityA*255/100)
alphaB = int(opacityB*255/100)

df['color'] = np.where(df.team=='A',colorA+f'{alphaA:02x}',colorB+f'{alphaB:02x}')
df['size'] = np.where(df.team=='A',sizeA, sizeB)

st.map(df, size='size', color='color')
```

</Collapse>

<Cloud src="https://doc-forms-overview.streamlit.app/?embed=true" height="800"/>

## User interaction

If a widget is not in a form, that widget will trigger a script rerun whenever a user changes its value. For widgets with keyed input (`st.number_input`, `st.text_input`, `st.text_area`), a new value triggers a rerun when the user clicks or tabs out of the widget. A user can also submit a change by pressing `Enter` while thier cursor is active in the widget.

On the other hand if a widget is inside of a form, the script will not rerun when a user clicks or tabs out of that widget. For widgets inside a form, the script will rerun when the form is submitted and all widgets within the form will send their updated values to the Python backend.

![Forms](/images/forms.gif)

A user can submit a form using **Enter** on their keyboard if their cursor active in a widget that accepts keyed input. Within `st.number_input` and `st.text_input` a user presses **Enter** to submit the form. Within `st.text_area` a user presses **Ctrl+Enter**/**Γîÿ+Enter** to submit the form.

![Keyboard-submit forms](/images/form-submit-keyboard.png)

## Widget values

Before a form is submitted, all widgets within that form will have default values, just like widgets outside of a form have default values.

```python
import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   my_number = st.slider('Pick a number', 1, 10)
   my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.form_submit_button('Submit my picks')

# This is outside the form
st.write(my_number)
st.write(my_color)
```

<Cloud src="https://doc-forms-default.streamlit.app/?embed=true" height="450"/>

## Forms are containers

When `st.form` is called, a container is created on the frontend. You can write to that container like you do with other [container elements](/develop/api-reference/layout). That is, you can use Python's `with` statement as shown in the example above, or you can assign the form container to a variable and call methods on it directly. Additionally, you can place `st.form_submit_button` anywhere in the form container.

```python
import streamlit as st

animal = st.form('my_animal')

# This is writing directly to the main body. Since the form container is
# defined above, this will appear below everything written in the form.
sound = st.selectbox('Sounds like', ['meow','woof','squeak','tweet'])

# These methods called on the form container, so they appear inside the form.
submit = animal.form_submit_button(f'Say it with {sound}!')
sentence = animal.text_input('Your sentence:', 'Where\'s the tuna?')
say_it = sentence.rstrip('.,!?') + f', {sound}!'
if submit:
    animal.subheader(say_it)
else:
    animal.subheader('&nbsp;')
```

<Cloud src="https://doc-forms-container.streamlit.app/?embed=true" height="375"/>

## Processing form submissions

The purpose of a form is to override the default behavior of Streamlit which reruns a script as soon as the user makes a change. For widgets outside of a form, the logical flow is:

1. The user changes a widget's value on the frontend.
2. The widget's value in `st.session_state` and in the Python backend (server) is updated.
3. The script rerun begins.
4. If the widget has a callback, it is executed as a prefix to the page rerun.
5. When the updated widget's function is executed during the rerun, it outputs the new value.

For widgets inside a form, any changes made by a user (step 1) do not get passed to the Python backend (step 2) until the form is submitted. Furthermore, the only widget inside a form that can have a callback function is the `st.form_submit_button`. If you need to execute a process using newly submitted values, you have three major patterns for doing so.

### Execute the process after the form

If you need to execute a one-time process as a result of a form submission, you can condition that process on the `st.form_submit_button` and execute it after the form. If you need results from your process to display above the form, you can use containers to control where the form displays relative to your output.

```python
import streamlit as st

col1,col2 = st.columns([1,2])
col1.title('Sum:')

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

if submit:
    col2.title(f'{a+b:.2f}')
```

<Cloud src="https://doc-forms-process1.streamlit.app/?embed=true" height="400"/>

### Use a callback with session state

You can use a callback to execute a process as a prefix to the script rerunning.

<Important>

When processing newly updated values within a callback, do not pass those values to the callback directly through the `args` or `kwargs` parameters. You need to assign a key to any widget whose value you use within the callback. If you look up the value of that widget from `st.session_state` within the body of the callback, you will be able to access the newly submitted value. See the example below.

</Important>

```python
import streamlit as st

if 'sum' not in st.session_state:
    st.session_state.sum = ''

def sum():
    result = st.session_state.a + st.session_state.b
    st.session_state.sum = result

col1,col2 = st.columns(2)
col1.title('Sum:')
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

with st.form('addition'):
    st.number_input('a', key = 'a')
    st.number_input('b', key = 'b')
    st.form_submit_button('add', on_click=sum)
```

<Cloud src="https://doc-forms-process2.streamlit.app/?embed=true" height="400"/>

### Use `st.rerun`

If your process affects content above your form, another alternative is using an extra rerun. This can be less resource-efficient though, and may be less desirable that the above options.

```python
import streamlit as st

if 'sum' not in st.session_state:
    st.session_state.sum = ''

col1,col2 = st.columns(2)
col1.title('Sum:')
if isinstance(st.session_state.sum, float):
    col2.title(f'{st.session_state.sum:.2f}')

with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

# The value of st.session_state.sum is updated at the end of the script rerun,
# so the displayed value at the top in col2 does not show the new sum. Trigger
# a second rerun when the form is submitted to update the value above.
st.session_state.sum = a + b
if submit:
    st.rerun()
```

<Cloud src="https://doc-forms-process3.streamlit.app/?embed=true" height="400"/>

## Limitations

- Every form must contain a `st.form_submit_button`.
- `st.button` and `st.download_button` cannot be added to a form.
- `st.form` cannot be embedded inside another `st.form`.
- Callback functions can only be assigned to `st.form_submit_button` within a form; no other widgets in a form can have a callback.
- Interdependent widgets within a form are unlikely to be particularly useful. If you pass `widget1`'s value into `widget2` when they are both inside a form, then `widget2` will only update when the form is submitted.

```

File: concepts/architecture/_index.md
```

---

title: Working with Streamlit's execution model
slug: /develop/concepts/architecture

---

# Working with Streamlit's execution model

<TileContainer layout="list">

<RefCard href="/develop/concepts/architecture/run-your-app">

<h5>Run your app</h5>

Understand how to start your Streamlit app.

</RefCard>

<RefCard href="/develop/concepts/architecture/architecture">

<h5>Streamlit's architecture</h5>

Understand Streamlit's client-server architecture and related considerations.

</RefCard>

<RefCard href="/develop/concepts/architecture/app-chrome">

<h5>The app chrome</h5>

Every Streamlit app has a few widgets in the top right to help you as you develop your app and help your users as they view your app. This is called the app chrome.

</RefCard>

<RefCard href="/develop/concepts/architecture/caching">

<h5>Caching</h5>

Make your app performant by caching results to avoid unecessary recomputation with each rerun.

</RefCard>

<RefCard href="/develop/concepts/architecture/session-state">

<h5>Session State</h5>

Manage your app's statefulness with Session State.

</RefCard>

<RefCard href="/develop/concepts/architecture/forms">

<h5>Forms</h5>

Use forms to isolate user input and prevent unnecessary app reruns.

</RefCard>

<RefCard href="/develop/concepts/architecture/widget-behavior">

<h5>Widget behavior</h5>

Understand how widgets work in detail.

</RefCard>

</TileContainer>

```

File: concepts/architecture/widget-behavior.md
```

---

title: Widget behavior
slug: /develop/concepts/architecture/widget-behavior

---

# Understanding widget behavior

Widgets (like `st.button`, `st.selectbox`, and `st.text_input`) are at the heart of Streamlit apps. They are the interactive elements of Streamlit that pass information from your users into your Python code. Widgets are magical and often work how you want, but they can have surprising behavior in some situations. Understanding the different parts of a widget and the precise order in which events occur helps you achieve your desired results.

This guide covers advanced concepts about widgets. Generally, it begins with simpler concepts and increases in complexity. For most beginning users, these details won't be important to know right away. When you want to dynamically change widgets or preserve widget information between pages, these concepts will be important to understand. We recommend having a basic understanding of [Session State](/develop/api-reference/caching-and-state/st.session_state) before reading this guide.

<Collapse title="≡ƒÄê TL;DR" expanded={false}>

1. The actions of one user do not affect the widgets of any other user.
2. A widget function call returns the widget's current value, which is a simple Python type. (e.g. `st.button` returns a boolean value.)
3. Widgets return their default values on their first call before a user interacts with them.
4. A widget's identity depends on the arguments passed to the widget function. Changing a widget's label, min or max value, default value, placeholder text, help text, or key will cause it to reset.
5. If you don't call a widget function in a script run, Streamlit will delete the widget's information&mdash;_including its key-value pair in Session State_. If you call the same widget function later, Streamlit treats it as a new widget.

The last two points (widget identity and widget deletion) are the most relevant when dynamically changing widgets or working with multi-page applications. This is covered in detail later in this guide: [Statefulness of widgets](#statefulness-of-widgets) and [Widget life cycle](#widget-life-cycle).

</Collapse>

## Anatomy of a widget

There are four parts to keep in mind when using widgets:

1. The frontend component as seen by the user.
2. The backend value or value as seen through `st.session_state`.
3. The key of the widget used to access its value via `st.session_state`.
4. The return value given by the widget's function.

### Widgets are session dependent

Widget states are dependent on a particular session (browser connection). The actions of one user do not affect the widgets of any other user. Furthermore, if a user opens up multiple tabs to access an app, each tab will be a unique session. Changing a widget in one tab will not affect the same widget in another tab.

### Widgets return simple Python data types

The value of a widget as seen through `st.session_state` and returned by the widget function are of simple Python types. For example, `st.button` returns a boolean value and will have the same boolean value saved in `st.session_state` if using a key. The first time a widget function is called (before a user interacts with it), it will return its default value. (e.g. `st.selectbox` returns the first option by default.) Default values are configurable for all widgets with a few special exceptions like `st.button` and `st.file_uploader`.

### Keys help distinguish widgets and access their values

Widget keys serve two purposes:

1. Distinguishing two otherwise identical widgets.
2. Creating a means to access and manipulate the widget's value through `st.session_state`.

Whenever possible, Streamlit updates widgets incrementally on the frontend instead of rebuilding them with each rerun. This means Streamlit assigns an ID to each widget from the arguments passed to the widget function. A widget's ID is based on parameters such as label, min or max value, default value, placeholder text, help text, and key. The page where the widget appears also factors into a widget's ID. If you have two widgets of the same type with the same arguments on the same page, you will get a `DuplicateWidgetID` error. In this case, assign unique keys to the two widgets.

#### Streamlit can't understand two identical widgets on the same page

```python
# This will cause a DuplicateWidgetID error.
st.button("OK")
st.button("OK")
```

#### Use keys to distinguish otherwise identical widgets

```python
st.button("OK", key="privacy")
st.button("OK", key="terms")
```

## Order of operations

When a user interacts with a widget, the order of logic is:

1. Its value in `st.session_state` is updated.
2. The callback function (if any) is executed.
3. The page reruns with the widget function returning its new value.

If the callback function writes anything to the screen, that content will appear above the rest of the page. A callback function runs as a _prefix_ to the script rerunning. Consequently, that means anything written via a callback function will disappear as soon as the user performs their next action. Other widgets should generally not be created within a callback function.

<Note>

If a callback function is passed any args or kwargs, those arguments will be established when the widget is rendered. In particular, if you want to use a widget's new value in its own callback function, you cannot pass that value to the callback function via the `args` parameter; you will have to assign a key to the widget and look up its new value using a call to `st.session_state` _within the callback function_.

</Note>

### Using callback functions with forms

Using a callback function with a form requires consideration of this order of operations.

```python
import streamlit as st

if "attendance" not in st.session_state:
    st.session_state.attendance = set()


def take_attendance():
    if st.session_state.name in st.session_state.attendance:
        st.info(f"{st.session_state.name} has already been counted.")
    else:
        st.session_state.attendance.add(st.session_state.name)


with st.form(key="my_form"):
    st.text_input("Name", key="name")
    st.form_submit_button("I'm here!", on_click=take_attendance)
```

<Cloud src="https://doc-guide-widgets-form-callbacks.streamlit.app/?embed=true" height="250"/>

## Statefulness of widgets

As long as the defining parameters of a widget remain the same and that widget is continuously rendered on the frontend, then it will be stateful and remember user input.

### Changing parameters of a widget will reset it

If any of the defining parameters of a widget change, Streamlit will see it as a new widget and it will reset. The use of manually assigned keys and default values is particularly important in this case. _Note that callback functions, callback args and kwargs, label visibility, and disabling a widget do not affect a widget's identity._

In this example, we have a slider whose min and max values are changed. Try interacting with each slider to change its value then change the min or max setting to see what happens.

```python
import streamlit as st

cols = st.columns([2, 1, 2])
minimum = cols[0].number_input("Minimum", 1, 5)
maximum = cols[2].number_input("Maximum", 6, 10, 10)

st.slider("No default, no key", minimum, maximum)
st.slider("No default, with key", minimum, maximum, key="a")
st.slider("With default, no key", minimum, maximum, value=5)
st.slider("With default, with key", minimum, maximum, value=5, key="b")
```

<Cloud src="https://doc-guide-widgets-change-parameters.streamlit.app/?embed=true" height="550"/>

#### Updating a slider with no default value

For the first two sliders above, as soon as the min or max value is changed, the sliders reset to the min value. The changing of the min or max value makes them "new" widgets from Streamlit's perspective and so they are recreated from scratch when the app reruns with the changed parameters. Since no default value is defined, each widget will reset to its min value. This is the same with or without a key since it's seen as a new widget either way. There is a subtle point to understand about pre-existing keys connecting to widgets. This will be explained further down in [Widget life cycle](#widget-life-cycle).

#### Updating a slider with a default value

For the last two sliders above, a change to the min or max value will result in the widgets being seen as "new" and thus recreated like before. Since a default value of 5 is defined, each widget will reset to 5 whenever the min or max is changed. This is again the same (with or without a key).

A solution to [Retain statefulness when changing a widget's parameters](#retain-statefulness-when-changing-a-widgets-parameters) is provided further on.

### Widgets do not persist when not continually rendered

If a widget's function is not called during a script run, then none of its parts will be retained, including its value in `st.session_state`. If a widget has a key and you navigate away from that widget, its key and associated value in `st.session_state` will be deleted. Even temporarily hiding a widget will cause it to reset when it reappears; Streamlit will treat it like a new widget. You can either interrupt the [Widget clean-up process](#widget-clean-up-process) (described at the end of this page) or save the value to another key.

#### Save widget values in Session State to preserve them between pages

If you want to navigate away from a widget and return to it while keeping its value, use a separate key in `st.session_state` to save the information independently from the widget. In this example, a temporary key is used with a widget. The temporary key uses an underscore prefix. Hence, `_my_key` is used as the widget key, but the data is copied to `my_key` to preserve it between pages.

```python
import streamlit as st

def save_value():
    # Copy the value to the permanent key
    st.session_state["my_key"] = st.session_state["_my_key"]

# Copy the saved value to the temporary key
st.session_state["_my_key"] = st.session_state["my_key"]
st.number_input("Number of filters", key="_my_key", on_change=save_value)
```

If this is functionalized to work with multiple widgets, it could look something like this:

```python
import streamlit as st

def save_value(key):
    st.session_state[key] = st.session_state["_"+key]
def get_value(key):
    st.session_state["_"+key] = st.session_state[key]

get_value("my_key")
st.number_input("Number of filters", key="_my_key", on_change=save_value, args="my_key")

```

## Widget life cycle

When a widget function is called, Streamlit will check if it already has a widget with the same parameters. Streamlit will reconnect if it thinks the widget already exists. Otherwise, it will make a new one.

As mentioned earlier, Streamlit determines a widget's ID based on parameters such as label, min or max value, default value, placeholder text, help text, and key. The page name also factors into a widget's ID. On the other hand, callback functions, callback args and kwargs, label visibility, and disabling a widget do not affect a widget's identity.

### Calling a widget function when the widget doesn't already exist

If your script rerun calls a widget function with changed parameters or calls a widget function that wasn't used on the last script run:

1. Streamlit will build the frontend and backend parts of the widget.
2. If the widget has been assigned a key, Streamlit will check if that key already exists in Session State.  
   a. If it exists and is not currently associated with another widget, Streamlit will attach to that key and take on its value for the widget.  
   b. Otherwise, it will assign the default value to the key in `st.session_state` (creating a new key-value pair or overwriting an existing one).
3. If there are args or kwargs for a callback function, they are computed and saved at this point in time.
4. The default value is then returned by the function.

Step 2 can be tricky. If you have a widget:

```python
st.number_input("Alpha",key="A")
```

and you change it on a page rerun to:

```python
st.number_input("Beta",key="A")
```

Streamlit will see that as a new widget because of the label change. The key `"A"` will be considered part of the widget labeled `"Alpha"` and will not be attached as-is to the new widget labeled `"Beta"`. Streamlit will destroy `st.session_state.A` and recreate it with the default value.

If a widget attaches to a pre-existing key when created and is also manually assigned a default value, you will get a warning if there is a disparity. If you want to control a widget's value through `st.session_state`, initialize the widget's value through `st.session_state` and avoid the default value argument to prevent conflict.

### Calling a widget function when the widget already exists

When rerunning a script without changing a widget's parameters:

1. Streamlit will connect to the existing frontend and backend parts.
2. If the widget has a key that was deleted from `st.session_state`, then Streamlit will recreate the key using the current frontend value. (e.g Deleting a key will not revert the widget to a default value.)
3. It will return the current value of the widget.

### Widget clean-up process

When Streamlit gets to the end of a script run, it will delete the data for any widgets it has in memory that were not rendered on the screen. Most importantly, that means Streamlit will delete all key-value pairs in `st.session_state` associated with a widget not currently on screen.

## Additional examples

As promised, let's address how to retain the statefulness of widgets when changing pages or modifying their parameters. There are two ways to do this.

1. Use dummy keys to duplicate widget values in `st.session_state` and protect the data from being deleted along with the widget.
2. Interrupt the widget clean-up process.

The first method was shown above in [Save widget values in Session State to preserve them between pages](#save-widget-values-in-session-state-to-preserve-them-between-pages)

### Interrupting the widget clean-up process

To retain information for a widget with `key="my_key"`, just add this to the top of every page:

```python
st.session_state.my_key = st.session_state.my_key
```

When you manually save data to a key in `st.session_state`, it will become detached from any widget as far as the clean-up process is concerned. If you navigate away from a widget with some key `"my_key"` and save data to `st.session_state.my_key` on the new page, you will interrupt the widget clean-up process and prevent the key-value pair from being deleted or overwritten if another widget with the same key exists.

### Retain statefulness when changing a widget's parameters

Here is a solution to our earlier example of changing a slider's min and max values. This solution interrupts the clean-up process as described above.

```python
import streamlit as st

# Set default value
if "a" not in st.session_state:
    st.session_state.a = 5

cols = st.columns(2)
minimum = cols[0].number_input("Min", 1, 5, key="min")
maximum = cols[1].number_input("Max", 6, 10, 10, key="max")


def update_value():
    # Helper function to ensure consistency between widget parameters and value
    st.session_state.a = min(st.session_state.a, maximum)
    st.session_state.a = max(st.session_state.a, minimum)


# Validate the slider value before rendering
update_value()
st.slider("A", minimum, maximum, key="a")
```

<Cloud src="https://doc-guide-widgets-change-parameters-solution.streamlit.app/?embed=true" height="250"/>

The `update_value()` helper function is actually doing two things. On the surface, it's making sure there are no inconsistent changes to the parameters values as described. Importantly, it's also interrupting the widget clean-up process. When the min or max value of the widget changes, Streamlit sees it as a new widget on rerun. Without saving a value to `st.session_state.a`, the value would be thrown out and replaced by the "new" widget's default value.

```

File: concepts/app-design/animate-elements.md
```

---

title: Animate and update elements
slug: /develop/concepts/design/animate
description: st.add_rows appends a dataframe to the bottom of the current one in certain elements, for optimized data updates.

---

# Animate and update elements

Sometimes you display a chart or dataframe and want to modify it live as the app
runs (for example, in a loop). Some elements have built-in methods to allow you
to update them in-place without rerunning the app.

Updatable elements include the following:

- `st.empty` containers can be written to in sequence and will always show the last thing written. They can also be cleared with an
  additional `.empty()` called like a method.
- `st.dataframe`, `st.table`, and many chart elements can be updated with the `.add_rows()` method which appends data.
- `st.progress` elements can be updated with additional `.progress()` calls. They can also be cleared with a `.empty()` method call.
- `st.status` containers have an `.update()` method to change their labels, expanded state, and status.
- `st.toast` messages can be updated in place with additional `.toast()` calls.

## `st.empty` containers

`st.empty` can hold a single element. When you write any element to an `st.empty` container, Streamlit discards its previous content
displays the new element. You can also `st.empty` containers by calling `.empty()` as a method. If you want to update a set of elements, use
a plain container (`st.container()`) inside `st.empty` and write contents to the plain container. Rewrite the plain container and its
contents as often as desired to update your app's display.

## The `.add_rows()` method

`st.dataframe`, `st.table`, and all chart functions can be mutated using the `.add_rows()` method on their output. In the following example, we use `my_data_element = st.line_chart(df)`. You can try the example with `st.table`, `st.dataframe`, and most of the other simple charts by just swapping out `st.line_chart`. Note that `st.dataframe` only shows the first ten rows by default and enables scrolling for additional rows. This means adding rows is not as visually apparent as it is with `st.table` or the chart elements.

```python
import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
my_data_element = st.line_chart(df)

for tick in range(10):
    time.sleep(.5)
    add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
    my_data_element.add_rows(add_df)

st.button("Regenerate")
```

```

File: concepts/app-design/custom-classes.md
```

---

title: Using custom Python classes in your Streamlit app
slug: /develop/concepts/design/custom-classes

---

# Using custom Python classes in your Streamlit app

If you are building a complex Streamlit app or working with existing code, you may have custom Python classes defined in your script. Common examples include the following:

- Defining a `@dataclass` to store related data within your app.
- Defining an `Enum` class to represent a fixed set of options or values.
- Defining custom interfaces to external services or databases not covered by [`st.connection`](/develop/api-reference/connections/st.connection).

Because Streamlit reruns your script after every user interaction, custom classes may be redefined multiple times within the same Streamlit session. This may result in unwanted effects, especially with class and instance comparisons. Read on to understand this common pitfall and how to avoid it.

We begin by covering some general-purpose patterns you can use for different types of custom classes, and follow with a few more technical details explaining why this matters. Finally, we go into more detail about [Using `Enum` classes](#using-enum-classes-in-streamlit) specifically, and describe a configuration option which can make them more convenient.

## Patterns to define your custom classes

### Pattern 1: Define your class in a separate module

This is the recommended, general solution. If possible, move class definitions into their own module file and import them into your app script. As long as you are not editing the file where your class is defined, Streamlit will not re-import it with each rerun. Therefore, if a class is defined in an external file and imported into your script, the class will not be redefined during the session.

#### Example: Move your class definition

Try running the following Streamlit app where `MyClass` is defined within the page's script. `isinstance()` will return `True` on the first script run then return `False` on each rerun thereafter.

```python
# app.py
import streamlit as st

# MyClass gets redefined every time app.py reruns
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on the first run then False on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")
```

If you move the class definition out of `app.py` into another file, you can make `isinstance()` consistently return `True`. Consider the following file structure:

```
myproject/
Γö£ΓöÇΓöÇ my_class.py
ΓööΓöÇΓöÇ app.py
```

```python
# my_class.py
class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
```

```python
# app.py
import streamlit as st
from my_class import MyClass # MyClass doesn't get redefined with each rerun

if "my_instance" not in st.session_state:
  st.session_state.my_instance = MyClass("foo", "bar")

# Displays True on every rerun
st.write(isinstance(st.session_state.my_instance, MyClass))

st.button("Rerun")
```

Streamlit only reloads code in imported modules when it detects the code has changed. Thus, if you are actively editing the file where your class is defined, you may need to stop and restart your Streamlit server to avoid an undesirable class redefinition mid-session.

### Pattern 2: Force your class to compare internal values

For classes that store data (like [dataclasses](https://docs.python.org/3/library/dataclasses.html)), you may be more interested in comparing the internally stored values rather than the class itself. If you define a custom `__eq__` method, you can force comparisons to be made on the internally stored values.

#### Example: Define `__eq__`

Try running the following Streamlit app and observe how the comparison is `True` on the first run then `False` on every rerun thereafter.

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5)

# Displays True on the first run the False on every rerun
st.session_state.my_dataclass == MyDataclass(1, 5.5)

st.button("Rerun")
```

Since `MyDataclass` gets redefined with each rerun, the instance stored in Session State will not be equal to any instance defined in a later script run. You can fix this by forcing a comparison of internal values as follows:

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

    def __eq__(self, other):
        # An instance of MyDataclass is equal to another object if the object
        # contains the same fields with the same values
        return (self.var1, self.var2) == (other.var1, other.var2)

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5)

# Displays True on every rerun
st.session_state.my_dataclass == MyDataclass(1, 5.5)

st.button("Rerun")
```

The default Python `__eq__` implementation for a regular class or `@dataclass` depends on the in-memory ID of the class or class instance. To avoid problems in Streamlit, your custom `__eq__` method should not depend the `type()` of `self` and `other`.

### Pattern 3: Store your class as serialized data

Another option for classes that store data is to define serialization and deserialization methods like `to_str` and `from_str` for your class. You can use these to store class instance data in `st.session_state` rather than storing the class instance itself. Similar to pattern 2, this is a way to force comparison of the internal data and bypass the changing in-memory IDs.

#### Example: Save your class instance as a string

Using the same example from pattern 2, this can be done as follows:

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class MyDataclass:
    var1: int
    var2: float

    def to_str(self):
        return f"{self.var1},{self.var2}"

    @classmethod
    def from_str(cls, serial_str):
        values = serial_str.split(",")
        var1 = int(values[0])
        var2 = float(values[1])
        return cls(var1, var2)

if "my_dataclass" not in st.session_state:
    st.session_state.my_dataclass = MyDataclass(1, 5.5).to_str()

# Displays True on every rerun
MyDataclass.from_str(st.session_state.my_dataclass) == MyDataclass(1, 5.5)

st.button("Rerun")
```

### Pattern 4: Use caching to preserve your class

For classes that are used as resources (database connections, state managers, APIs), consider using the cached singleton pattern. Use `@st.cache_resource` to decorate a `@staticmethod` of your class to generate a single, cached instance of the class. For example:

```python
import streamlit as st

class MyResource:
    def __init__(self, api_url: str):
        self._url = api_url

    @st.cache_resource(ttl=300)
    @staticmethod
    def get_resource_manager(api_url: str):
        return MyResource(api_url)

# This is cached until Session State is cleared or 5 minutes has elapsed.
resource_manager = MyResource.get_resource_manager("http://example.com/api/")
```

When you use one of Streamlit's caching decorators on a function, Streamlit doesn't use the function object to look up cached values. Instead, Streamlit's caching decorators index return values using the function's qualified name and module. So, even though Streamlit redefines `MyResource` with each script run, `st.cache_resource` is unaffected by this. `get_resource_manager()` will return its cached value with each rerun, until the value expires.

## Understanding how Python defines and compares classes

So what's really happening here? We'll consider a simple example to illustrate why this is a pitfall. Feel free to skip this section if you don't want to deal more details. You can jump ahead to learn about [Using `Enum` classes](#using-enum-classes-in-streamlit).

### Example: What happens when you define the same class twice?

Set aside Streamlit for a moment and think about this simple Python script:

```python
from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str

Marshall_A = Student(1, "Marshall")
Marshall_B = Student(1, "Marshall")

# This is True (because a dataclass will compare two of its instances by value)
Marshall_A == Marshall_B

# Redefine the class
@dataclass
class Student:
    student_id: int
    name: str

Marshall_C = Student(1, "Marshall")

# This is False
Marshall_A == Marshall_C
```

In this example, the dataclass `Student` is defined twice. All three Marshalls have the same internal values. If you compare `Marshall_A` and `Marshall_B` they will be equal because they were both created from the first definition of `Student`. However, if you compare `Marshall_A` and `Marshall_C` they will not be equal because `Marshall_C` was created from the _second_ definition of `Student`. Even though both `Student` dataclasses are defined exactly the same, they have differnt in-memory IDs and are therefore different.

### What's happening in Streamlit?

In Streamlit, you probably don't have the same class written twice in your page script. However, the rerun logic of Streamlit creates the same effect. Let's use the above example for an analogy. If you define a class in one script run and save an instance in Session State, then a later rerun will redefine the class and you may end up comparing a `Mashall_C` in your rerun to a `Marshall_A` in Session State. Since widgets rely on Session State under the hood, this is where things can get confusing.

## How Streamlit widgets store options

Several Streamlit UI elements, such as `st.selectbox` or `st.radio`, accept multiple-choice options via an `options` argument. The user of your application can typically select one or more of these options. The selected value is returned by the widget function. For example:

```python
number = st.selectbox("Pick a number, any number", options=[1, 2, 3])
# number == whatever value the user has selected from the UI.
```

When you call a function like `st.selectbox` and pass an `Iterable` to `options`, the `Iterable` and current selection are saved into a hidden portion of [Session State](/develop/concepts/architecture/session-state) called the Widget Metadata.

When the user of your application interacts with the `st.selectbox` widget, the broswer sends the index of their selection to your Streamlit server. This index is used to determine which values from the original `options` list, _saved in the Widget Metadata from the previous page execution_, are returned to your application.

The key detail is that the value returned by `st.selectbox` (or similar widget function) is from an `Iterable` saved in Session State during a _previous_ execution of the page, NOT the values passed to `options` on the _current_ execution. There are a number of architectural reasons why Streamlit is designed this way, which we won't go into here. However, **this** is how we end up comparing instances of different classes when we think we are comparing instances of the same class.

### A pathological example

The above explanation might be a bit confusing, so here's a pathological example to illustrate the idea.

```python
import streamlit as st
from dataclasses import dataclass

@dataclass
class Student:
    student_id: int
    name: str

Marshall_A = Student(1, "Marshall")
if "B" not in st.session_state:
    st.session_state.B = Student(1, "Marshall")
Marshall_B = st.session_state.B

options = [Marshall_A,Marshall_B]
selected = st.selectbox("Pick", options)

# This comparison does not return expected results:
selected == Marshall_A
# This comparison evaluates as expected:
selected == Marshall_B
```

As a final note, we used `@dataclass` in the example for this section to illustrate a point, but in fact it is possible to encounter these same problems with classes, in general. Any class which checks class identity inside of a comparison operator&mdash;such as `__eq__` or `__gt__`&mdash;can exhibit these issues.

## Using `Enum` classes in Streamlit

The [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum) class from the Python standard library is a powerful way to define custom symbolic names that can be used as options for `st.multiselect` or `st.selectbox` in place of `str` values.

For example, you might add the following to your streamlit page:

```python
from enum import Enum
import streamlit as st

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

selected_colors = set(st.multiselect("Pick colors", options=Color))

if selected_colors == {Color.RED, Color.GREEN}:
    st.write("Hooray, you found the color YELLOW!")
```

If you're using the latest version of Streamlit, this Streamlit page will work as it appears it should. When a user picks both `Color.RED` and `Color.GREEN`, they are shown the special message.

However, if you've read the rest of this page you might notice something tricky going on. Specifically, the `Enum` class `Color` gets redefined every time this script is run. In Python, if you define two `Enum` classes with the same class name, members, and values, the classes and their members are still considered unique from each other. This _should_ cause the above `if` condition to always evaluate to `False`. In any script rerun, the `Color` values returned by `st.multiselect` would be of a different class than the `Color` defined in that script run.

If you run the snippet above with Streamlit version 1.28.0 or less, you will not be able see the special message. Thankfully, as of version 1.29.0, Streamlit introduced a configuration option to greatly simplify the problem. That's where the enabled-by-default `enumCoercion` configuration option comes in.

### Understanding the `enumCoercion` configuration option

When `enumCoercion` is enabled, Streamlit tries to recognize when you are using an element like `st.multiselect` or `st.selectbox` with a set of `Enum` members as options.

If Streamlit detects this, it will convert the widget's returned values to members of the `Enum` class defined in the latest script run. This is something we call automatic `Enum` coercion.

This behavior is [configurable](/develop/concepts/configuration) via the `enumCoercion` setting in your Streamlit `config.toml` file. It is enabled by default, and may be disabled or set to a stricter set of matching criteria.

If you find that you still encounter issues with `enumCoercion` enabled, consider using the [custom class patterns](#patterns-to-define-your-custom-classes) described above, such as moving your `Enum` class definition to a separate module file.

```

File: concepts/app-design/button-behavior-and-examples.md
```

---

title: Button behavior and examples
slug: /develop/concepts/design/buttons

---

# Button behavior and examples

## Summary

Buttons created with [`st.button`](/develop/api-reference/widgets/st.button) do not retain state. They return `True` on the script rerun resulting from their click and immediately return to `False` on the next script rerun. If a displayed element is nested inside `if st.button('Click me'):`, the element will be visible when the button is clicked and disappear as soon as the user takes their next action. This is because the script reruns and the button return value becomes `False`.

In this guide, we will illustrate the use of buttons and explain common misconceptions. Read on to see a variety of examples that expand on `st.button` using [`st.session_state`](/develop/api-reference/caching-and-state/st.session_state). [Anti-patterns](#anti-patterns) are included at the end. Go ahead and pull up your favorite code editor so you can `streamlit run` the examples as you read. Check out Streamlit's [Basic concepts](/get-started/fundamentals/main-concepts) if you haven't run your own Streamlit scripts yet.

## When to use `if st.button()`

When code is conditioned on a button's value, it will execute once in response to the button being clicked and not again (until the button is clicked again).

Good to nest inside buttons:

- Transient messages that immediately disappear.
- Once-per-click processes that saves data to session state, a file, or
  a database.

Bad to nest inside buttons:

- Displayed items that should persist as the user continues.
- Other widgets which cause the script to rerun when used.
- Processes that neither modify session state nor write to a file/database.\*

\* This can be appropriate when disposable results are desired. If you
have a "Validate" button, that could be a process conditioned directly on a
button. It could be used to create an alert to say 'Valid' or 'Invalid' with no
need to keep that info.

## Common logic with buttons

### Show a temporary message with a button

If you want to give the user a quick button to check if an entry is valid, but not keep that check displayed as the user continues.

In this example, a user can click a button to check if their `animal` string is in the `animal_shelter` list. When the user clicks "**Check availability**" they will see "We have that animal!" or "We don't have that animal." If they change the animal in [`st.text_input`](/develop/api-reference/widgets/st.text_input), the script reruns and the message disappears until they click "**Check availability**" again.

```python
import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'
```

Note: The above example uses [magic](/develop/api-reference/write-magic/magic) to render the message on the frontend.

### Stateful button

If you want a clicked button to continue to be `True`, create a value in `st.session_state` and use the button to set that value to `True` in a callback.

```python
import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Click me', on_click=click_button)

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write('Button clicked!')
    st.slider('Select a value')
```

### Toggle button

If you want a button to work like a toggle switch, consider using [`st.checkbox`](/develop/api-reference/widgets/st.checkbox). Otherwise, you can use a button with a callback function to reverse a boolean value saved in `st.session_state`.

In this example, we use `st.button` to toggle another widget on and off. By displaying [`st.slider`](/develop/api-reference/widgets/st.slider) conditionally on a value in `st.session_state`, the user can interact with the slider without it disappearing.

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')
```

Alternatively, you can use the value in `st.session_state` on the slider's `disabled` parameter.

```python
import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

st.slider('Select a value', disabled=st.session_state.button)
```

### Buttons to continue or control stages of a process

Another alternative to nesting content inside a button is to use a value in `st.session_state` that designates the "step" or "stage" of a process. In this example, we have four stages in our script:

0. Before the user begins.
1. User enters their name.
2. User chooses a color.
3. User gets a thank-you message.

A button at the beginning advances the stage from 0 to 1. A button at the end resets the stage from 3 to 0. The other widgets used in stage 1 and 2 have callbacks to set the stage. If you have a process with dependant steps and want to keep previous stages visible, such a callback forces a user to retrace subsequent stages if they change an earlier widget.

```python
import streamlit as st

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input('Name', on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f'Hello {name}!')
    color = st.selectbox(
        'Pick a Color',
        [None, 'red', 'orange', 'green', 'blue', 'violet'],
        on_change=set_state, args=[3]
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f':{color}[Thank you!]')
    st.button('Start Over', on_click=set_state, args=[0])
```

### Buttons to modify `st.session_state`

If you modify `st.session_state` inside of a button, you must consider where that button is within the script.

#### A slight problem

In this example, we access `st.session_state.name` both before and after the buttons which modify it. When a button ("**Jane**" or "**John**") is clicked, the script reruns. The info displayed before the buttons lags behind the info written after the button. The data in `st.session_state` before the button is not updated. When the script executes the button function, that is when the conditional code to update `st.session_state` creates the change. Thus, this change is reflected after the button.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'

if st.button('John'):
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])
```

#### Logic used in a callback

Callbacks are a clean way to modify `st.session_state`. Callbacks are executed as a prefix to the script rerunning, so the position of the button relative to accessing data is not important.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

def change_name(name):
    st.session_state['name'] = name

st.header(st.session_state['name'])

st.button('Jane', on_click=change_name, args=['Jane Doe'])
st.button('John', on_click=change_name, args=['John Doe'])

st.header(st.session_state['name'])
```

#### Logic nested in a button with a rerun

Although callbacks are often preferred to avoid extra reruns, our first 'John Doe'/'Jane Doe' example can be modified by adding [`st.rerun`](/develop/api-reference/execution-flow/st.rerun) instead. If you need to acces data in `st.session_state` before the button that modifies it, you can include `st.rerun` to rerun the script after the change has been committed. This means the script will rerun twice when a button is clicked.

```python
import streamlit as st
import pandas as pd

if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'
    st.rerun()

if st.button('John'):
    st.session_state['name'] = 'John Doe'
    st.rerun()

st.header(st.session_state['name'])
```

### Buttons to modify or reset other widgets

When a button is used to modify or reset another widget, it is the same as the above examples to modify `st.session_state`. However, an extra consideration exists: you cannot modify a key-value pair in `st.session_state` if the widget with that key has already been rendered on the page for the current script run.

<Important>

Don't do this!

```python
import streamlit as st

st.text_input('Name', key='name')

# These buttons will error because their nested code changes
# a widget's state after that widget within the script.
if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')
```

</Important>

#### Option 1: Use a key for the button and put the logic before the widget

If you assign a key to a button, you can condition code on a button's state by using its value in `st.session_state`. This means that logic depending on your button can be in your script before that button. In the following example, we use the `.get()` method on `st.session_state` because the keys for the buttons will not exist when the script runs for the first time. The `.get()` method will return `False` if it can't find the key. Otherwise, it will return the value of the key.

```python
import streamlit as st

# Use the get method since the keys won't be in session_state
# on the first script run
if st.session_state.get('clear'):
    st.session_state['name'] = ''
if st.session_state.get('streamlit'):
    st.session_state['name'] = 'Streamlit'

st.text_input('Name', key='name')

st.button('Clear name', key='clear')
st.button('Streamlit!', key='streamlit')
```

#### Option 2: Use a callback

```python
import streamlit as st

st.text_input('Name', key='name')

def set_name(name):
    st.session_state.name = name

st.button('Clear name', on_click=set_name, args=[''])
st.button('Streamlit!', on_click=set_name, args=['Streamlit'])
```

#### Option 3: Use containers

By using [`st.container`](/develop/api-reference/layout/st.container) you can have widgets appear in different orders in your script and frontend view (webpage).

```python
import streamlit as st

begin = st.container()

if st.button('Clear name'):
    st.session_state.name = ''
if st.button('Streamlit!'):
    st.session_state.name = ('Streamlit')

# The widget is second in logic, but first in display
begin.text_input('Name', key='name')
```

### Buttons to add other widgets dynamically

When dynamically adding widgets to the page, make sure to use an index to keep the keys unique and avoid a `DuplicateWidgetID` error. In this example, we define a function `display_input_row` which renders a row of widgets. That function accepts an `index` as a parameter. The widgets rendered by `display_input_row` use `index` within their keys so that `dispaly_input_row` can be executed multiple times on a single script rerun without repeating any widget keys.

```python
import streamlit as st

def display_input_row(index):
    left, middle, right = st.columns(3)
    left.text_input('First', key=f'first_{index}')
    middle.text_input('Middle', key=f'middle_{index}')
    right.text_input('Last', key=f'last_{index}')

if 'rows' not in st.session_state:
    st.session_state['rows'] = 0

def increase_rows():
    st.session_state['rows'] += 1

st.button('Add person', on_click=increase_rows)

for i in range(st.session_state['rows']):
    display_input_row(i)

# Show the results
st.subheader('People')
for i in range(st.session_state['rows']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'first_{i}'],
        st.session_state[f'middle_{i}'],
        st.session_state[f'last_{i}']
    )
```

### Buttons to handle expensive or file-writing processes

When you have expensive processes, set them to run upon clicking a button and save the results into `st.session_state`. This allows you to keep accessing the results of the process without re-executing it unnecessarily. This is especially helpful for processes that save to disk or write to a database. In this example, we have an `expensive_process` that depends on two parameters: `option` and `add`. Functionally, `add` changes the output, but `option` does not&mdash;`option` is there to provide a parameter

```python
import streamlit as st
import pandas as pd
import time

def expensive_process(option, add):
    with st.spinner('Processing...'):
        time.sleep(5)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C':[7, 8, 9]}) + add
    return (df, add)

cols = st.columns(2)
option = cols[0].selectbox('Select a number', options=['1', '2', '3'])
add = cols[1].number_input('Add a number', min_value=0, max_value=10)

if 'processed' not in st.session_state:
    st.session_state.processed = {}

# Process and save results
if st.button('Process'):
    result = expensive_process(option, add)
    st.session_state.processed[option] = result

if option in st.session_state.processed:
    st.write(f'Option {option} processed with add {add}')
    st.write(st.session_state.processed[option][0])
```

Astute observers may think, "This feels a little like caching." We are only saving results relative to one parameter, but the pattern could easily be expanded to save results relative to both parameters. In that sense, yes, it has some similarities to caching, but also some important differences. When you save results in `st.session_state`, the results are only available to the current user in their current session. If you use [`st.cache_data`](/develop/api-reference/caching-and-state/st.cache_data) instead, the results are available to all users across all sessions. Furthermore, if you want to update a saved result, you have to clear all saved results for that function to do so.

## Anti-patterns

Here are some simplified examples of how buttons can go wrong. Be on the lookout for these common mistakes.

### Buttons nested inside buttons

```python
import streamlit as st

if st.button('Button 1'):
    st.write('Button 1 was clicked')
    if st.button('Button 2'):
        # This will never be executed.
        st.write('Button 2 was clicked')
```

### Other widgets nested inside buttons

```python
import streamlit as st

if st.button('Sign up'):
    name = st.text_input('Name')

    if name:
        # This will never be executed.
        st.success(f'Welcome {name}')
```

### Nesting a process inside a button without saving to session state

```python
import streamlit as st
import pandas as pd

file = st.file_uploader("Upload a file", type="csv")

if st.button('Get data'):
    df = pd.read_csv(file)
    # This display will go away with the user's next action.
    st.write(df)

if st.button('Save'):
    # This will always error.
    df.to_csv('data.csv')
```

```

File: concepts/app-design/timezone-handling.md
```

---

title: Working with timezones
slug: /develop/concepts/design/timezone-handling

---

# Working with timezones

In general, working with timezones can be tricky. Your Streamlit app users are not necessarily in the same timezone as the server running your app. It is especially true of public apps, where anyone in the world (in any timezone) can access your app. As such, it is crucial to understand how Streamlit handles timezones, so you can avoid unexpected behavior when displaying `datetime` information.

## How Streamlit handles timezones

Streamlit always shows `datetime` information on the frontend with the same information as its corresponding `datetime` instance in the backend. I.e., date or time information does not automatically adjust to the users' timezone. We distinguish between the following two cases:

### **`datetime` instance without a timezone (naive)**

When you provide a `datetime` instance _without specifying a timezone_, the frontend shows the `datetime` instance without timezone information. For example (this also applies to other widgets like [`st.dataframe`](/develop/api-reference/data/st.dataframe)):

```python
import streamlit as st
from datetime import datetime

st.write(datetime(2020, 1, 10, 10, 30))
# Outputs: 2020-01-10 10:30:00
```

Users of the above app always see the output as `2020-01-10 10:30:00`.

### **`datetime` instance with a timezone**

When you provide a `datetime` instance _and specify a timezone_, the frontend shows the `datetime` instance in that same timezone. For example (this also applies to other widgets like [`st.dataframe`](/develop/api-reference/data/st.dataframe)):

```python
import streamlit as st
from datetime import datetime
import pytz

st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# Outputs: 2020-01-10 10:30:00-05:00
```

Users of the above app always see the output as `2020-01-10 10:30:00-05:00`.

In both cases, neither the date nor time information automatically adjusts to the users' timezone on the frontend. What users see is identical to the corresponding `datetime` instance in the backend. It is currently not possible to automatically adjust the date or time information to the timezone of the users viewing the app.

<Note>

The legacy version of the `st.dataframe` has issues with timezones. We do not plan to roll out additional fixes or enhancements for the legacy dataframe. If you need stable timezone support, please consider switching to the arrow serialization by changing the [config setting](/develop/concepts/configuration), _config.dataFrameSerialization = "arrow"_.

</Note>

```

File: concepts/app-design/_index.md
```

---

title: App design concepts and considerations
slug: /develop/concepts/design

---

# App design concepts and considerations

<TileContainer layout="list">

<RefCard href="/develop/concepts/design/animate">

<h5>Animate and update elements</h5>

Understand how to create dynamic, animated content or update elements without rerunning your app.

</RefCard>

<RefCard href="/develop/concepts/design/buttons">

<h5>Button behavior and examples</h5>

Understand how buttons work with explanations and examples to avoid common mistakes.

</RefCard>

<RefCard href="/develop/concepts/design/dataframes">

<h5>Dataframes</h5>

Dataframes are a great way to display and edit data in a tabular format. Understand the UI and options available in Streamlit.

</RefCard>

<RefCard href="/develop/concepts/design/custom-classes">

<h5>Using custom Python classes in your Streamlit app</h5>

Understand the impact of defining your own Python classes within Streamlit's rerun model.

</RefCard>

<RefCard href="/develop/concepts/design/timezone-handling">

<h5>Working with timezones</h5>

Understand how to localize time to your users.

</RefCard>

</TileContainer>

```

File: concepts/app-design/dataframes.md
```

---

title: Dataframes
slug: /develop/concepts/design/dataframes

---

# Dataframes

Dataframes are a great way to display and edit data in a tabular format. Working with Pandas DataFrames and other tabular data structures is key to data science workflows. If developers and data scientists want to display this data in Streamlit, they have multiple options: `st.dataframe` and `st.data_editor`. If you want to solely display data in a table-like UI, [st.dataframe](/develop/api-reference/data/st.dataframe) is the way to go. If you want to interactively edit data, use [st.data_editor](/develop/api-reference/data/st.data_editor). We explore the use cases and advantages of each option in the following sections.

## Display dataframes with st.dataframe

Streamlit can display dataframes in a table-like UI via `st.dataframe` :

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
```

<Cloud src="https://doc-dataframe-basic.streamlit.app/?embed=true" height="300px"/>

## `st.dataframe` UI features

`st.dataframe` provides additional functionality by using [glide-data-grid](https://github.com/glideapps/glide-data-grid) under the hood:

- **Column sorting**: Sort columns by clicking on their headers.
- **Column resizing**: Resize columns by dragging and dropping column header borders.
- **Table resizing**: Resize tables by dragging and dropping the bottom right corner.
- **Fullscreen view**: Enlarge tables to fullscreen by clicking the fullscreen icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>fullscreen</i>) in the toolbar.
- **Search**: Click the search icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>search</i>) in the toolbar or use hotkeys (`Γîÿ+F`┬áor┬á`Ctrl+F`) to search through the data.
- **Download**: Click the download icon in the toolbar to download the data as a CSV file.
- **Copy to clipboard**: Select one or multiple cells, copy them to the clipboard (`Γîÿ+C`┬áor┬á`Ctrl+C`), and paste them into your favorite spreadsheet software.

<YouTube videoId="nauAnULRG1c" loop autoplay />

Try out all the UI features using the embedded app from the prior section.

In addition to Pandas DataFrames, `st.dataframe` also supports other common Python types, e.g., list, dict, or numpy array. It also supports [Snowpark](https://docs.snowflake.com/en/developer-guide/snowpark/index) and [PySpark](https://spark.apache.org/docs/latest/api/python/) DataFrames, which allow you to lazily evaluate and pull data from databases. This can be useful for working with large datasets.

## Edit data with st.data_editor

Streamlit supports editable dataframes via the `st.data_editor` command. Check out its API in [st.data_editor](/develop/api-reference/data/st.data_editor). It shows the dataframe in a table, similar to `st.dataframe`. But in contrast to `st.dataframe`, this table isn't static! The user can click on cells and edit them. The edited data is then returned on the Python side. Here's an example:

```python
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

df = load_data()
edited_df = st.data_editor(df) # ≡ƒæê An editable dataframe

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** ≡ƒÄê")
```

<Cloud src="https://doc-data-editor.streamlit.app/?embed=true" height="300px"/>

Try it out by double-clicking on any cell. You'll notice you can edit all cell values. Try editing the values in the rating column and observe how the text output at the bottom changes:

## `st.data_editor` UI features

`st.data_editor` also supports a few additional things:

- [**Add and delete rows**](#add-and-delete-rows): You can do this by setting `num_rows= "dynamic"` when calling `st.data_editor`. This will allow users to add and delete rows as needed.
- [**Copy and paste support**](#copy-and-paste-support): Copy and paste both between `st.data_editor` and spreadsheet software like Google Sheets and Excel.
- [**Access edited data**](#access-edited-data): Access only the individual edits instead of the entire edited data structure via Session State.
- [**Bulk edits**](#bulk-edits): Similar to Excel, just drag a handle to edit neighboring cells.
- [**Automatic input validation**](#automatic-input-validation): Column Configuration provides strong data type support and other configurable options. For example, there's no way to enter letters into a number cell. Number cells can have a designated min and max.
- [**Edit common data structures**](#edit-common-data-structures): `st.data_editor` supports lists, dicts, NumPy ndarray, and more!

<YouTube videoId="6tah69LkfxE" loop autoplay />

### Add and delete rows

With `st.data_editor`, viewers can add or delete rows via the table UI. This mode can be activated by setting the┬á`num_rows` parameter to┬á`"dynamic"`:

```python
edited_df = st.data_editor(df, num_rows="dynamic")
```

- To add new rows, click the plus icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>add</i>) in the toolbar. Alternatively, click inside a shaded cell below the bottom row of the table.
- To delete rows, select one or more rows using the checkboxes on the left. Click the delete icon (<i style={{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}>delete</i>) or press the `delete` key on your keyboard.

<Cloud src="https://doc-data-editor-clipboard.streamlit.app/?embed=true" height="400px"/>

### Copy and paste support

The data editor supports pasting in tabular data from Google Sheets, Excel, Notion, and many other similar tools. You can also copy-paste data between┬á`st.data_editor` instances. This functionality, powered by the [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API), can be a huge time saver for users who need to work with data across multiple platforms. To try it out:

1. Copy data from┬á[this Google Sheets document](https://docs.google.com/spreadsheets/d/1Z0zd-5dF_HfqUaDDq4BWAOnsdlGCjkbTNwDZMBQ1dOY/edit?usp=sharing)┬áto your clipboard.
2. Single click any cell in the┬á`name`┬ácolumn in the app above. Paste it in using hotkeys (`Γîÿ+V`┬áor┬á`Ctrl+V`).

<Note>

Every cell of the pasted data will be evaluated individually and inserted into the cells if the data is compatible with the column type. For example, pasting in non-numerical text data into a number column will be ignored.

</Note>

<Tip>

If you embed your apps with iframes, you'll need to allow the iframe to access the clipboard if you want to use the copy-paste functionality. To do so, give the iframe [`clipboard-write`](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/write) and [`clipboard-read`](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard/read) permissions. E.g.

```javascript
<iframe allow="clipboard-write;clipboard-read;" ... src="https://your-app-url"></iframe>
```

As developers, ensure the app is served with a valid, trusted certificate when using TLS. If users encounter issues with copying and pasting data, direct them to check if their browser has activated clipboard access permissions for the Streamlit application, either when prompted or through the browser's site settings.

</Tip>

### Access edited data

Sometimes, it is more convenient to know which cells have been changed rather than getting the entire edited dataframe back. Streamlit makes this easy through the use of [Session State](/develop/concepts/architecture/session-state). If a `key` parameter is set, Streamlit will store any changes made to the dataframe in Session State.

This snippet shows how you can access changed data using Session State:

```python
st.data_editor(df, key="my_key", num_rows="dynamic") # ≡ƒæê Set a key
st.write("Here's the value in Session State:")
st.write(st.session_state["my_key"]) # ≡ƒæê Show the value in Session State
```

In this code snippet, the `key` parameter is set to `"my_key"`. After the data editor is created, the value associated to `"my_key"` in Session State is displayed in the app using `st.write`. This shows the additions, edits, and deletions that were made.

This can be useful when working with large dataframes and you only need to know which cells have changed, rather than access the entire edited dataframe.

<Cloud src="https://doc-data-editor-changed.streamlit.app/?embed=true" height="700px"/>

Use all we've learned so far and apply them to the above embedded app. Try editing cells, adding new rows, and deleting rows.

Notice how edits to the table are reflected in Session State. When you make any edits, a rerun is triggered which sends the edits to the backend. The widget's state is a JSON object containing three properties: **edited_rows**, **added_rows**, and **deleted rows:**.

<Warning>

When going from `st.experimental_data_editor` to `st.data_editor` in 1.23.0, the data editor's representation in `st.session_state` was changed. The `edited_cells` dictionary is now called `edited_rows` and uses a different format (`{0: {"column name": "edited value"}}` instead of `{"0:1": "edited value"}`). You may need to adjust your code if your app uses `st.experimental_data_editor` in combination with `st.session_state`."

</Warning>

- `edited_rows` is a dictionary containing all edits. Keys are zero-based row indices and values are dictionaries that map column names to edits (e.g. `{0: {"col1": ..., "col2": ...}}`).
- `added_rows` is a list of newly added rows. Each value is a dictionary with the same format as above (e.g. `[{"col1": ..., "col2": ...}]`).
- `deleted_rows` is a list of row numbers that have been deleted from the table (e.g. `[0, 2]`).

`st.data_editor` does not support reordering rows, so added rows will always be appended to the end of the dataframe with any edits and deletions applicable to the original rows.

### Bulk edits

The data editor includes a feature that allows for bulk editing of cells. Similar to Excel, you can drag a handle across a selection of cells to edit their values in bulk. You can even apply commonly used [keyboard shortcuts](https://github.com/glideapps/glide-data-grid/blob/main/packages/core/API.md#keybindings) in spreadsheet software. This is useful when you need to make the same change across multiple cells, rather than editing each cell individually.

### Edit common data structures

Editing doesn't just work for Pandas DataFrames! You can also edit lists, tuples, sets, dictionaries, NumPy arrays, or Snowpark & PySpark DataFrames. Most data types will be returned in their original format. But some types (e.g. Snowpark and PySpark) are converted to Pandas DataFrames. To learn about all the supported types, read the [st.data_editor](/develop/api-reference/data/st.data_editor) API.

For example, you can easily let the user add items to a list:

```python
edited_list = st.data_editor(["red", "green", "blue"], num_rows= "dynamic")
st.write("Here are all the colors you entered:")
st.write(edited_list)
```

Or numpy arrays:

```python
import numpy as np

st.data_editor(np.array([
	["st.text_area", "widget", 4.92],
	["st.markdown", "element", 47.22]
]))
```

Or lists of records:

```python
st.data_editor([
    {"name": "st.text_area", "type": "widget"},
    {"name": "st.markdown", "type": "element"},
])
```

Or dictionaries and many more types!

```python
st.data_editor({
	"st.text_area": "widget",
	"st.markdown": "element"
})
```

### Automatic input validation

The data editor includes automatic input validation to help prevent errors when editing cells. For example, if you have a column that contains numerical data, the input field will automatically restrict the user to only entering numerical data. This helps to prevent errors that could occur if the user were to accidentally enter a non-numerical value. Additional input validation can be configured through the [Column configuration API](/develop/api-reference/data/st.column_config). Keep reading below for an overview of column configuration, including validation options.

## Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

Column configuration includes the following column types: Text, Number, Checkbox, Selectbox, Date, Time, Datetime, List, Link, Image, Line chart, Bar chart, and Progress. There is also a generic Column option. See the embedded app below to view these different column types. Each column type is individually previewed in the [Column configuration API](/develop/api-reference/data/st.column_config) documentation.

<Cloud src="https://doc-column-config-overview.streamlit.app/?embed=true&embed_options=disable_scrolling" height="480"/>

### Format values

A `format` parameter is available in column configuration for [Text](/develop/api-reference/data/st.column_config/st.column_config.textcolumn), [Date](/develop/api-reference/data/st.column_config/st.column_config.datecolumn), [Time](/develop/api-reference/data/st.column_config/st.column_config.timecolumn), and [Datetime](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn) columns. Chart-like columns can also be formatted. [Line chart](/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn) and [Bar chart](/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn) columns have a `y_min` and `y_max` parameters to set the vertical bounds. For a [Progress column](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn), you can declare the horizontal bounds with `min_value` and `max_value`.

### Validate input

When specifying a column configuration, you can declare not only the data type of the column but also value restrictions. All column configuration elements allow you to make a column required with the keyword parameter `required=True`.

For Text and Link columns, you can specify the maximum number of characters with `max_chars` or use regular expressions to validate entries through `validate`. Numerical columns, including Number, Date, Time, and Datetime have `min_value` and `max_value` parameters. Selectbox columns have a configurable list of `options`.

The data type for Number columns is `float` by default. Passing a value of type `int` to any of `min_value`, `max_value`, `step`, or `default` will set the type for the column as `int`.

### Configure an empty dataframe

You can use `st.data_editor` to collect tabular input from a user. When starting from an empty dataframe, default column types are text. Use column configuration to specify the data types you want to collect from users.

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(columns=['name','age','color'])
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
config = {
    'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
    'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
    'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
}

result = st.data_editor(df, column_config = config, num_rows='dynamic')

if st.button('Get results'):
    st.write(result)
```

<Cloud src="https://doc-column-config-empty.streamlit.app/?embed=true" height="300"/>

## Additional formatting options

In addition to column configuration, `st.dataframe` and `st.data_editor` have a few more parameters to customize the display of your dataframe.

- `hide_index` : Set to `True` to hide the dataframe's index.
- `column_order` : Pass a list of column labels to specify the order of display.
- `disabled` : Pass a list of column labels to disable them from editing. This let's you avoid disabling them individually.

## Handling large datasets

`st.dataframe` and `st.data_editor` have been designed to theoretically handle tables with millions of rows thanks to their highly performant implementation using the glide-data-grid library and HTML canvas. However, the maximum amount of data that an app can realistically handle will depend on several other factors, including:

1. The maximum size of WebSocket messages: Streamlit's WebSocket messages are configurable via the `server.maxMessageSize` [config option](https://docs.streamlit.io/develop/concepts/configuration#view-all-configuration-options), which limits the amount of data that can be transferred via the WebSocket connection at once.
2. The server memory: The amount of data that your app can handle will also depend on the amount of memory available on your server. If the server's memory is exceeded, the app may become slow or unresponsive.
3. The user's browser memory: Since all the data needs to be transferred to the user's browser for rendering, the amount of memory available on the user's device can also affect the app's performance. If the browser's memory is exceeded, it may crash or become unresponsive.

In addition to these factors, a slow network connection can also significantly slow down apps that handle large datasets.

When handling large datasets with more than 150,000 rows, Streamlit applies additional optimizations and disables column sorting. This can help to reduce the amount of data that needs to be processed at once and improve the app's performance.

## Limitations

- Streamlit casts all column names to strings internally, so `st.data_editor` will return a DataFrame where all column names are strings.
- The dataframe toolbar is not currently configurable.
- While Streamlit's data editing capabilities offer a lot of functionality, editing is enabled for a limited set of column types ([TextColumn](/develop/api-reference/data/st.column_config/st.column_config.textcolumn), [NumberColumn](/develop/api-reference/data/st.column_config/st.column_config.numbercolumn), [LinkColumn](/develop/api-reference/data/st.column_config/st.column_config.linkcolumn), [CheckboxColumn](/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn), [SelectboxColumn](/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn), [DateColumn](/develop/api-reference/data/st.column_config/st.column_config.datecolumn), [TimeColumn](/develop/api-reference/data/st.column_config/st.column_config.timecolumn), and [DatetimeColumn](/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn)). We are actively working on supporting editing for other column types as well, such as images, lists, and charts.
- Almost all editable datatypes are supported for index editing. However, `pandas.CategoricalIndex` and `pandas.MultiIndex` are not supported for editing.
- Sorting is not supported for `st.data_editor` when `num_rows="dynamic"`.
- Sorting is deactivated to optimize performance on large datasets with more than 150,000 rows.

We are continually working to improve Streamlit's handling of DataFrame and add functionality to data editing, so keep an eye out for updates.

```

File: concepts/configuration/options.md
```

---

title: Working with configuration options
slug: /develop/concepts/configuration/options

---

# Working with configuration options

Streamlit provides four different ways to set configuration options. This list is in reverse order of precedence, i.e. command line flags take precedence over environment variables when the same configuration option is provided multiple times.

<Note>

If you change theme settings in `.streamlit/config.toml` _while_ the app is running, these changes will reflect immediately. If you change non-theme settings in `.streamlit/config.toml` _while_ the app is running, the server needs to be restarted for changes to be reflected in the app.

</Note>

1. In a **global config file** at `~/.streamlit/config.toml` for macOS/Linux or `%userprofile%/.streamlit/config.toml` for Windows:

   ```toml
   [server]
   port = 80
   ```

2. In a **per-project config file** at `$CWD/.streamlit/config.toml`, where
   `$CWD` is the folder you're running Streamlit from.

3. Through `STREAMLIT_*` **environment variables**, such as:

   ```bash
   export STREAMLIT_SERVER_PORT=80
   export STREAMLIT_SERVER_COOKIE_SECRET=dontforgottochangeme
   ```

4. As **flags on the command line** when running `streamlit run`:

   ```bash
   streamlit run your_script.py --server.port 80
   ```

## Telemetry

As mentioned during the installation process, Streamlit collects usage statistics. You can find out
more by reading our [Privacy Notice](https://streamlit.io/privacy-policy), but the high-level
summary is that although we collect telemetry data we cannot see and do not store information
contained in Streamlit apps.

If you'd like to opt out of usage statistics, add the following to your config file:

```toml
[browser]
gatherUsageStats = false
```

## Theming

You can change the base colors of your app using the `[theme]` section of the configuration system.
To learn more, see [Theming.](/develop/concepts/configuration/theming)

## View all configuration options

As described in [Command-line options](/develop/api-reference/cli), you can
view all available configuration options using:

```bash
streamlit config show
```

```

File: concepts/configuration/theming.md
```

---

title: Theming
slug: /develop/concepts/configuration/theming

---

# Theming

In this guide, we provide examples of how Streamlit page elements are affected
by the various theme config options. For a more high-level overview of
Streamlit themes, see the Themes section of the
[main concepts documentation](/get-started/fundamentals/additional-features#themes).

Streamlit themes are defined using regular config options: a theme can be set
via command line flag when starting your app using `streamlit run` or by
defining it in the `[theme]` section of a `.streamlit/config.toml` file. For
more information on setting config options, please refer to the
[Streamlit configuration documentation](/develop/concepts/configuration).

The following config options show the default Streamlit Light theme recreated
in the `[theme]` section of a `.streamlit/config.toml` file.

```toml
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
```

Let's go through each of these options, providing screenshots to demonstrate
what parts of a Streamlit app they affect where needed.

## primaryColor

`primaryColor` defines the accent color most often used throughout a Streamlit
app. A few examples of Streamlit widgets that use `primaryColor` include
`st.checkbox`, `st.slider`, and `st.text_input` (when focused).

![Primary Color](/images/theme_config_options/primaryColor.png)

<Tip>

Any CSS color can be used as the value for primaryColor and the other color
options below. This means that theme colors can be specified in hex or with
browser-supported color names like "green", "yellow", and
"chartreuse". They can even be defined in the RGB and HSL formats!

</Tip>

## backgroundColor

Defines the background color used in the main content area of your app.

## secondaryBackgroundColor

This color is used where a second background color is needed for added
contrast. Most notably, it is the sidebar's background color. It is also used
as the background color for most interactive widgets.

![Secondary Background Color](/images/theme_config_options/secondaryBackgroundColor.png)

## textColor

This option controls the text color for most of your Streamlit app.

## font

Selects the font used in your Streamlit app. Valid values are `"sans serif"`,
`"serif"`, and `"monospace"`. This option defaults to `"sans serif"` if unset
or invalid.

Note that code blocks are always rendered using the monospace font regardless of
the font selected here.

## base

An easy way to define custom themes that make small changes to one of the
preset Streamlit themes is to use the `base` option. Using `base`, the
Streamlit Light theme can be recreated as a custom theme by writing the
following:

```toml
[theme]
base="light"
```

The `base` option allows you to specify a preset Streamlit theme that your
custom theme inherits from. Any theme config options not defined in your theme
settings have their values set to those of the base theme. Valid values for
`base` are `"light"` and `"dark"`.

For example, the following theme config defines a custom theme nearly identical
to the Streamlit Dark theme, but with a new `primaryColor`.

```toml
[theme]
base="dark"
primaryColor="purple"
```

If `base` itself is omitted, it defaults to `"light"`, so you can define a
custom theme that changes the font of the Streamlit Light theme to serif with
the following config

```toml
[theme]
font="serif"
```

```

File: concepts/configuration/static-file-serving.md
```

---

title: Static file serving
slug: /develop/concepts/configuration/serving-static-files

---

# Static file serving

Streamlit apps can host and serve small, static media files to support media embedding use cases that
won't work with the normal [media elements](/develop/api-reference/media).

To enable this feature, set `enableStaticServing = true` under `[server]` in your config file,
or environment variable `STREAMLIT_SERVER_ENABLE_STATIC_SERVING=true`.

Media stored in the folder `./static/` relative to the running app file is served at path
`app/static/[filename]`, such as `http://localhost:8501/app/static/cat.png`.

## Details on usage

- Files with the following extensions will be served normally: `".jpg", ".jpeg", ".png", ".gif"`. Any other
  file will be sent with header `Content-Type:text/plain` which will cause browsers to render in plain text.
  This is included for security - other file types that need to render should be hosted outside the app.
- Streamlit also sets `X-Content-Type-Options:nosniff` for all files rendered from the static directory.
- For apps running on Streamlit Community Cloud:
  - Files available in the Github repo will always be served. Any files generated while the app is running,
    such as based on user interaction (file upload, etc), are not guaranteed to persist across user sessions.
  - Apps which store and serve many files, or large files, may run into resource limits and be shut down.

## Example usage

- Put an image `cat.png` in the folder `./static/`
- Add `enableStaticServing = true` under `[server]` in your `.streamlit/config.toml`
- Any media in the `./static/` folder is served at the relative URL like `app/static/cat.png`

```toml
# .streamlit/config.toml

[server]
enableStaticServing = true
```

```python
# app.py
import streamlit as st

with st.echo():
    st.title("CAT")

    st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")

```

Additional resources:

- [https://docs.streamlit.io/develop/concepts/configuration](https://docs.streamlit.io/develop/concepts/configuration)
- [https://static-file-serving.streamlit.app/](https://static-file-serving.streamlit.app/)

<Cloud src="https://static-file-serving.streamlit.app/?embedded=true" height="1000" />

```

File: concepts/configuration/https.md
```

---

title: HTTPS support
slug: /develop/concepts/configuration/https-support

---

# HTTPS support

Many apps need to be accessed with SSL / [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) protocol or `https://`.

We recommend performing SSL termination in a reverse proxy or load balancer for self-hosted and production use cases, not directly in the app. [Streamlit Community Cloud](/deploy/streamlit-community-cloud) uses this approach, and every major cloud and app hosting platform should allow you to configure it and provide extensive documentation. You can find some of these platforms in our [Deployment tutorials](/deploy/tutorials).

To terminate SSL in your Streamlit app, you must configure `server.sslCertFile` and `server.sslKeyFile`. Learn how to set config options in [Configuration](/develop/concepts/configuration).

## Details on usage

- The configuration value should be a local file path to a cert file and key file. These must be available at the time the app starts.
- Both `server.sslCertFile` and `server.sslKeyFile` must be specified. If only one is specified, your app will exit with an error.
- This feature will not work in Community Cloud. Community Cloud already serves your app with TLS.

<Warning>

In a production environment, we recommend performing SSL termination by the load balancer or the reverse proxy, not using this option. The use of this option in Streamlit has not gone through extensive security audits or performance tests.

</Warning>

## Example usage

```toml
# .streamlit/config.toml

[server]
sslCertFile = '/path/to/certchain.pem'
sslKeyFile = '/path/to/private.key'
```

```

File: concepts/configuration/_index.md
```

---

title: Configure and customize your app
slug: /develop/concepts/configuration

---

# Configure and customize your app

<TileContainer layout="list">

<RefCard href="/develop/concepts/configuration/options">

<h5>Configuration options</h5>

Understand they types of options available to you through Streamlit configuration.

</RefCard>

<RefCard href="/develop/concepts/configuration/https-support">

<h5>HTTPS support</h5>

Understand how to configure SSL and TLS for your Streamlit app.

</RefCard>

<RefCard href="/develop/concepts/configuration/serving-static-files">

<h5>Static file serving</h5>

Understand how to host files alongside your app to make them accessible by URL. Use this if you want to point to files with raw HTML.

</RefCard>

<RefCard href="/develop/concepts/configuration/theming">

<h5>Theming</h5>

Understand how to use the theming configuration options to customize the color and appearance of your app.

</RefCard>

</TileContainer>

```

File: concepts/custom-components/limitations.md
```

---

title: Limitations of custom components
slug: /develop/concepts/custom-components/limitations

---

# Limitations of custom components

## How do Streamlit Components differ from functionality provided in the base Streamlit package?

- Streamlit Components are wrapped up in an iframe, which gives you the ability to do whatever you want (within the iframe) using any web technology you like.

## What types of things aren't possible with Streamlit Components?

Because each Streamlit Component gets mounted into its own sandboxed iframe, this implies a few limitations on what is possible with Components:

- **Can't communicate with other Components**: Components canΓÇÖt contain (or otherwise communicate with) other components, so Components cannot be used to build something like a grid layout.
- **Can't modify CSS**: A Component canΓÇÖt modify the CSS that the rest of the Streamlit app uses, so you can't create something to put the app in dark mode, for example.
- **Can't add/remove elements**: A Component canΓÇÖt add or remove other elements of a Streamlit app, so you couldn't make something to remove the app menu, for example.

## My Component seems to be blinking/stuttering...how do I fix that?

Currently, no automatic debouncing of Component updates is performed within Streamlit. The Component creator themselves can decide to rate-limit the updates they send back to Streamlit.

```

File: concepts/custom-components/_index.md
```

---

title: Components
slug: /develop/concepts/custom-components

---

# Custom Components

Components are third-party Python modules that extend what's possible with Streamlit.

## How to use a Component

Components are super easy to use:

1. Start by finding the Component you'd like to use. Two great resources for this are:

   - The [Component gallery](https://streamlit.io/components)
   - [This thread](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634),
     by Fanilo A. from our forums.

2. Install the Component using your favorite Python package manager. This step and all following
   steps are described in your component's instructions.

   For example, to use the fantastic [AgGrid
   Component](https://github.com/PablocFonseca/streamlit-aggrid), you first install it with:

   ```python
   pip install streamlit-aggrid
   ```

3. In your Python code, import the Component as described in its instructions. For AgGrid, this step
   is:

   ```python
   from st_aggrid import AgGrid
   ```

4. ...now you're ready to use it! For AgGrid, that's:

   ```python
   AgGrid(my_dataframe)
   ```

## Making your own Component

If you're interested in making your own component, check out the following resources:

- [Create a Component](/develop/concepts/custom-components/create)
- [Publish a Component](/develop/concepts/custom-components/publish)
- [Components API](/develop/concepts/custom-components/intro)
- [Blog post for when we launched Components!](https://blog.streamlit.io/introducing-streamlit-components/)

Alternatively, if you prefer to learn using videos, our engineer Tim Conkling has put together some
amazing tutorials:

##### Video tutorial, part 1

<YouTube videoId="BuD3gILJW-Q" />

##### Video tutorial, part 2

<YouTube videoId="QjccJl_7Jco" />

```

File: concepts/custom-components/create-component.md
```

---

title: Create a Component
slug: /develop/concepts/custom-components/create

---

# Create a Component

<Note>

If you are only interested in **using Streamlit Components**, then you can skip this section and
head over to the [Streamlit Components Gallery](https://streamlit.io/components) to find and install
components created by the community!

</Note>

Developers can write JavaScript and HTML "components" that can be rendered in Streamlit apps. Streamlit Components can receive data from, and also send data to, Streamlit Python scripts.

Streamlit Components let you expand the functionality provided in the base Streamlit package. Use Streamlit Components to create the needed functionality for your use-case, then wrap it up in a Python package and share with the broader Streamlit community!

**Types of Streamlit Components you could create include:**

- Custom versions of existing Streamlit elements and widgets, such as `st.slider` or `st.file_uploader`.
- Completely new Streamlit elements and widgets by wrapping existing React.js, Vue.js, or other JavaScript widget toolkits.
- Rendering Python objects having methods that output HTML, such as IPython [`__repr_html__`](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display).
- Convenience functions for commonly-used web features like [GitHub gists and Pastebin](https://github.com/randyzwitch/streamlit-embedcode).

Check out these Streamlit Components tutorial videos by Streamlit engineer Tim Conkling to get started:

## Part 1: Setup and Architecture

<YouTube videoId="BuD3gILJW-Q" />

## Part 2: Make a Slider Widget

<YouTube videoId="QjccJl_7Jco" />

```

File: concepts/custom-components/publish-component.md
```

---

title: Publish a Component
slug: /develop/concepts/custom-components/publish

---

# Publish a Component

## Publish to PyPI

Publishing your Streamlit Component to [PyPI](https://pypi.org/) makes it easily accessible to Python users around the world. This step is completely optional, so if you wonΓÇÖt be releasing your component publicly, you can skip this section!

<Note>

For [static Streamlit Components](/develop/concepts/custom-components/intro#create-a-static-component), publishing a Python package to PyPI follows the same steps as the
[core PyPI packaging instructions](https://packaging.python.org/tutorials/packaging-projects/). A static Component likely contains only Python code, so once you have your
[setup.py](https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py) file correct and
[generate your distribution files](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives), you're ready to
[upload to PyPI](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives).

[Bi-directional Streamlit Components](/develop/concepts/custom-components/intro#create-a-bi-directional-component) at minimum include both Python and JavaScript code, and as such, need a bit more preparation before they can be published on PyPI. The remainder of this page focuses on the bi-directional Component preparation process.

</Note>

### Prepare your Component

A bi-directional Streamlit Component varies slightly from a pure Python library in that it must contain pre-compiled frontend code. This is how base Streamlit works as well; when you `pip install streamlit`, you are getting a Python library where the HTML and frontend code contained within it have been compiled into static assets.

The [component-template](https://github.com/streamlit/component-template) GitHub repo provides the folder structure necessary for PyPI publishing. But before you can publish, you'll need to do a bit of housekeeping:

1. Give your Component a name, if you haven't already
   - Rename the `template/my_component/` folder to `template/<component name>/`
   - Pass your component's name as the the first argument to `declare_component()`
2. Edit `MANIFEST.in`, change the path for recursive-include from `package/frontend/build *` to `<component name>/frontend/build *`
3. Edit `setup.py`, adding your component's name and other relevant info
4. Create a release build of your frontend code. This will add a new directory, `frontend/build/`, with your compiled frontend in it:

   ```bash
   cd frontend
   npm run export
   ```

5. Pass the build folder's path as the `path` parameter to `declare_component`. (If you're using the template Python file, you can set `_RELEASE = True` at the top of the file):

   ```python
      import streamlit.components.v1 as components

      # Change this:
      # component = components.declare_component("my_component", url="http://localhost:3001")

      # To this:
      parent_dir = os.path.dirname(os.path.abspath(__file__))
      build_dir = os.path.join(parent_dir, "frontend/build")
      component = components.declare_component("new_component_name", path=build_dir)
   ```

### Build a Python wheel

Once you've changed the default `my_component` references, compiled the HTML and JavaScript code and set your new component name in `components.declare_component()`, you're ready to build a Python wheel:

1. Make sure you have the latest versions of setuptools, wheel, and twine

2. Create a wheel from the source code:

   ```bash
    # Run this from your component's top-level directory; that is,
    # the directory that contains `setup.py`
    python setup.py sdist bdist_wheel
   ```

### Upload your wheel to PyPI

With your wheel created, the final step is to upload to PyPI. The instructions here highlight how to upload to [Test PyPI](https://test.pypi.org/), so that you can learn the mechanics of the process without worrying about messing anything up. Uploading to PyPI follows the same basic procedure.

1. Create an account on [Test PyPI](https://test.pypi.org/) if you don't already have one

   - Visit [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) and complete the steps

   - Visit [https://test.pypi.org/manage/account/#api-tokens](https://test.pypi.org/manage/account/#api-tokens) and create a new API token. DonΓÇÖt limit the token scope to a particular project, since you are creating a new project. Copy your token before closing the page, as you wonΓÇÖt be able to retrieve it again.

2. Upload your wheel to Test PyPI. `twine` will prompt you for a username and password. For the username, use **\_\_token\_\_**. For the password, use your token value from the previous step, including the `pypi-` prefix:

   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

3. Install your newly-uploaded package in a new Python project to make sure it works:

   ```bash
    python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE
   ```

If all goes well, you're ready to upload your library to PyPI by following the instructions at [https://packaging.python.org/tutorials/packaging-projects/#next-steps](https://packaging.python.org/tutorials/packaging-projects/#next-steps).

Congratulations, you've created a publicly-available Streamlit Component!

## Promote your Component!

We'd love to help you share your Component with the Streamlit Community! To share it:

1. If you host your code on GitHub, add the tag `streamlit-component`, so that it's listed in the [GitHub **streamlit-component** topic](https://github.com/topics/streamlit-component):

   <Image caption="Add the streamlit-component tag to your GitHub repo" src="/images/component-tag.gif" />

2. Post on the Streamlit Forum in [Show the Community!](https://discuss.streamlit.io/c/streamlit-examples/9). Use a post title similar to "New Component: `<your component name>`, a new way to do X".
3. Add your component to the [Community Component Tracker](https://discuss.streamlit.io/t/streamlit-components-community-tracker/4634).
4. Tweet us at [@streamlit](https://twitter.com/streamlit) so that we can retweet your announcement for you.

Our [Components Gallery](https://streamlit.io/components) is updated approximately every month. Follow the above recommendations to maximize the liklihood of your component landing in our Components Gallery. Community Components featured in our docs are hand-curated on a less-regular basis. Popular components with many stars and good documentation are more likely to be selected.

```

File: concepts/custom-components/components-api.md
```

---

title: Intro to custom components
slug: /develop/concepts/custom-components/intro

---

# Intro to custom components

The first step in developing a Streamlit Component is deciding whether to create a static component (i.e. rendered once, controlled by Python) or to create a bi-directional component that can communicate from Python to JavaScript and back.

## Create a static component

If your goal in creating a Streamlit Component is solely to display HTML code or render a chart from a Python visualization library, Streamlit provides two methods that greatly simplify the process: `components.html()` and `components.iframe()`.

If you are unsure whether you need bi-directional communication, **start here first**!

### Render an HTML string

While [`st.text`](/develop/api-reference/text/st.text), [`st.markdown`](/develop/api-reference/text/st.markdown) and [`st.write`](/develop/api-reference/write-magic/st.write) make it easy to write text to a Streamlit app, sometimes you'd rather implement a custom piece of HTML. Similarly, while Streamlit natively supports [many charting libraries](/develop/api-reference/charts#chart-elements), you may want to implement a specific HTML/JavaScript template for a new charting library. [`components.html`](/develop/api-reference/custom-components/st.components.v1.html) works by giving you the ability to embed an iframe inside of a Streamlit app that contains your desired output.

**Example**

```python
import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)
```

### Render an iframe URL

[`components.iframe`](/develop/api-reference/custom-components/st.components.v1.iframe) is similar in features to `components.html`, with the difference being that `components.iframe` takes a URL as its input. This is used for situations where you want to include an entire page within a Streamlit app.

**Example**

```python
import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe("https://example.com", height=500)
```

## Create a bi-directional component

A bi-directional Streamlit Component has two parts:

1. A **frontend**, which is built out of HTML and any other web tech you like (JavaScript, React, Vue, etc.), and gets rendered in Streamlit apps via an iframe tag.
2. A **Python API**, which Streamlit apps use to instantiate and talk to that frontend

To make the process of creating bi-directional Streamlit Components easier, we've created a React template and a TypeScript-only template in the [Streamlit Component-template GitHub repo](https://github.com/streamlit/component-template). We also provide some [example Components](https://github.com/streamlit/component-template/tree/master/examples) in the same repo.

### Development Environment Setup

To build a Streamlit Component, you need the following installed in your development environment:

- Python 3.8 - Python 3.12
- Streamlit 1.11.1 or higher
- [nodejs](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

Clone the [component-template GitHub repo](https://github.com/streamlit/component-template), then decide whether you want to use the React.js (["template"](https://github.com/streamlit/component-template/tree/master/template)) or plain TypeScript (["template-reactless"](https://github.com/streamlit/component-template/tree/master/template-reactless)) template.

1. Initialize and build the component template frontend from the terminal:

   ```bash
   # React template
   template/my_component/frontend
   npm install    # Initialize the project and install npm dependencies
   npm run start  # Start the Webpack dev server

   # or

   # TypeScript-only template
   template-reactless/my_component/frontend
   npm install    # Initialize the project and install npm dependencies
   npm run start  # Start the Webpack dev server
   ```

2. _From a separate terminal_, run the Streamlit app (Python) that declares and uses the component:

   ```bash
   # React template
   cd template
   . venv/bin/activate # or similar to activate the venv/conda environment where Streamlit is installed
   pip install -e . # install template as editable package
   streamlit run my_component/example.py # run the example

   # or

   # TypeScript-only template
   cd template-reactless
   . venv/bin/activate # or similar to activate the venv/conda environment where Streamlit is installed
   pip install -e . # install template as editable package
   streamlit run my_component/example.py # run the example
   ```

After running the steps above, you should see a Streamlit app in your browser that looks like this:

![Streamlit Component Example App](/images/component_demo_example.png)

The example app from the template shows how bi-directional communication is implemented. The Streamlit Component displays a button (`Python ΓåÆ JavaScript`), and the end-user can click the button. Each time the button is clicked, the JavaScript front-end increments the counter value and passes it back to Python (`JavaScript ΓåÆ Python`), which is then displayed by Streamlit (`Python ΓåÆ JavaScript`).

### Frontend

Because each Streamlit Component is its own webpage that gets rendered into an `iframe`, you can use just about any web tech you'd like to create that web page. We provide two templates to get started with in the Streamlit [Components-template GitHub repo](https://github.com/streamlit/component-template/); one of those templates uses [React](https://reactjs.org/) and the other does not.

<Note>

Even if you're not already familiar with React, you may still want to check out the React-based
template. It handles most of the boilerplate required to send and receive data from Streamlit, and
you can learn the bits of React you need as you go.

If you'd rather not use React, please read this section anyway! It explains the fundamentals of
Streamlit Γåö Component communication.
</Note>

#### React

The React-based template is in `template/my_component/frontend/src/MyComponent.tsx`.

- `MyComponent.render()` is called automatically when the component needs to be re-rendered (just like in any React app)
- Arguments passed from the Python script are available via the `this.props.args` dictionary:

```python
# Send arguments in Python:
result = my_component(greeting="Hello", name="Streamlit")
```

```javascript
// Receive arguments in frontend:
let greeting = this.props.args["greeting"]; // greeting = "Hello"
let name = this.props.args["name"]; // name = "Streamlit"
```

- Use `Streamlit.setComponentValue()` to return data from the component to the Python script:

```javascript
// Set value in frontend:
Streamlit.setComponentValue(3.14);
```

```python
# Access value in Python:
result = my_component(greeting="Hello", name="Streamlit")
st.write("result = ", result) # result = 3.14
```

When you call `Streamlit.setComponentValue(new_value)`, that new value is sent to Streamlit, which then _re-executes the Python script from top to bottom_. When the script is re-executed, the call to `my_component(...)` will return the new value.

From a _code flow_ perspective, it appears that you're transmitting data synchronously with the frontend: Python sends the arguments to JavaScript, and JavaScript returns a value to Python, all in a single function call! But in reality this is all happening _asynchronously_, and it's the re-execution of the Python script that achieves the sleight of hand.

- Use `Streamlit.setFrameHeight()` to control the height of your component. By default, the React template calls this automatically (see `StreamlitComponentBase.componentDidUpdate()`). You can override this behavior if you need more control.
- There's a tiny bit of magic in the last line of the file: `export default withStreamlitConnection(MyComponent)` - this does some handshaking with Streamlit, and sets up the mechanisms for bi-directional data communication.

#### TypeScript-only

The TypeScript-only template is in `template-reactless/my_component/frontend/src/MyComponent.tsx`.

This template has much more code than its React sibling, in that all the mechanics of handshaking, setting up event listeners, and updating the component's frame height are done manually. The React version of the template handles most of these details automatically.

- Towards the bottom of the source file, the template calls `Streamlit.setComponentReady()` to tell Streamlit it's ready to start receiving data. (You'll generally want to do this after creating and loading everything that the Component relies on.)
- It subscribes to `Streamlit.RENDER_EVENT` to be notified of when to redraw. (This event won't be fired until `setComponentReady` is called)
- Within its `onRender` event handler, it accesses the arguments passed in the Python script via `event.detail.args`
- It sends data back to the Python script in the same way that the React template doesΓÇöclicking on the "Click Me!" button calls `Streamlit.setComponentValue()`
- It informs Streamlit when its height may have changed via `Streamlit.setFrameHeight()`

#### Working with Themes

<Note>

Custom component theme support requires streamlit-component-lib version 1.2.0 or higher.

</Note>

Along with sending an `args` object to your component, Streamlit also sends
a `theme` object defining the active theme so that your component can adjust
its styling in a compatible way. This object is sent in the same message as
`args`, so it can be accessed via `this.props.theme` (when using the React
template) or `event.detail.theme` (when using the plain TypeScript template).

The `theme` object has the following shape:

```json
{
  "base": "lightORdark",
  "primaryColor": "someColor1",
  "backgroundColor": "someColor2",
  "secondaryBackgroundColor": "someColor3",
  "textColor": "someColor4",
  "font": "someFont"
}
```

The `base` option allows you to specify a preset Streamlit theme that your custom theme inherits from. Any theme config options not defined in your theme settings have their values set to those of the base theme. Valid values for `base` are `"light"` and `"dark"`.

Note that the theme object has fields with the same names and semantics as the
options in the "theme" section of the config options printed with the command
`streamlit config show`.

When using the React template, the following CSS variables are also set
automatically.

```css
--base
--primary-color
--background-color
--secondary-background-color
--text-color
--font
```

If you're not familiar with
[CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties),
the TLDR version is that you can use them like this:

```css
.mySelector {
  color: var(--text-color);
}
```

These variables match the fields defined in the `theme` object above, and
whether to use CSS variables or the theme object in your component is a matter
of personal preference.

#### Other frontend details

- Because you're hosting your component from a dev server (via `npm run start`), any changes you make should be automatically reflected in the Streamlit app when you save.
- If you want to add more packages to your component, run `npm add` to add them from within your component's `frontend/` directory.

```bash
npm add baseui
```

- To build a static version of your component, run `npm run export`. See [Prepare your Component](publish#prepare-your-component) for more information

### Python API

`components.declare_component()` is all that's required to create your Component's Python API:

```python
  import streamlit.components.v1 as components
  my_component = components.declare_component(
    "my_component",
    url="http://localhost:3001"
  )
```

You can then use the returned `my_component` function to send and receive data with your frontend code:

```python
# Send data to the frontend using named arguments.
return_value = my_component(name="Blackbeard", ship="Queen Anne's Revenge")

# `my_component`'s return value is the data returned from the frontend.
st.write("Value = ", return_value)
```

While the above is all you need to define from the Python side to have a working Component, we recommend creating a "wrapper" function with named arguments and default values, input validation and so on. This will make it easier for end-users to understand what data values your function accepts and allows for defining helpful docstrings.

Please see [this example](https://github.com/streamlit/component-template/blob/master/template/my_component/__init__.py#L41-L77) from the Components-template for an example of creating a wrapper function.

### Data serialization

#### Python ΓåÆ Frontend

You send data from Python to the frontend by passing keyword args to your Component's invoke function (that is, the function returned from `declare_component`). You can send the following types of data from Python to the frontend:

- Any JSON-serializable data
- `numpy.array`
- `pandas.DataFrame`

Any JSON-serializable data gets serialized to a JSON string, and deserialized to its JavaScript equivalent. `numpy.array` and `pandas.DataFrame` get serialized using [Apache Arrow](https://arrow.apache.org/) and are deserialized as instances of `ArrowTable`, which is a custom type that wraps Arrow structures and provides a convenient API on top of them.

Check out the [CustomDataframe](https://github.com/streamlit/component-template/tree/master/examples/CustomDataframe) and [SelectableDataTable](https://github.com/streamlit/component-template/tree/master/examples/SelectableDataTable) Component example code for more context on how to use `ArrowTable`.

#### Frontend ΓåÆ Python

You send data from the frontend to Python via the `Streamlit.setComponentValue()` API (which is part of the template code). Unlike arg-passing from Python ΓåÆ frontend, **this API takes a single value**. If you want to return multiple values, you'll need to wrap them in an `Array` or `Object`.

Custom Components can send JSON-serializable data from the frontend to Python, as well as [Apache Arrow](http://arrow.apache.org/) `ArrowTable`s to represent dataframes.

```

```
