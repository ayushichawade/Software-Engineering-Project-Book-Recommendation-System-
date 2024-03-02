import org.junit.Test;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

public class SignInAndLoginTest {

    @Test
    public void testSignUpAndLogin() {
        SignInAndLogin.main(new String[]{});
        String simulatedUserInput = "1\nusername\npassword\n2\nusername\npassword\n3\n";
        System.setIn(new ByteArrayInputStream(simulatedUserInput.getBytes()));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outputStream));

        SignInAndLogin.main(new String[]{});
        String output = outputStream.toString();

        assert output.contains("User registered successfully.") : "User registration message not found";
        assert output.contains("Login successful. Welcome, username!") : "Login message not found";
    }
}
