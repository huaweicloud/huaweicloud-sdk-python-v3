# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'JobTag',
        'description': 'str',
        'sex': 'str',
        'voice_name': 'str',
        'language': 'str',
        'phone': 'str',
        'app_user_id': 'str',
        'output_language': 'str',
        'custom_text': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'description': 'description',
        'sex': 'sex',
        'voice_name': 'voice_name',
        'language': 'language',
        'phone': 'phone',
        'app_user_id': 'app_user_id',
        'output_language': 'output_language',
        'custom_text': 'custom_text'
    }

    def __init__(self, tag=None, description=None, sex=None, voice_name=None, language=None, phone=None, app_user_id=None, output_language=None, custom_text=None):
        r"""CommitJobReq

        The model defined in huaweicloud sdk

        :param tag: 
        :type tag: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        :param description: 一段描述信息,会呈现在资产库中。
        :type description: str
        :param sex: 语音性别,是男性声音还是女性声音。 * FEMALE: 女性 * MALE: 男性
        :type sex: str
        :param voice_name: 音色名称。该名称会作为资产库中音色模型资产名称。
        :type voice_name: str
        :param language: 训练语言,当前仅支持中文。 * CN: 中文 * EN: 英文
        :type language: str
        :param phone: 手机号
        :type phone: str
        :param app_user_id: 第三方用户id
        :type app_user_id: str
        :param output_language: 模型输出语言类型
        :type output_language: str
        :param custom_text: 自定义试听文本
        :type custom_text: str
        """
        
        

        self._tag = None
        self._description = None
        self._sex = None
        self._voice_name = None
        self._language = None
        self._phone = None
        self._app_user_id = None
        self._output_language = None
        self._custom_text = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if description is not None:
            self.description = description
        if sex is not None:
            self.sex = sex
        if voice_name is not None:
            self.voice_name = voice_name
        if language is not None:
            self.language = language
        if phone is not None:
            self.phone = phone
        if app_user_id is not None:
            self.app_user_id = app_user_id
        if output_language is not None:
            self.output_language = output_language
        if custom_text is not None:
            self.custom_text = custom_text

    @property
    def tag(self):
        r"""Gets the tag of this CommitJobReq.

        :return: The tag of this CommitJobReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CommitJobReq.

        :param tag: The tag of this CommitJobReq.
        :type tag: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        self._tag = tag

    @property
    def description(self):
        r"""Gets the description of this CommitJobReq.

        一段描述信息,会呈现在资产库中。

        :return: The description of this CommitJobReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CommitJobReq.

        一段描述信息,会呈现在资产库中。

        :param description: The description of this CommitJobReq.
        :type description: str
        """
        self._description = description

    @property
    def sex(self):
        r"""Gets the sex of this CommitJobReq.

        语音性别,是男性声音还是女性声音。 * FEMALE: 女性 * MALE: 男性

        :return: The sex of this CommitJobReq.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this CommitJobReq.

        语音性别,是男性声音还是女性声音。 * FEMALE: 女性 * MALE: 男性

        :param sex: The sex of this CommitJobReq.
        :type sex: str
        """
        self._sex = sex

    @property
    def voice_name(self):
        r"""Gets the voice_name of this CommitJobReq.

        音色名称。该名称会作为资产库中音色模型资产名称。

        :return: The voice_name of this CommitJobReq.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        r"""Sets the voice_name of this CommitJobReq.

        音色名称。该名称会作为资产库中音色模型资产名称。

        :param voice_name: The voice_name of this CommitJobReq.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def language(self):
        r"""Gets the language of this CommitJobReq.

        训练语言,当前仅支持中文。 * CN: 中文 * EN: 英文

        :return: The language of this CommitJobReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CommitJobReq.

        训练语言,当前仅支持中文。 * CN: 中文 * EN: 英文

        :param language: The language of this CommitJobReq.
        :type language: str
        """
        self._language = language

    @property
    def phone(self):
        r"""Gets the phone of this CommitJobReq.

        手机号

        :return: The phone of this CommitJobReq.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this CommitJobReq.

        手机号

        :param phone: The phone of this CommitJobReq.
        :type phone: str
        """
        self._phone = phone

    @property
    def app_user_id(self):
        r"""Gets the app_user_id of this CommitJobReq.

        第三方用户id

        :return: The app_user_id of this CommitJobReq.
        :rtype: str
        """
        return self._app_user_id

    @app_user_id.setter
    def app_user_id(self, app_user_id):
        r"""Sets the app_user_id of this CommitJobReq.

        第三方用户id

        :param app_user_id: The app_user_id of this CommitJobReq.
        :type app_user_id: str
        """
        self._app_user_id = app_user_id

    @property
    def output_language(self):
        r"""Gets the output_language of this CommitJobReq.

        模型输出语言类型

        :return: The output_language of this CommitJobReq.
        :rtype: str
        """
        return self._output_language

    @output_language.setter
    def output_language(self, output_language):
        r"""Sets the output_language of this CommitJobReq.

        模型输出语言类型

        :param output_language: The output_language of this CommitJobReq.
        :type output_language: str
        """
        self._output_language = output_language

    @property
    def custom_text(self):
        r"""Gets the custom_text of this CommitJobReq.

        自定义试听文本

        :return: The custom_text of this CommitJobReq.
        :rtype: str
        """
        return self._custom_text

    @custom_text.setter
    def custom_text(self, custom_text):
        r"""Sets the custom_text of this CommitJobReq.

        自定义试听文本

        :param custom_text: The custom_text of this CommitJobReq.
        :type custom_text: str
        """
        self._custom_text = custom_text

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
        if not isinstance(other, CommitJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
