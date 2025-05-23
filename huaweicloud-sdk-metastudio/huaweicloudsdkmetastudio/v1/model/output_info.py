# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_addr': 'str',
        'body_addr': 'str',
        'audio_addr': 'str',
        'session_id': 'int',
        'output_data_version': 'str'
    }

    attribute_map = {
        'face_addr': 'face_addr',
        'body_addr': 'body_addr',
        'audio_addr': 'audio_addr',
        'session_id': 'session_id',
        'output_data_version': 'output_data_version'
    }

    def __init__(self, face_addr=None, body_addr=None, audio_addr=None, session_id=None, output_data_version=None):
        r"""OutputInfo

        The model defined in huaweicloud sdk

        :param face_addr: 面部表情输入地址。
        :type face_addr: str
        :param body_addr: 身体动作输入地址。
        :type body_addr: str
        :param audio_addr: 音频输入地址。
        :type audio_addr: str
        :param session_id: 会话ID。
        :type session_id: int
        :param output_data_version: 输出数据的格式版本，如请求中无此参数，则输出数据格式为1.0，可选值有： 1.0: 对应的输出为：         动作数据：75个骨骼旋转值         表情数据：52ARkit表情及参数 2.0: 对应的输出为：         动作数据：55个骨骼旋转值+骨骼3D坐标         表情数据：178个控制器的数据
        :type output_data_version: str
        """
        
        

        self._face_addr = None
        self._body_addr = None
        self._audio_addr = None
        self._session_id = None
        self._output_data_version = None
        self.discriminator = None

        if face_addr is not None:
            self.face_addr = face_addr
        if body_addr is not None:
            self.body_addr = body_addr
        if audio_addr is not None:
            self.audio_addr = audio_addr
        if session_id is not None:
            self.session_id = session_id
        if output_data_version is not None:
            self.output_data_version = output_data_version

    @property
    def face_addr(self):
        r"""Gets the face_addr of this OutputInfo.

        面部表情输入地址。

        :return: The face_addr of this OutputInfo.
        :rtype: str
        """
        return self._face_addr

    @face_addr.setter
    def face_addr(self, face_addr):
        r"""Sets the face_addr of this OutputInfo.

        面部表情输入地址。

        :param face_addr: The face_addr of this OutputInfo.
        :type face_addr: str
        """
        self._face_addr = face_addr

    @property
    def body_addr(self):
        r"""Gets the body_addr of this OutputInfo.

        身体动作输入地址。

        :return: The body_addr of this OutputInfo.
        :rtype: str
        """
        return self._body_addr

    @body_addr.setter
    def body_addr(self, body_addr):
        r"""Sets the body_addr of this OutputInfo.

        身体动作输入地址。

        :param body_addr: The body_addr of this OutputInfo.
        :type body_addr: str
        """
        self._body_addr = body_addr

    @property
    def audio_addr(self):
        r"""Gets the audio_addr of this OutputInfo.

        音频输入地址。

        :return: The audio_addr of this OutputInfo.
        :rtype: str
        """
        return self._audio_addr

    @audio_addr.setter
    def audio_addr(self, audio_addr):
        r"""Sets the audio_addr of this OutputInfo.

        音频输入地址。

        :param audio_addr: The audio_addr of this OutputInfo.
        :type audio_addr: str
        """
        self._audio_addr = audio_addr

    @property
    def session_id(self):
        r"""Gets the session_id of this OutputInfo.

        会话ID。

        :return: The session_id of this OutputInfo.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this OutputInfo.

        会话ID。

        :param session_id: The session_id of this OutputInfo.
        :type session_id: int
        """
        self._session_id = session_id

    @property
    def output_data_version(self):
        r"""Gets the output_data_version of this OutputInfo.

        输出数据的格式版本，如请求中无此参数，则输出数据格式为1.0，可选值有： 1.0: 对应的输出为：         动作数据：75个骨骼旋转值         表情数据：52ARkit表情及参数 2.0: 对应的输出为：         动作数据：55个骨骼旋转值+骨骼3D坐标         表情数据：178个控制器的数据

        :return: The output_data_version of this OutputInfo.
        :rtype: str
        """
        return self._output_data_version

    @output_data_version.setter
    def output_data_version(self, output_data_version):
        r"""Sets the output_data_version of this OutputInfo.

        输出数据的格式版本，如请求中无此参数，则输出数据格式为1.0，可选值有： 1.0: 对应的输出为：         动作数据：75个骨骼旋转值         表情数据：52ARkit表情及参数 2.0: 对应的输出为：         动作数据：55个骨骼旋转值+骨骼3D坐标         表情数据：178个控制器的数据

        :param output_data_version: The output_data_version of this OutputInfo.
        :type output_data_version: str
        """
        self._output_data_version = output_data_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OutputInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
