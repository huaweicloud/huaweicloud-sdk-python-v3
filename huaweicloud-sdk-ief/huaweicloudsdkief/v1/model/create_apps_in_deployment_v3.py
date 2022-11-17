# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppsInDeploymentV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replicas': 'int',
        'template': 'PodRequest',
        'annotations': 'Annotations'
    }

    attribute_map = {
        'replicas': 'replicas',
        'template': 'template',
        'annotations': 'annotations'
    }

    def __init__(self, replicas=None, template=None, annotations=None):
        """CreateAppsInDeploymentV3

        The model defined in huaweicloud sdk

        :param replicas: 副本数量
        :type replicas: int
        :param template: 
        :type template: :class:`huaweicloudsdkief.v1.PodRequest`
        :param annotations: 
        :type annotations: :class:`huaweicloudsdkief.v1.Annotations`
        """
        
        

        self._replicas = None
        self._template = None
        self._annotations = None
        self.discriminator = None

        self.replicas = replicas
        self.template = template
        if annotations is not None:
            self.annotations = annotations

    @property
    def replicas(self):
        """Gets the replicas of this CreateAppsInDeploymentV3.

        副本数量

        :return: The replicas of this CreateAppsInDeploymentV3.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this CreateAppsInDeploymentV3.

        副本数量

        :param replicas: The replicas of this CreateAppsInDeploymentV3.
        :type replicas: int
        """
        self._replicas = replicas

    @property
    def template(self):
        """Gets the template of this CreateAppsInDeploymentV3.

        :return: The template of this CreateAppsInDeploymentV3.
        :rtype: :class:`huaweicloudsdkief.v1.PodRequest`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateAppsInDeploymentV3.

        :param template: The template of this CreateAppsInDeploymentV3.
        :type template: :class:`huaweicloudsdkief.v1.PodRequest`
        """
        self._template = template

    @property
    def annotations(self):
        """Gets the annotations of this CreateAppsInDeploymentV3.

        :return: The annotations of this CreateAppsInDeploymentV3.
        :rtype: :class:`huaweicloudsdkief.v1.Annotations`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this CreateAppsInDeploymentV3.

        :param annotations: The annotations of this CreateAppsInDeploymentV3.
        :type annotations: :class:`huaweicloudsdkief.v1.Annotations`
        """
        self._annotations = annotations

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
        if not isinstance(other, CreateAppsInDeploymentV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
