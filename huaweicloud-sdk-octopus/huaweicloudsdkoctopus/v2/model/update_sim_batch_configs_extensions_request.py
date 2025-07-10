# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSimBatchConfigsExtensionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'batch_config_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'batch_config_id': 'batch_config_id'
    }

    def __init__(self, id=None, batch_config_id=None):
        r"""UpdateSimBatchConfigsExtensionsRequest

        The model defined in huaweicloud sdk

        :param id: A unique integer value identifying this extension.
        :type id: int
        :param batch_config_id: 
        :type batch_config_id: str
        """
        
        

        self._id = None
        self._batch_config_id = None
        self.discriminator = None

        self.id = id
        self.batch_config_id = batch_config_id

    @property
    def id(self):
        r"""Gets the id of this UpdateSimBatchConfigsExtensionsRequest.

        A unique integer value identifying this extension.

        :return: The id of this UpdateSimBatchConfigsExtensionsRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSimBatchConfigsExtensionsRequest.

        A unique integer value identifying this extension.

        :param id: The id of this UpdateSimBatchConfigsExtensionsRequest.
        :type id: int
        """
        self._id = id

    @property
    def batch_config_id(self):
        r"""Gets the batch_config_id of this UpdateSimBatchConfigsExtensionsRequest.

        :return: The batch_config_id of this UpdateSimBatchConfigsExtensionsRequest.
        :rtype: str
        """
        return self._batch_config_id

    @batch_config_id.setter
    def batch_config_id(self, batch_config_id):
        r"""Sets the batch_config_id of this UpdateSimBatchConfigsExtensionsRequest.

        :param batch_config_id: The batch_config_id of this UpdateSimBatchConfigsExtensionsRequest.
        :type batch_config_id: str
        """
        self._batch_config_id = batch_config_id

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
        if not isinstance(other, UpdateSimBatchConfigsExtensionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
