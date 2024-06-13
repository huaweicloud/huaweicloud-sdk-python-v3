# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllFeatureChildrenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_id': 'str',
        'body': 'QueryTestItemTreeInfo'
    }

    attribute_map = {
        'feature_id': 'feature_id',
        'body': 'body'
    }

    def __init__(self, feature_id=None, body=None):
        """ShowAllFeatureChildrenRequest

        The model defined in huaweicloud sdk

        :param feature_id: 
        :type feature_id: str
        :param body: Body of the ShowAllFeatureChildrenRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.QueryTestItemTreeInfo`
        """
        
        

        self._feature_id = None
        self._body = None
        self.discriminator = None

        self.feature_id = feature_id
        if body is not None:
            self.body = body

    @property
    def feature_id(self):
        """Gets the feature_id of this ShowAllFeatureChildrenRequest.

        :return: The feature_id of this ShowAllFeatureChildrenRequest.
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this ShowAllFeatureChildrenRequest.

        :param feature_id: The feature_id of this ShowAllFeatureChildrenRequest.
        :type feature_id: str
        """
        self._feature_id = feature_id

    @property
    def body(self):
        """Gets the body of this ShowAllFeatureChildrenRequest.

        :return: The body of this ShowAllFeatureChildrenRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.QueryTestItemTreeInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ShowAllFeatureChildrenRequest.

        :param body: The body of this ShowAllFeatureChildrenRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.QueryTestItemTreeInfo`
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
        if not isinstance(other, ShowAllFeatureChildrenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
