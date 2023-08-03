# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePictureModelingJobRequestBody:

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
        'style_id': 'str',
        'name': 'str',
        'notify_url': 'str'
    }

    attribute_map = {
        'file': 'file',
        'style_id': 'style_id',
        'name': 'name',
        'notify_url': 'notify_url'
    }

    def __init__(self, file=None, style_id=None, name=None, notify_url=None):
        """CreatePictureModelingJobRequestBody

        The model defined in huaweicloud sdk

        :param file: 照片文件。 &gt; 只能上传jpg/jpeg/png格式文件， 最大分辨率为3840*2160
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param style_id: 数字人风格ID。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02 * system_female_002：女性风格02
        :type style_id: str
        :param name: 数字人模型名称，首次创建时使用。
        :type name: str
        :param notify_url: 照片建模任务结束的回调地址。
        :type notify_url: str
        """
        
        

        self._file = None
        self._style_id = None
        self._name = None
        self._notify_url = None
        self.discriminator = None

        self.file = file
        self.style_id = style_id
        self.name = name
        if notify_url is not None:
            self.notify_url = notify_url

    @property
    def file(self):
        """Gets the file of this CreatePictureModelingJobRequestBody.

        照片文件。 > 只能上传jpg/jpeg/png格式文件， 最大分辨率为3840*2160

        :return: The file of this CreatePictureModelingJobRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreatePictureModelingJobRequestBody.

        照片文件。 > 只能上传jpg/jpeg/png格式文件， 最大分辨率为3840*2160

        :param file: The file of this CreatePictureModelingJobRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def style_id(self):
        """Gets the style_id of this CreatePictureModelingJobRequestBody.

        数字人风格ID。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02 * system_female_002：女性风格02

        :return: The style_id of this CreatePictureModelingJobRequestBody.
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this CreatePictureModelingJobRequestBody.

        数字人风格ID。 * system_male_001：男性风格01 * system_female_001：女性风格01 * system_male_002：男性风格02 * system_female_002：女性风格02

        :param style_id: The style_id of this CreatePictureModelingJobRequestBody.
        :type style_id: str
        """
        self._style_id = style_id

    @property
    def name(self):
        """Gets the name of this CreatePictureModelingJobRequestBody.

        数字人模型名称，首次创建时使用。

        :return: The name of this CreatePictureModelingJobRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePictureModelingJobRequestBody.

        数字人模型名称，首次创建时使用。

        :param name: The name of this CreatePictureModelingJobRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def notify_url(self):
        """Gets the notify_url of this CreatePictureModelingJobRequestBody.

        照片建模任务结束的回调地址。

        :return: The notify_url of this CreatePictureModelingJobRequestBody.
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this CreatePictureModelingJobRequestBody.

        照片建模任务结束的回调地址。

        :param notify_url: The notify_url of this CreatePictureModelingJobRequestBody.
        :type notify_url: str
        """
        self._notify_url = notify_url

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
        if not isinstance(other, CreatePictureModelingJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
