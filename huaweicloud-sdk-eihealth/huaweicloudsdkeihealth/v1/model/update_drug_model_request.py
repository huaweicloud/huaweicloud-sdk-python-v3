# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDrugModelRequest:

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
        'body': 'UpdateDrugModelReq'
    }

    attribute_map = {
        'model_id': 'model_id',
        'body': 'body'
    }

    def __init__(self, model_id=None, body=None):
        r"""UpdateDrugModelRequest

        The model defined in huaweicloud sdk

        :param model_id: 模型id
        :type model_id: str
        :param body: Body of the UpdateDrugModelRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelReq`
        """
        
        

        self._model_id = None
        self._body = None
        self.discriminator = None

        self.model_id = model_id
        if body is not None:
            self.body = body

    @property
    def model_id(self):
        r"""Gets the model_id of this UpdateDrugModelRequest.

        模型id

        :return: The model_id of this UpdateDrugModelRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this UpdateDrugModelRequest.

        模型id

        :param model_id: The model_id of this UpdateDrugModelRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def body(self):
        r"""Gets the body of this UpdateDrugModelRequest.

        :return: The body of this UpdateDrugModelRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateDrugModelRequest.

        :param body: The body of this UpdateDrugModelRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.UpdateDrugModelReq`
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
        if not isinstance(other, UpdateDrugModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
