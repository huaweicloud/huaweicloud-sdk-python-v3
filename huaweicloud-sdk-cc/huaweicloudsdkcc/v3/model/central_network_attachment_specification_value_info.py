# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkAttachmentSpecificationValueInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_router_table_id': 'str',
        'attached_er_id': 'str',
        'approved_state': 'ApprovedStateEnum',
        'hosted_cloud': 'HostedCloudEnum',
        'reason': 'str'
    }

    attribute_map = {
        'enterprise_router_table_id': 'enterprise_router_table_id',
        'attached_er_id': 'attached_er_id',
        'approved_state': 'approved_state',
        'hosted_cloud': 'hosted_cloud',
        'reason': 'reason'
    }

    def __init__(self, enterprise_router_table_id=None, attached_er_id=None, approved_state=None, hosted_cloud=None, reason=None):
        """CentralNetworkAttachmentSpecificationValueInfo

        The model defined in huaweicloud sdk

        :param enterprise_router_table_id: 资源ID标识符。
        :type enterprise_router_table_id: str
        :param attached_er_id: 资源ID标识符。
        :type attached_er_id: str
        :param approved_state: 
        :type approved_state: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        :param hosted_cloud: 
        :type hosted_cloud: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        :param reason: 审批拒绝创建附件的原因。
        :type reason: str
        """
        
        

        self._enterprise_router_table_id = None
        self._attached_er_id = None
        self._approved_state = None
        self._hosted_cloud = None
        self._reason = None
        self.discriminator = None

        if enterprise_router_table_id is not None:
            self.enterprise_router_table_id = enterprise_router_table_id
        if attached_er_id is not None:
            self.attached_er_id = attached_er_id
        if approved_state is not None:
            self.approved_state = approved_state
        if hosted_cloud is not None:
            self.hosted_cloud = hosted_cloud
        if reason is not None:
            self.reason = reason

    @property
    def enterprise_router_table_id(self):
        """Gets the enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.

        资源ID标识符。

        :return: The enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: str
        """
        return self._enterprise_router_table_id

    @enterprise_router_table_id.setter
    def enterprise_router_table_id(self, enterprise_router_table_id):
        """Sets the enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.

        资源ID标识符。

        :param enterprise_router_table_id: The enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :type enterprise_router_table_id: str
        """
        self._enterprise_router_table_id = enterprise_router_table_id

    @property
    def attached_er_id(self):
        """Gets the attached_er_id of this CentralNetworkAttachmentSpecificationValueInfo.

        资源ID标识符。

        :return: The attached_er_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: str
        """
        return self._attached_er_id

    @attached_er_id.setter
    def attached_er_id(self, attached_er_id):
        """Sets the attached_er_id of this CentralNetworkAttachmentSpecificationValueInfo.

        资源ID标识符。

        :param attached_er_id: The attached_er_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :type attached_er_id: str
        """
        self._attached_er_id = attached_er_id

    @property
    def approved_state(self):
        """Gets the approved_state of this CentralNetworkAttachmentSpecificationValueInfo.

        :return: The approved_state of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        """
        return self._approved_state

    @approved_state.setter
    def approved_state(self, approved_state):
        """Sets the approved_state of this CentralNetworkAttachmentSpecificationValueInfo.

        :param approved_state: The approved_state of this CentralNetworkAttachmentSpecificationValueInfo.
        :type approved_state: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        """
        self._approved_state = approved_state

    @property
    def hosted_cloud(self):
        """Gets the hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.

        :return: The hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        """
        return self._hosted_cloud

    @hosted_cloud.setter
    def hosted_cloud(self, hosted_cloud):
        """Sets the hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.

        :param hosted_cloud: The hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.
        :type hosted_cloud: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        """
        self._hosted_cloud = hosted_cloud

    @property
    def reason(self):
        """Gets the reason of this CentralNetworkAttachmentSpecificationValueInfo.

        审批拒绝创建附件的原因。

        :return: The reason of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CentralNetworkAttachmentSpecificationValueInfo.

        审批拒绝创建附件的原因。

        :param reason: The reason of this CentralNetworkAttachmentSpecificationValueInfo.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, CentralNetworkAttachmentSpecificationValueInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
