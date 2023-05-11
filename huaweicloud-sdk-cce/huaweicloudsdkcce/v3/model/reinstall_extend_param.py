# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alpha_cce_node_image_id': 'str'
    }

    attribute_map = {
        'alpha_cce_node_image_id': 'alpha.cce/NodeImageID'
    }

    def __init__(self, alpha_cce_node_image_id=None):
        """ReinstallExtendParam

        The model defined in huaweicloud sdk

        :param alpha_cce_node_image_id: 指定待切换目标操作系统所使用的用户镜像ID，已废弃。 指定此参数等价于指定ReinstallVolumeSpec中imageID，原取值将被覆盖。 
        :type alpha_cce_node_image_id: str
        """
        
        

        self._alpha_cce_node_image_id = None
        self.discriminator = None

        if alpha_cce_node_image_id is not None:
            self.alpha_cce_node_image_id = alpha_cce_node_image_id

    @property
    def alpha_cce_node_image_id(self):
        """Gets the alpha_cce_node_image_id of this ReinstallExtendParam.

        指定待切换目标操作系统所使用的用户镜像ID，已废弃。 指定此参数等价于指定ReinstallVolumeSpec中imageID，原取值将被覆盖。 

        :return: The alpha_cce_node_image_id of this ReinstallExtendParam.
        :rtype: str
        """
        return self._alpha_cce_node_image_id

    @alpha_cce_node_image_id.setter
    def alpha_cce_node_image_id(self, alpha_cce_node_image_id):
        """Sets the alpha_cce_node_image_id of this ReinstallExtendParam.

        指定待切换目标操作系统所使用的用户镜像ID，已废弃。 指定此参数等价于指定ReinstallVolumeSpec中imageID，原取值将被覆盖。 

        :param alpha_cce_node_image_id: The alpha_cce_node_image_id of this ReinstallExtendParam.
        :type alpha_cce_node_image_id: str
        """
        self._alpha_cce_node_image_id = alpha_cce_node_image_id

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
        if not isinstance(other, ReinstallExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
