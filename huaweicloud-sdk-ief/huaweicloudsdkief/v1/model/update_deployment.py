# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDeployment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployment': 'UpdatePodDeployment',
        'description': 'str'
    }

    attribute_map = {
        'deployment': 'deployment',
        'description': 'description'
    }

    def __init__(self, deployment=None, description=None):
        """UpdateDeployment

        The model defined in huaweicloud sdk

        :param deployment: 
        :type deployment: :class:`huaweicloudsdkief.v1.UpdatePodDeployment`
        :param description: 应用部署描述修改，只修改描述不需要传入deployment参数
        :type description: str
        """
        
        

        self._deployment = None
        self._description = None
        self.discriminator = None

        if deployment is not None:
            self.deployment = deployment
        if description is not None:
            self.description = description

    @property
    def deployment(self):
        """Gets the deployment of this UpdateDeployment.

        :return: The deployment of this UpdateDeployment.
        :rtype: :class:`huaweicloudsdkief.v1.UpdatePodDeployment`
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this UpdateDeployment.

        :param deployment: The deployment of this UpdateDeployment.
        :type deployment: :class:`huaweicloudsdkief.v1.UpdatePodDeployment`
        """
        self._deployment = deployment

    @property
    def description(self):
        """Gets the description of this UpdateDeployment.

        应用部署描述修改，只修改描述不需要传入deployment参数

        :return: The description of this UpdateDeployment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDeployment.

        应用部署描述修改，只修改描述不需要传入deployment参数

        :param description: The description of this UpdateDeployment.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
