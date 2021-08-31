# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetJobEntitiesObjectDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance': 'GetJobEntitiesInstanceInfoDetail',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'instance': 'instance',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, instance=None, resource_ids=None):
        """GetJobEntitiesObjectDetail - a model defined in huaweicloud sdk"""
        
        

        self._instance = None
        self._resource_ids = None
        self.discriminator = None

        self.instance = instance
        self.resource_ids = resource_ids

    @property
    def instance(self):
        """Gets the instance of this GetJobEntitiesObjectDetail.


        :return: The instance of this GetJobEntitiesObjectDetail.
        :rtype: GetJobEntitiesInstanceInfoDetail
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this GetJobEntitiesObjectDetail.


        :param instance: The instance of this GetJobEntitiesObjectDetail.
        :type: GetJobEntitiesInstanceInfoDetail
        """
        self._instance = instance

    @property
    def resource_ids(self):
        """Gets the resource_ids of this GetJobEntitiesObjectDetail.

        任务涉及到的资源ID。

        :return: The resource_ids of this GetJobEntitiesObjectDetail.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this GetJobEntitiesObjectDetail.

        任务涉及到的资源ID。

        :param resource_ids: The resource_ids of this GetJobEntitiesObjectDetail.
        :type: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, GetJobEntitiesObjectDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
