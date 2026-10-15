# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chat_id': 'str',
        'file': 'file',
        'agent_type': 'str',
        'domain_type': 'str'
    }

    attribute_map = {
        'chat_id': 'chat_id',
        'file': 'file',
        'agent_type': 'agent_type',
        'domain_type': 'domain_type'
    }

    def __init__(self, chat_id=None, file=None, agent_type=None, domain_type=None):
        r"""UploadFileRequestBody

        The model defined in huaweicloud sdk

        :param chat_id: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及
        :type chat_id: str
        :param file: **参数解释**： 上传的文件。 **约束限制**： 不涉及 **取值范围**： 100MB 以内。 **默认取值**： 不涉及
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param agent_type: **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及
        :type agent_type: str
        :param domain_type: **参数解释**： 领域类型，仅agent_type为optverse时生效。 **约束限制**： 不涉及 **取值范围**： * production-planning：生产计划 * sequence-planning：生产排程 * vrp：运输计划 * optverse：通用数学规划 **默认取值**： optverse
        :type domain_type: str
        """
        
        

        self._chat_id = None
        self._file = None
        self._agent_type = None
        self._domain_type = None
        self.discriminator = None

        if chat_id is not None:
            self.chat_id = chat_id
        self.file = file
        self.agent_type = agent_type
        if domain_type is not None:
            self.domain_type = domain_type

    @property
    def chat_id(self):
        r"""Gets the chat_id of this UploadFileRequestBody.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及

        :return: The chat_id of this UploadFileRequestBody.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        r"""Sets the chat_id of this UploadFileRequestBody.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及

        :param chat_id: The chat_id of this UploadFileRequestBody.
        :type chat_id: str
        """
        self._chat_id = chat_id

    @property
    def file(self):
        r"""Gets the file of this UploadFileRequestBody.

        **参数解释**： 上传的文件。 **约束限制**： 不涉及 **取值范围**： 100MB 以内。 **默认取值**： 不涉及

        :return: The file of this UploadFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this UploadFileRequestBody.

        **参数解释**： 上传的文件。 **约束限制**： 不涉及 **取值范围**： 100MB 以内。 **默认取值**： 不涉及

        :param file: The file of this UploadFileRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def agent_type(self):
        r"""Gets the agent_type of this UploadFileRequestBody.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及

        :return: The agent_type of this UploadFileRequestBody.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this UploadFileRequestBody.

        **参数解释**： 对话ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及

        :param agent_type: The agent_type of this UploadFileRequestBody.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def domain_type(self):
        r"""Gets the domain_type of this UploadFileRequestBody.

        **参数解释**： 领域类型，仅agent_type为optverse时生效。 **约束限制**： 不涉及 **取值范围**： * production-planning：生产计划 * sequence-planning：生产排程 * vrp：运输计划 * optverse：通用数学规划 **默认取值**： optverse

        :return: The domain_type of this UploadFileRequestBody.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this UploadFileRequestBody.

        **参数解释**： 领域类型，仅agent_type为optverse时生效。 **约束限制**： 不涉及 **取值范围**： * production-planning：生产计划 * sequence-planning：生产排程 * vrp：运输计划 * optverse：通用数学规划 **默认取值**： optverse

        :param domain_type: The domain_type of this UploadFileRequestBody.
        :type domain_type: str
        """
        self._domain_type = domain_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
