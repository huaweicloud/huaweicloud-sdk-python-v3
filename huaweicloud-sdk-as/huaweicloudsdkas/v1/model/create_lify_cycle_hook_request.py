# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLifyCycleHookRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'body': 'CreateLifeCycleHookOption'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'body': 'body'
    }

    def __init__(self, scaling_group_id=None, body=None):
        r"""CreateLifyCycleHookRequest

        The model defined in huaweicloud sdk

        :param scaling_group_id: 伸缩组标识。
        :type scaling_group_id: str
        :param body: Body of the CreateLifyCycleHookRequest
        :type body: :class:`huaweicloudsdkas.v1.CreateLifeCycleHookOption`
        """
        
        

        self._scaling_group_id = None
        self._body = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        if body is not None:
            self.body = body

    @property
    def scaling_group_id(self):
        r"""Gets the scaling_group_id of this CreateLifyCycleHookRequest.

        伸缩组标识。

        :return: The scaling_group_id of this CreateLifyCycleHookRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        r"""Sets the scaling_group_id of this CreateLifyCycleHookRequest.

        伸缩组标识。

        :param scaling_group_id: The scaling_group_id of this CreateLifyCycleHookRequest.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def body(self):
        r"""Gets the body of this CreateLifyCycleHookRequest.

        :return: The body of this CreateLifyCycleHookRequest.
        :rtype: :class:`huaweicloudsdkas.v1.CreateLifeCycleHookOption`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateLifyCycleHookRequest.

        :param body: The body of this CreateLifyCycleHookRequest.
        :type body: :class:`huaweicloudsdkas.v1.CreateLifeCycleHookOption`
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
        if not isinstance(other, CreateLifyCycleHookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
