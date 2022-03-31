# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlavorByTypeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'types': 'str',
        'body': 'UpdateFlavorReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'types': 'types',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, types=None, body=None):
        """UpdateFlavorByTypeRequest - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._types = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.types = types
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateFlavorByTypeRequest.

        指定待更改的集群ID。

        :return: The cluster_id of this UpdateFlavorByTypeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateFlavorByTypeRequest.

        指定待更改的集群ID。

        :param cluster_id: The cluster_id of this UpdateFlavorByTypeRequest.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def types(self):
        """Gets the types of this UpdateFlavorByTypeRequest.

        指定待更改的集群节点类型。

        :return: The types of this UpdateFlavorByTypeRequest.
        :rtype: str
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this UpdateFlavorByTypeRequest.

        指定待更改的集群节点类型。

        :param types: The types of this UpdateFlavorByTypeRequest.
        :type: str
        """
        self._types = types

    @property
    def body(self):
        """Gets the body of this UpdateFlavorByTypeRequest.


        :return: The body of this UpdateFlavorByTypeRequest.
        :rtype: UpdateFlavorReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateFlavorByTypeRequest.


        :param body: The body of this UpdateFlavorByTypeRequest.
        :type: UpdateFlavorReq
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
        if not isinstance(other, UpdateFlavorByTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other