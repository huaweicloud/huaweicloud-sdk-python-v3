# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeconfigStatusConfigsStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_warm_up': 'NodeconfigStatusConfigsStatusImageWarmUp'
    }

    attribute_map = {
        'image_warm_up': 'image_warm_up'
    }

    def __init__(self, image_warm_up=None):
        r"""NodeconfigStatusConfigsStatus

        The model defined in huaweicloud sdk

        :param image_warm_up: 
        :type image_warm_up: :class:`huaweicloudsdkmodelarts.v1.NodeconfigStatusConfigsStatusImageWarmUp`
        """
        
        

        self._image_warm_up = None
        self.discriminator = None

        if image_warm_up is not None:
            self.image_warm_up = image_warm_up

    @property
    def image_warm_up(self):
        r"""Gets the image_warm_up of this NodeconfigStatusConfigsStatus.

        :return: The image_warm_up of this NodeconfigStatusConfigsStatus.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeconfigStatusConfigsStatusImageWarmUp`
        """
        return self._image_warm_up

    @image_warm_up.setter
    def image_warm_up(self, image_warm_up):
        r"""Sets the image_warm_up of this NodeconfigStatusConfigsStatus.

        :param image_warm_up: The image_warm_up of this NodeconfigStatusConfigsStatus.
        :type image_warm_up: :class:`huaweicloudsdkmodelarts.v1.NodeconfigStatusConfigsStatusImageWarmUp`
        """
        self._image_warm_up = image_warm_up

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeconfigStatusConfigsStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
