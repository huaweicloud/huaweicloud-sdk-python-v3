# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bridge_id': 'str',
        'classification_id': 'str'
    }

    attribute_map = {
        'bridge_id': 'bridge_id',
        'classification_id': 'classification_id'
    }

    def __init__(self, bridge_id=None, classification_id=None):
        r"""JobLogRequest

        The model defined in huaweicloud sdk

        :param bridge_id: 桥接作业id
        :type bridge_id: str
        :param classification_id: 分类作业id
        :type classification_id: str
        """
        
        

        self._bridge_id = None
        self._classification_id = None
        self.discriminator = None

        self.bridge_id = bridge_id
        if classification_id is not None:
            self.classification_id = classification_id

    @property
    def bridge_id(self):
        r"""Gets the bridge_id of this JobLogRequest.

        桥接作业id

        :return: The bridge_id of this JobLogRequest.
        :rtype: str
        """
        return self._bridge_id

    @bridge_id.setter
    def bridge_id(self, bridge_id):
        r"""Sets the bridge_id of this JobLogRequest.

        桥接作业id

        :param bridge_id: The bridge_id of this JobLogRequest.
        :type bridge_id: str
        """
        self._bridge_id = bridge_id

    @property
    def classification_id(self):
        r"""Gets the classification_id of this JobLogRequest.

        分类作业id

        :return: The classification_id of this JobLogRequest.
        :rtype: str
        """
        return self._classification_id

    @classification_id.setter
    def classification_id(self, classification_id):
        r"""Sets the classification_id of this JobLogRequest.

        分类作业id

        :param classification_id: The classification_id of this JobLogRequest.
        :type classification_id: str
        """
        self._classification_id = classification_id

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
        if not isinstance(other, JobLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
