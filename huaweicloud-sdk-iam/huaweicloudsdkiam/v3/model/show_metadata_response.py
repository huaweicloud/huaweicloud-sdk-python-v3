# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'idp_id': 'str',
        'entity_id': 'str',
        'protocol_id': 'str',
        'domain_id': 'str',
        'xaccount_type': 'str',
        'update_time': 'str',
        'data': 'str'
    }

    attribute_map = {
        'id': 'id',
        'idp_id': 'idp_id',
        'entity_id': 'entity_id',
        'protocol_id': 'protocol_id',
        'domain_id': 'domain_id',
        'xaccount_type': 'xaccount_type',
        'update_time': 'update_time',
        'data': 'data'
    }

    def __init__(self, id=None, idp_id=None, entity_id=None, protocol_id=None, domain_id=None, xaccount_type=None, update_time=None, data=None):
        r"""ShowMetadataResponse

        The model defined in huaweicloud sdk

        :param id: Metadata的ID。
        :type id: str
        :param idp_id: 身份提供商ID。
        :type idp_id: str
        :param entity_id: Metadata文件中的entityID字段。
        :type entity_id: str
        :param protocol_id: 协议ID。
        :type protocol_id: str
        :param domain_id: 用户所属账号ID。
        :type domain_id: str
        :param xaccount_type: 账号来源，默认为空。
        :type xaccount_type: str
        :param update_time: 导入或更新Metadata文件的时间。
        :type update_time: str
        :param data: Metadata文件的内容。
        :type data: str
        """
        
        super(ShowMetadataResponse, self).__init__()

        self._id = None
        self._idp_id = None
        self._entity_id = None
        self._protocol_id = None
        self._domain_id = None
        self._xaccount_type = None
        self._update_time = None
        self._data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if idp_id is not None:
            self.idp_id = idp_id
        if entity_id is not None:
            self.entity_id = entity_id
        if protocol_id is not None:
            self.protocol_id = protocol_id
        if domain_id is not None:
            self.domain_id = domain_id
        if xaccount_type is not None:
            self.xaccount_type = xaccount_type
        if update_time is not None:
            self.update_time = update_time
        if data is not None:
            self.data = data

    @property
    def id(self):
        r"""Gets the id of this ShowMetadataResponse.

        Metadata的ID。

        :return: The id of this ShowMetadataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowMetadataResponse.

        Metadata的ID。

        :param id: The id of this ShowMetadataResponse.
        :type id: str
        """
        self._id = id

    @property
    def idp_id(self):
        r"""Gets the idp_id of this ShowMetadataResponse.

        身份提供商ID。

        :return: The idp_id of this ShowMetadataResponse.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        r"""Sets the idp_id of this ShowMetadataResponse.

        身份提供商ID。

        :param idp_id: The idp_id of this ShowMetadataResponse.
        :type idp_id: str
        """
        self._idp_id = idp_id

    @property
    def entity_id(self):
        r"""Gets the entity_id of this ShowMetadataResponse.

        Metadata文件中的entityID字段。

        :return: The entity_id of this ShowMetadataResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this ShowMetadataResponse.

        Metadata文件中的entityID字段。

        :param entity_id: The entity_id of this ShowMetadataResponse.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def protocol_id(self):
        r"""Gets the protocol_id of this ShowMetadataResponse.

        协议ID。

        :return: The protocol_id of this ShowMetadataResponse.
        :rtype: str
        """
        return self._protocol_id

    @protocol_id.setter
    def protocol_id(self, protocol_id):
        r"""Sets the protocol_id of this ShowMetadataResponse.

        协议ID。

        :param protocol_id: The protocol_id of this ShowMetadataResponse.
        :type protocol_id: str
        """
        self._protocol_id = protocol_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowMetadataResponse.

        用户所属账号ID。

        :return: The domain_id of this ShowMetadataResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowMetadataResponse.

        用户所属账号ID。

        :param domain_id: The domain_id of this ShowMetadataResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def xaccount_type(self):
        r"""Gets the xaccount_type of this ShowMetadataResponse.

        账号来源，默认为空。

        :return: The xaccount_type of this ShowMetadataResponse.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        r"""Sets the xaccount_type of this ShowMetadataResponse.

        账号来源，默认为空。

        :param xaccount_type: The xaccount_type of this ShowMetadataResponse.
        :type xaccount_type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowMetadataResponse.

        导入或更新Metadata文件的时间。

        :return: The update_time of this ShowMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowMetadataResponse.

        导入或更新Metadata文件的时间。

        :param update_time: The update_time of this ShowMetadataResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def data(self):
        r"""Gets the data of this ShowMetadataResponse.

        Metadata文件的内容。

        :return: The data of this ShowMetadataResponse.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowMetadataResponse.

        Metadata文件的内容。

        :param data: The data of this ShowMetadataResponse.
        :type data: str
        """
        self._data = data

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
        if not isinstance(other, ShowMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
