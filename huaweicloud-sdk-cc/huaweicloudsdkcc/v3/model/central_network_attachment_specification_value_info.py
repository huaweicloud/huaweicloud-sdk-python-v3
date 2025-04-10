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
        'attachment_parent_instance_id': 'str',
        'hosted_cloud': 'HostedCloudEnum',
        'approved_state': 'ApprovedStateEnum',
        'reason': 'str'
    }

    attribute_map = {
        'enterprise_router_table_id': 'enterprise_router_table_id',
        'attachment_parent_instance_id': 'attachment_parent_instance_id',
        'hosted_cloud': 'hosted_cloud',
        'approved_state': 'approved_state',
        'reason': 'reason'
    }

    def __init__(self, enterprise_router_table_id=None, attachment_parent_instance_id=None, hosted_cloud=None, approved_state=None, reason=None):
        r"""CentralNetworkAttachmentSpecificationValueInfo

        The model defined in huaweicloud sdk

        :param enterprise_router_table_id: 企业路由器的路由表ID。
        :type enterprise_router_table_id: str
        :param attachment_parent_instance_id: 连接的父资源ID，这里表示企业路由器ID。
        :type attachment_parent_instance_id: str
        :param hosted_cloud: 
        :type hosted_cloud: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        :param approved_state: 
        :type approved_state: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        :param reason: 审批拒绝创建附件的原因。
        :type reason: str
        """
        
        

        self._enterprise_router_table_id = None
        self._attachment_parent_instance_id = None
        self._hosted_cloud = None
        self._approved_state = None
        self._reason = None
        self.discriminator = None

        self.enterprise_router_table_id = enterprise_router_table_id
        if attachment_parent_instance_id is not None:
            self.attachment_parent_instance_id = attachment_parent_instance_id
        if hosted_cloud is not None:
            self.hosted_cloud = hosted_cloud
        if approved_state is not None:
            self.approved_state = approved_state
        if reason is not None:
            self.reason = reason

    @property
    def enterprise_router_table_id(self):
        r"""Gets the enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.

        企业路由器的路由表ID。

        :return: The enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: str
        """
        return self._enterprise_router_table_id

    @enterprise_router_table_id.setter
    def enterprise_router_table_id(self, enterprise_router_table_id):
        r"""Sets the enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.

        企业路由器的路由表ID。

        :param enterprise_router_table_id: The enterprise_router_table_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :type enterprise_router_table_id: str
        """
        self._enterprise_router_table_id = enterprise_router_table_id

    @property
    def attachment_parent_instance_id(self):
        r"""Gets the attachment_parent_instance_id of this CentralNetworkAttachmentSpecificationValueInfo.

        连接的父资源ID，这里表示企业路由器ID。

        :return: The attachment_parent_instance_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: str
        """
        return self._attachment_parent_instance_id

    @attachment_parent_instance_id.setter
    def attachment_parent_instance_id(self, attachment_parent_instance_id):
        r"""Sets the attachment_parent_instance_id of this CentralNetworkAttachmentSpecificationValueInfo.

        连接的父资源ID，这里表示企业路由器ID。

        :param attachment_parent_instance_id: The attachment_parent_instance_id of this CentralNetworkAttachmentSpecificationValueInfo.
        :type attachment_parent_instance_id: str
        """
        self._attachment_parent_instance_id = attachment_parent_instance_id

    @property
    def hosted_cloud(self):
        r"""Gets the hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.

        :return: The hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        """
        return self._hosted_cloud

    @hosted_cloud.setter
    def hosted_cloud(self, hosted_cloud):
        r"""Sets the hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.

        :param hosted_cloud: The hosted_cloud of this CentralNetworkAttachmentSpecificationValueInfo.
        :type hosted_cloud: :class:`huaweicloudsdkcc.v3.HostedCloudEnum`
        """
        self._hosted_cloud = hosted_cloud

    @property
    def approved_state(self):
        r"""Gets the approved_state of this CentralNetworkAttachmentSpecificationValueInfo.

        :return: The approved_state of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        """
        return self._approved_state

    @approved_state.setter
    def approved_state(self, approved_state):
        r"""Sets the approved_state of this CentralNetworkAttachmentSpecificationValueInfo.

        :param approved_state: The approved_state of this CentralNetworkAttachmentSpecificationValueInfo.
        :type approved_state: :class:`huaweicloudsdkcc.v3.ApprovedStateEnum`
        """
        self._approved_state = approved_state

    @property
    def reason(self):
        r"""Gets the reason of this CentralNetworkAttachmentSpecificationValueInfo.

        审批拒绝创建附件的原因。

        :return: The reason of this CentralNetworkAttachmentSpecificationValueInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this CentralNetworkAttachmentSpecificationValueInfo.

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
