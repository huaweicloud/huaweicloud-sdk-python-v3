# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadMediaRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'file_type': 'str'
    }

    attribute_map = {
        'file': 'file',
        'file_type': 'file_type'
    }

    def __init__(self, file=None, file_type=None):
        """UploadMediaRequestBody

        The model defined in huaweicloud sdk

        :param file: 图片资源。  &gt; 文件格式与文件名后缀需保持一致，请勿修改原始文件后缀，否则导致资源上传失败。 
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param file_type: 文件类型。 - PUB_LOGO：上传服务号LOGO。支持jpg、bmp、png和jpeg格式，分辨率大于等于240*240且比例为1:1，大小不超过4M。 - BG_IMAGE：上传服务号主页背景图。分辨率大于等于1440*810。 - FASTAPP_LOGO：上传快应用LOGO。上传快应用LOGO。支持jpg、bmp和jpeg格式，分辨率大于等于192*192，大小不超过4M。 - OTHER：上传授权证明和营业执照等 
        :type file_type: str
        """
        
        

        self._file = None
        self._file_type = None
        self.discriminator = None

        self.file = file
        self.file_type = file_type

    @property
    def file(self):
        """Gets the file of this UploadMediaRequestBody.

        图片资源。  > 文件格式与文件名后缀需保持一致，请勿修改原始文件后缀，否则导致资源上传失败。 

        :return: The file of this UploadMediaRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UploadMediaRequestBody.

        图片资源。  > 文件格式与文件名后缀需保持一致，请勿修改原始文件后缀，否则导致资源上传失败。 

        :param file: The file of this UploadMediaRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def file_type(self):
        """Gets the file_type of this UploadMediaRequestBody.

        文件类型。 - PUB_LOGO：上传服务号LOGO。支持jpg、bmp、png和jpeg格式，分辨率大于等于240*240且比例为1:1，大小不超过4M。 - BG_IMAGE：上传服务号主页背景图。分辨率大于等于1440*810。 - FASTAPP_LOGO：上传快应用LOGO。上传快应用LOGO。支持jpg、bmp和jpeg格式，分辨率大于等于192*192，大小不超过4M。 - OTHER：上传授权证明和营业执照等 

        :return: The file_type of this UploadMediaRequestBody.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this UploadMediaRequestBody.

        文件类型。 - PUB_LOGO：上传服务号LOGO。支持jpg、bmp、png和jpeg格式，分辨率大于等于240*240且比例为1:1，大小不超过4M。 - BG_IMAGE：上传服务号主页背景图。分辨率大于等于1440*810。 - FASTAPP_LOGO：上传快应用LOGO。上传快应用LOGO。支持jpg、bmp和jpeg格式，分辨率大于等于192*192，大小不超过4M。 - OTHER：上传授权证明和营业执照等 

        :param file_type: The file_type of this UploadMediaRequestBody.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, UploadMediaRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
