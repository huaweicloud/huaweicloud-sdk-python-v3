# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssetModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'model_id': 'str',
        'body': 'AssetModelModRequest'
    }

    attribute_map = {
        'model_id': 'model_id',
        'body': 'body'
    }

    def __init__(self, model_id=None, body=None):
        """UpdateAssetModelRequest

        The model defined in huaweicloud sdk

        :param model_id: 模型ID
        :type model_id: str
        :param body: Body of the UpdateAssetModelRequest
        :type body: :class:`huaweicloudsdkiotanalytics.v1.AssetModelModRequest`
        """
        
        

        self._model_id = None
        self._body = None
        self.discriminator = None

        self.model_id = model_id
        if body is not None:
            self.body = body

    @property
    def model_id(self):
        """Gets the model_id of this UpdateAssetModelRequest.

        模型ID

        :return: The model_id of this UpdateAssetModelRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this UpdateAssetModelRequest.

        模型ID

        :param model_id: The model_id of this UpdateAssetModelRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def body(self):
        """Gets the body of this UpdateAssetModelRequest.


        :return: The body of this UpdateAssetModelRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AssetModelModRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAssetModelRequest.


        :param body: The body of this UpdateAssetModelRequest.
        :type body: :class:`huaweicloudsdkiotanalytics.v1.AssetModelModRequest`
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
        if not isinstance(other, UpdateAssetModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
