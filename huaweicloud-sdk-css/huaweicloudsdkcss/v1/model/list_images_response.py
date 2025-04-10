# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'need_upload_upgrade_plugin': 'bool',
        'image_info_list': 'list[GetTargetImageIdDetail]'
    }

    attribute_map = {
        'need_upload_upgrade_plugin': 'needUploadUpgradePlugin',
        'image_info_list': 'imageInfoList'
    }

    def __init__(self, need_upload_upgrade_plugin=None, image_info_list=None):
        r"""ListImagesResponse

        The model defined in huaweicloud sdk

        :param need_upload_upgrade_plugin: 是否需要上传升级后版本的插件。
        :type need_upload_upgrade_plugin: bool
        :param image_info_list: 
        :type image_info_list: list[:class:`huaweicloudsdkcss.v1.GetTargetImageIdDetail`]
        """
        
        super(ListImagesResponse, self).__init__()

        self._need_upload_upgrade_plugin = None
        self._image_info_list = None
        self.discriminator = None

        if need_upload_upgrade_plugin is not None:
            self.need_upload_upgrade_plugin = need_upload_upgrade_plugin
        if image_info_list is not None:
            self.image_info_list = image_info_list

    @property
    def need_upload_upgrade_plugin(self):
        r"""Gets the need_upload_upgrade_plugin of this ListImagesResponse.

        是否需要上传升级后版本的插件。

        :return: The need_upload_upgrade_plugin of this ListImagesResponse.
        :rtype: bool
        """
        return self._need_upload_upgrade_plugin

    @need_upload_upgrade_plugin.setter
    def need_upload_upgrade_plugin(self, need_upload_upgrade_plugin):
        r"""Sets the need_upload_upgrade_plugin of this ListImagesResponse.

        是否需要上传升级后版本的插件。

        :param need_upload_upgrade_plugin: The need_upload_upgrade_plugin of this ListImagesResponse.
        :type need_upload_upgrade_plugin: bool
        """
        self._need_upload_upgrade_plugin = need_upload_upgrade_plugin

    @property
    def image_info_list(self):
        r"""Gets the image_info_list of this ListImagesResponse.

        :return: The image_info_list of this ListImagesResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.GetTargetImageIdDetail`]
        """
        return self._image_info_list

    @image_info_list.setter
    def image_info_list(self, image_info_list):
        r"""Sets the image_info_list of this ListImagesResponse.

        :param image_info_list: The image_info_list of this ListImagesResponse.
        :type image_info_list: list[:class:`huaweicloudsdkcss.v1.GetTargetImageIdDetail`]
        """
        self._image_info_list = image_info_list

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
        if not isinstance(other, ListImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
