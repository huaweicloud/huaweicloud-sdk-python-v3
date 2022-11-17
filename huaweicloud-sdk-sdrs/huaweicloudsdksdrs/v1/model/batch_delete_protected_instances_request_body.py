# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteProtectedInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protected_instances': 'list[ResourceId]',
        'delete_target_server': 'bool',
        'delete_target_eip': 'bool'
    }

    attribute_map = {
        'protected_instances': 'protected_instances',
        'delete_target_server': 'delete_target_server',
        'delete_target_eip': 'delete_target_eip'
    }

    def __init__(self, protected_instances=None, delete_target_server=None, delete_target_eip=None):
        """BatchDeleteProtectedInstancesRequestBody

        The model defined in huaweicloud sdk

        :param protected_instances: 所需要删除的保护实例列表。
        :type protected_instances: list[:class:`huaweicloudsdksdrs.v1.ResourceId`]
        :param delete_target_server: 是否删除容灾站点服务器，默认值为false。
        :type delete_target_server: bool
        :param delete_target_eip: 是否删除容灾站点弹性IP，默认值为false。
        :type delete_target_eip: bool
        """
        
        

        self._protected_instances = None
        self._delete_target_server = None
        self._delete_target_eip = None
        self.discriminator = None

        self.protected_instances = protected_instances
        if delete_target_server is not None:
            self.delete_target_server = delete_target_server
        if delete_target_eip is not None:
            self.delete_target_eip = delete_target_eip

    @property
    def protected_instances(self):
        """Gets the protected_instances of this BatchDeleteProtectedInstancesRequestBody.

        所需要删除的保护实例列表。

        :return: The protected_instances of this BatchDeleteProtectedInstancesRequestBody.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ResourceId`]
        """
        return self._protected_instances

    @protected_instances.setter
    def protected_instances(self, protected_instances):
        """Sets the protected_instances of this BatchDeleteProtectedInstancesRequestBody.

        所需要删除的保护实例列表。

        :param protected_instances: The protected_instances of this BatchDeleteProtectedInstancesRequestBody.
        :type protected_instances: list[:class:`huaweicloudsdksdrs.v1.ResourceId`]
        """
        self._protected_instances = protected_instances

    @property
    def delete_target_server(self):
        """Gets the delete_target_server of this BatchDeleteProtectedInstancesRequestBody.

        是否删除容灾站点服务器，默认值为false。

        :return: The delete_target_server of this BatchDeleteProtectedInstancesRequestBody.
        :rtype: bool
        """
        return self._delete_target_server

    @delete_target_server.setter
    def delete_target_server(self, delete_target_server):
        """Sets the delete_target_server of this BatchDeleteProtectedInstancesRequestBody.

        是否删除容灾站点服务器，默认值为false。

        :param delete_target_server: The delete_target_server of this BatchDeleteProtectedInstancesRequestBody.
        :type delete_target_server: bool
        """
        self._delete_target_server = delete_target_server

    @property
    def delete_target_eip(self):
        """Gets the delete_target_eip of this BatchDeleteProtectedInstancesRequestBody.

        是否删除容灾站点弹性IP，默认值为false。

        :return: The delete_target_eip of this BatchDeleteProtectedInstancesRequestBody.
        :rtype: bool
        """
        return self._delete_target_eip

    @delete_target_eip.setter
    def delete_target_eip(self, delete_target_eip):
        """Sets the delete_target_eip of this BatchDeleteProtectedInstancesRequestBody.

        是否删除容灾站点弹性IP，默认值为false。

        :param delete_target_eip: The delete_target_eip of this BatchDeleteProtectedInstancesRequestBody.
        :type delete_target_eip: bool
        """
        self._delete_target_eip = delete_target_eip

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
        if not isinstance(other, BatchDeleteProtectedInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
