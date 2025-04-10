# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutPutInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_info': 'OutPutResult',
        'package_infos': 'dict(str, OutPutResult)',
        'image_infos': 'dict(str, OutPutResult)'
    }

    attribute_map = {
        'package_info': 'package_info',
        'package_infos': 'package_infos',
        'image_infos': 'image_infos'
    }

    def __init__(self, package_info=None, package_infos=None, image_infos=None):
        r"""OutPutInfoResult

        The model defined in huaweicloud sdk

        :param package_info: 
        :type package_info: :class:`huaweicloudsdkcodeartsbuild.v3.OutPutResult`
        :param package_infos: 二方包信息
        :type package_infos: dict(str, OutPutResult)
        :param image_infos: 镜像包信息
        :type image_infos: dict(str, OutPutResult)
        """
        
        

        self._package_info = None
        self._package_infos = None
        self._image_infos = None
        self.discriminator = None

        if package_info is not None:
            self.package_info = package_info
        if package_infos is not None:
            self.package_infos = package_infos
        if image_infos is not None:
            self.image_infos = image_infos

    @property
    def package_info(self):
        r"""Gets the package_info of this OutPutInfoResult.

        :return: The package_info of this OutPutInfoResult.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.OutPutResult`
        """
        return self._package_info

    @package_info.setter
    def package_info(self, package_info):
        r"""Sets the package_info of this OutPutInfoResult.

        :param package_info: The package_info of this OutPutInfoResult.
        :type package_info: :class:`huaweicloudsdkcodeartsbuild.v3.OutPutResult`
        """
        self._package_info = package_info

    @property
    def package_infos(self):
        r"""Gets the package_infos of this OutPutInfoResult.

        二方包信息

        :return: The package_infos of this OutPutInfoResult.
        :rtype: dict(str, OutPutResult)
        """
        return self._package_infos

    @package_infos.setter
    def package_infos(self, package_infos):
        r"""Sets the package_infos of this OutPutInfoResult.

        二方包信息

        :param package_infos: The package_infos of this OutPutInfoResult.
        :type package_infos: dict(str, OutPutResult)
        """
        self._package_infos = package_infos

    @property
    def image_infos(self):
        r"""Gets the image_infos of this OutPutInfoResult.

        镜像包信息

        :return: The image_infos of this OutPutInfoResult.
        :rtype: dict(str, OutPutResult)
        """
        return self._image_infos

    @image_infos.setter
    def image_infos(self, image_infos):
        r"""Sets the image_infos of this OutPutInfoResult.

        镜像包信息

        :param image_infos: The image_infos of this OutPutInfoResult.
        :type image_infos: dict(str, OutPutResult)
        """
        self._image_infos = image_infos

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
        if not isinstance(other, OutPutInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
