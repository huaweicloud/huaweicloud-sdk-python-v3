# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateCompositeHostsRequest:

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
        'target_enterprise_project_id': 'str',
        'body': 'MigrateCompositeHostsRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'target_enterprise_project_id': 'target_enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, target_enterprise_project_id=None, body=None):
        """MigrateCompositeHostsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 当前企业项目ID
        :type enterprise_project_id: str
        :param target_enterprise_project_id: 迁移的目标企业项目ID
        :type target_enterprise_project_id: str
        :param body: Body of the MigrateCompositeHostsRequest
        :type body: :class:`huaweicloudsdkwaf.v1.MigrateCompositeHostsRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._target_enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.target_enterprise_project_id = target_enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MigrateCompositeHostsRequest.

        当前企业项目ID

        :return: The enterprise_project_id of this MigrateCompositeHostsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MigrateCompositeHostsRequest.

        当前企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this MigrateCompositeHostsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def target_enterprise_project_id(self):
        """Gets the target_enterprise_project_id of this MigrateCompositeHostsRequest.

        迁移的目标企业项目ID

        :return: The target_enterprise_project_id of this MigrateCompositeHostsRequest.
        :rtype: str
        """
        return self._target_enterprise_project_id

    @target_enterprise_project_id.setter
    def target_enterprise_project_id(self, target_enterprise_project_id):
        """Sets the target_enterprise_project_id of this MigrateCompositeHostsRequest.

        迁移的目标企业项目ID

        :param target_enterprise_project_id: The target_enterprise_project_id of this MigrateCompositeHostsRequest.
        :type target_enterprise_project_id: str
        """
        self._target_enterprise_project_id = target_enterprise_project_id

    @property
    def body(self):
        """Gets the body of this MigrateCompositeHostsRequest.

        :return: The body of this MigrateCompositeHostsRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.MigrateCompositeHostsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MigrateCompositeHostsRequest.

        :param body: The body of this MigrateCompositeHostsRequest.
        :type body: :class:`huaweicloudsdkwaf.v1.MigrateCompositeHostsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, MigrateCompositeHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
