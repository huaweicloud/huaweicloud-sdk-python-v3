# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrainingJobReq:

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
        'create_type': 'CreateType',
        'phone': 'str',
        'dhtms_job_id': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'description': 'description',
        'sex': 'sex',
        'voice_name': 'voice_name',
        'language': 'language',
        'create_type': 'create_type',
        'phone': 'phone',
        'dhtms_job_id': 'dhtms_job_id'
    }

    def __init__(self, tag=None, description=None, sex=None, voice_name=None, language=None, create_type=None, phone=None, dhtms_job_id=None):
        """CreateTrainingJobReq

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
        :param create_type: 
        :type create_type: :class:`huaweicloudsdkmetastudio.v1.CreateType`
        :param phone: 手机号
        :type phone: str
        :param dhtms_job_id: 形象制作任务id
        :type dhtms_job_id: str
        """
        
        

        self._tag = None
        self._description = None
        self._sex = None
        self._voice_name = None
        self._language = None
        self._create_type = None
        self._phone = None
        self._dhtms_job_id = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if description is not None:
            self.description = description
        if sex is not None:
            self.sex = sex
        self.voice_name = voice_name
        if language is not None:
            self.language = language
        if create_type is not None:
            self.create_type = create_type
        if phone is not None:
            self.phone = phone
        if dhtms_job_id is not None:
            self.dhtms_job_id = dhtms_job_id

    @property
    def tag(self):
        """Gets the tag of this CreateTrainingJobReq.

        :return: The tag of this CreateTrainingJobReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateTrainingJobReq.

        :param tag: The tag of this CreateTrainingJobReq.
        :type tag: :class:`huaweicloudsdkmetastudio.v1.JobTag`
        """
        self._tag = tag

    @property
    def description(self):
        """Gets the description of this CreateTrainingJobReq.

        一段描述信息,会呈现在资产库中。

        :return: The description of this CreateTrainingJobReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTrainingJobReq.

        一段描述信息,会呈现在资产库中。

        :param description: The description of this CreateTrainingJobReq.
        :type description: str
        """
        self._description = description

    @property
    def sex(self):
        """Gets the sex of this CreateTrainingJobReq.

        语音性别,是男性声音还是女性声音。 * FEMALE: 女性 * MALE: 男性

        :return: The sex of this CreateTrainingJobReq.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this CreateTrainingJobReq.

        语音性别,是男性声音还是女性声音。 * FEMALE: 女性 * MALE: 男性

        :param sex: The sex of this CreateTrainingJobReq.
        :type sex: str
        """
        self._sex = sex

    @property
    def voice_name(self):
        """Gets the voice_name of this CreateTrainingJobReq.

        音色名称。该名称会作为资产库中音色模型资产名称。

        :return: The voice_name of this CreateTrainingJobReq.
        :rtype: str
        """
        return self._voice_name

    @voice_name.setter
    def voice_name(self, voice_name):
        """Sets the voice_name of this CreateTrainingJobReq.

        音色名称。该名称会作为资产库中音色模型资产名称。

        :param voice_name: The voice_name of this CreateTrainingJobReq.
        :type voice_name: str
        """
        self._voice_name = voice_name

    @property
    def language(self):
        """Gets the language of this CreateTrainingJobReq.

        训练语言,当前仅支持中文。 * CN: 中文 * EN: 英文

        :return: The language of this CreateTrainingJobReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateTrainingJobReq.

        训练语言,当前仅支持中文。 * CN: 中文 * EN: 英文

        :param language: The language of this CreateTrainingJobReq.
        :type language: str
        """
        self._language = language

    @property
    def create_type(self):
        """Gets the create_type of this CreateTrainingJobReq.

        :return: The create_type of this CreateTrainingJobReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateType`
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        """Sets the create_type of this CreateTrainingJobReq.

        :param create_type: The create_type of this CreateTrainingJobReq.
        :type create_type: :class:`huaweicloudsdkmetastudio.v1.CreateType`
        """
        self._create_type = create_type

    @property
    def phone(self):
        """Gets the phone of this CreateTrainingJobReq.

        手机号

        :return: The phone of this CreateTrainingJobReq.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateTrainingJobReq.

        手机号

        :param phone: The phone of this CreateTrainingJobReq.
        :type phone: str
        """
        self._phone = phone

    @property
    def dhtms_job_id(self):
        """Gets the dhtms_job_id of this CreateTrainingJobReq.

        形象制作任务id

        :return: The dhtms_job_id of this CreateTrainingJobReq.
        :rtype: str
        """
        return self._dhtms_job_id

    @dhtms_job_id.setter
    def dhtms_job_id(self, dhtms_job_id):
        """Sets the dhtms_job_id of this CreateTrainingJobReq.

        形象制作任务id

        :param dhtms_job_id: The dhtms_job_id of this CreateTrainingJobReq.
        :type dhtms_job_id: str
        """
        self._dhtms_job_id = dhtms_job_id

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
        if not isinstance(other, CreateTrainingJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
