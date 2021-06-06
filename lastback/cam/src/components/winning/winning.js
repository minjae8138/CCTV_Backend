import React, {useContext} from 'react';

import {Text, View, StyleSheet, Button, Image} from 'react-native';
import {NotiContext} from "../context";

const notifi = () => {
  const {notioff} = useContext(NotiContext);

  const styles = StyleSheet.create({
    container: {
      paddingTop: 50,
    },
    tinyLogo: {
      width: 50,
      height: 50,
    },
    logo: {
      width: 66,
      height: 58,
    },
  });

  return (
    <View>
      <Text>위험을 알립니다</Text>
      <Image
        style={styles.logo}
        source={{
          uri: 'https://reactnative.dev/img/tiny_logo.png',
        }}
      />
      <Button title="끄기" onPress={() => notioff()} />
    </View>
  );
};

export default notifi;
