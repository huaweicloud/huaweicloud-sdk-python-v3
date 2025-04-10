# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_url': 'str'
    }

    attribute_map = {
        'image_url': 'image_url'
    }

    def __init__(self, image_url=None):
        r"""RegisterImageRequestBody

        The model defined in huaweicloud sdk

        :param image_url: 源镜像的URL，格式：&lt;bucket&gt;:&lt;file&gt; image_url对应的镜像桶中的文件，镜像文件格式的取值范围为：ZVHD、QCOW2、VHD、RAW、VHDX、QED、VDI、QCOW、ZVHD2、VMDK。
        :type image_url: str
        """
        
        

        self._image_url = None
        self.discriminator = None

        self.image_url = image_url

    @property
    def image_url(self):
        r"""Gets the image_url of this RegisterImageRequestBody.

        源镜像的URL，格式：<bucket>:<file> image_url对应的镜像桶中的文件，镜像文件格式的取值范围为：ZVHD、QCOW2、VHD、RAW、VHDX、QED、VDI、QCOW、ZVHD2、VMDK。

        :return: The image_url of this RegisterImageRequestBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this RegisterImageRequestBody.

        源镜像的URL，格式：<bucket>:<file> image_url对应的镜像桶中的文件，镜像文件格式的取值范围为：ZVHD、QCOW2、VHD、RAW、VHDX、QED、VDI、QCOW、ZVHD2、VMDK。

        :param image_url: The image_url of this RegisterImageRequestBody.
        :type image_url: str
        """
        self._image_url = image_url

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
        if not isinstance(other, RegisterImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
