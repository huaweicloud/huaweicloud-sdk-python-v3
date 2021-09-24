# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussInstanceActionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'expand_cluster': 'OpenGaussExpandCluster',
        'enlarge_volume': 'OpenGaussEnlargeVolume'
    }

    attribute_map = {
        'expand_cluster': 'expand_cluster',
        'enlarge_volume': 'enlarge_volume'
    }

    def __init__(self, expand_cluster=None, enlarge_volume=None):
        """OpenGaussInstanceActionRequest - a model defined in huaweicloud sdk"""
        
        

        self._expand_cluster = None
        self._enlarge_volume = None
        self.discriminator = None

        if expand_cluster is not None:
            self.expand_cluster = expand_cluster
        if enlarge_volume is not None:
            self.enlarge_volume = enlarge_volume

    @property
    def expand_cluster(self):
        """Gets the expand_cluster of this OpenGaussInstanceActionRequest.


        :return: The expand_cluster of this OpenGaussInstanceActionRequest.
        :rtype: OpenGaussExpandCluster
        """
        return self._expand_cluster

    @expand_cluster.setter
    def expand_cluster(self, expand_cluster):
        """Sets the expand_cluster of this OpenGaussInstanceActionRequest.


        :param expand_cluster: The expand_cluster of this OpenGaussInstanceActionRequest.
        :type: OpenGaussExpandCluster
        """
        self._expand_cluster = expand_cluster

    @property
    def enlarge_volume(self):
        """Gets the enlarge_volume of this OpenGaussInstanceActionRequest.


        :return: The enlarge_volume of this OpenGaussInstanceActionRequest.
        :rtype: OpenGaussEnlargeVolume
        """
        return self._enlarge_volume

    @enlarge_volume.setter
    def enlarge_volume(self, enlarge_volume):
        """Sets the enlarge_volume of this OpenGaussInstanceActionRequest.


        :param enlarge_volume: The enlarge_volume of this OpenGaussInstanceActionRequest.
        :type: OpenGaussEnlargeVolume
        """
        self._enlarge_volume = enlarge_volume

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
        if not isinstance(other, OpenGaussInstanceActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
