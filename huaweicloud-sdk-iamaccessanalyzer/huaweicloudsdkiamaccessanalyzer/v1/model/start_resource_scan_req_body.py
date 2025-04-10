# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartResourceScanReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_owner_account': 'str',
        'resource_project_id': 'str',
        'resource_urn': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_owner_account': 'resource_owner_account',
        'resource_project_id': 'resource_project_id',
        'resource_urn': 'resource_urn'
    }

    def __init__(self, resource_id=None, resource_owner_account=None, resource_project_id=None, resource_urn=None):
        r"""StartResourceScanReqBody

        The model defined in huaweicloud sdk

        :param resource_id: 资源的唯一标识符。
        :type resource_id: str
        :param resource_owner_account: 拥有资源的账号ID。
        :type resource_owner_account: str
        :param resource_project_id: 资源所属的项目标识符
        :type resource_project_id: str
        :param resource_urn: 资源的唯一资源标识符。
        :type resource_urn: str
        """
        
        

        self._resource_id = None
        self._resource_owner_account = None
        self._resource_project_id = None
        self._resource_urn = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        if resource_project_id is not None:
            self.resource_project_id = resource_project_id
        self.resource_urn = resource_urn

    @property
    def resource_id(self):
        r"""Gets the resource_id of this StartResourceScanReqBody.

        资源的唯一标识符。

        :return: The resource_id of this StartResourceScanReqBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this StartResourceScanReqBody.

        资源的唯一标识符。

        :param resource_id: The resource_id of this StartResourceScanReqBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_owner_account(self):
        r"""Gets the resource_owner_account of this StartResourceScanReqBody.

        拥有资源的账号ID。

        :return: The resource_owner_account of this StartResourceScanReqBody.
        :rtype: str
        """
        return self._resource_owner_account

    @resource_owner_account.setter
    def resource_owner_account(self, resource_owner_account):
        r"""Sets the resource_owner_account of this StartResourceScanReqBody.

        拥有资源的账号ID。

        :param resource_owner_account: The resource_owner_account of this StartResourceScanReqBody.
        :type resource_owner_account: str
        """
        self._resource_owner_account = resource_owner_account

    @property
    def resource_project_id(self):
        r"""Gets the resource_project_id of this StartResourceScanReqBody.

        资源所属的项目标识符

        :return: The resource_project_id of this StartResourceScanReqBody.
        :rtype: str
        """
        return self._resource_project_id

    @resource_project_id.setter
    def resource_project_id(self, resource_project_id):
        r"""Sets the resource_project_id of this StartResourceScanReqBody.

        资源所属的项目标识符

        :param resource_project_id: The resource_project_id of this StartResourceScanReqBody.
        :type resource_project_id: str
        """
        self._resource_project_id = resource_project_id

    @property
    def resource_urn(self):
        r"""Gets the resource_urn of this StartResourceScanReqBody.

        资源的唯一资源标识符。

        :return: The resource_urn of this StartResourceScanReqBody.
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        r"""Sets the resource_urn of this StartResourceScanReqBody.

        资源的唯一资源标识符。

        :param resource_urn: The resource_urn of this StartResourceScanReqBody.
        :type resource_urn: str
        """
        self._resource_urn = resource_urn

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
        if not isinstance(other, StartResourceScanReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
