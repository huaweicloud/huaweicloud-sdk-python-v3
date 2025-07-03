# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAttachmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'provider_code': 'str',
        'msg': 'str',
        'data': 'ExternalAttachment',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'provider_code': 'provider_code',
        'msg': 'msg',
        'data': 'data',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, code=None, provider_code=None, msg=None, data=None, name=None, id=None):
        r"""CreateAttachmentResponse

        The model defined in huaweicloud sdk

        :param code: 业务code，0 代表业务成功，其他数值代表有错误，详情请见错误码。
        :type code: str
        :param provider_code: 服务编码。
        :type provider_code: str
        :param msg: 错误信息，code为0，此值为空；code不为0，此处为具体的错误描述。
        :type msg: str
        :param data: 
        :type data: :class:`huaweicloudsdkcoc.v1.ExternalAttachment`
        :param name: **参数解释：** 附件文件名。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param id: **参数解释：** 附件唯一id。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        """
        
        super(CreateAttachmentResponse, self).__init__()

        self._code = None
        self._provider_code = None
        self._msg = None
        self._data = None
        self._name = None
        self._id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if provider_code is not None:
            self.provider_code = provider_code
        if msg is not None:
            self.msg = msg
        if data is not None:
            self.data = data
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def code(self):
        r"""Gets the code of this CreateAttachmentResponse.

        业务code，0 代表业务成功，其他数值代表有错误，详情请见错误码。

        :return: The code of this CreateAttachmentResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateAttachmentResponse.

        业务code，0 代表业务成功，其他数值代表有错误，详情请见错误码。

        :param code: The code of this CreateAttachmentResponse.
        :type code: str
        """
        self._code = code

    @property
    def provider_code(self):
        r"""Gets the provider_code of this CreateAttachmentResponse.

        服务编码。

        :return: The provider_code of this CreateAttachmentResponse.
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        r"""Sets the provider_code of this CreateAttachmentResponse.

        服务编码。

        :param provider_code: The provider_code of this CreateAttachmentResponse.
        :type provider_code: str
        """
        self._provider_code = provider_code

    @property
    def msg(self):
        r"""Gets the msg of this CreateAttachmentResponse.

        错误信息，code为0，此值为空；code不为0，此处为具体的错误描述。

        :return: The msg of this CreateAttachmentResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this CreateAttachmentResponse.

        错误信息，code为0，此值为空；code不为0，此处为具体的错误描述。

        :param msg: The msg of this CreateAttachmentResponse.
        :type msg: str
        """
        self._msg = msg

    @property
    def data(self):
        r"""Gets the data of this CreateAttachmentResponse.

        :return: The data of this CreateAttachmentResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.ExternalAttachment`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this CreateAttachmentResponse.

        :param data: The data of this CreateAttachmentResponse.
        :type data: :class:`huaweicloudsdkcoc.v1.ExternalAttachment`
        """
        self._data = data

    @property
    def name(self):
        r"""Gets the name of this CreateAttachmentResponse.

        **参数解释：** 附件文件名。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this CreateAttachmentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAttachmentResponse.

        **参数解释：** 附件文件名。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this CreateAttachmentResponse.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this CreateAttachmentResponse.

        **参数解释：** 附件唯一id。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this CreateAttachmentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAttachmentResponse.

        **参数解释：** 附件唯一id。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this CreateAttachmentResponse.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, CreateAttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
