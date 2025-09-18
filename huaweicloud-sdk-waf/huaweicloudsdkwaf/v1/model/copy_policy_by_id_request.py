# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyPolicyByIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'src_policy_id': 'str',
        'dest_policy_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'src_policy_id': 'src_policy_id',
        'dest_policy_name': 'dest_policy_name'
    }

    def __init__(self, enterprise_project_id=None, src_policy_id=None, dest_policy_name=None):
        r"""CopyPolicyByIdRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS)的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param src_policy_id: 源策略ID
        :type src_policy_id: str
        :param dest_policy_name: 复制出的新策略名称
        :type dest_policy_name: str
        """
        
        

        self._enterprise_project_id = None
        self._src_policy_id = None
        self._dest_policy_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.src_policy_id = src_policy_id
        self.dest_policy_name = dest_policy_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CopyPolicyByIdRequest.

        您可以通过调用企业项目管理服务（EPS)的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this CopyPolicyByIdRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CopyPolicyByIdRequest.

        您可以通过调用企业项目管理服务（EPS)的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CopyPolicyByIdRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def src_policy_id(self):
        r"""Gets the src_policy_id of this CopyPolicyByIdRequest.

        源策略ID

        :return: The src_policy_id of this CopyPolicyByIdRequest.
        :rtype: str
        """
        return self._src_policy_id

    @src_policy_id.setter
    def src_policy_id(self, src_policy_id):
        r"""Sets the src_policy_id of this CopyPolicyByIdRequest.

        源策略ID

        :param src_policy_id: The src_policy_id of this CopyPolicyByIdRequest.
        :type src_policy_id: str
        """
        self._src_policy_id = src_policy_id

    @property
    def dest_policy_name(self):
        r"""Gets the dest_policy_name of this CopyPolicyByIdRequest.

        复制出的新策略名称

        :return: The dest_policy_name of this CopyPolicyByIdRequest.
        :rtype: str
        """
        return self._dest_policy_name

    @dest_policy_name.setter
    def dest_policy_name(self, dest_policy_name):
        r"""Sets the dest_policy_name of this CopyPolicyByIdRequest.

        复制出的新策略名称

        :param dest_policy_name: The dest_policy_name of this CopyPolicyByIdRequest.
        :type dest_policy_name: str
        """
        self._dest_policy_name = dest_policy_name

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
        if not isinstance(other, CopyPolicyByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
