# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEditingJobReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'edit_type': 'list[str]',
        'clips': 'list[ClipInfo]',
        'contcat': 'ConcatInfo',
        'output_setting': 'OutputSetting',
        'image_watermark_settings': 'list[ImageWatermarkSetting]',
        'user_data': 'str'
    }

    attribute_map = {
        'edit_type': 'edit_type',
        'clips': 'clips',
        'contcat': 'contcat',
        'output_setting': 'output_setting',
        'image_watermark_settings': 'image_watermark_settings',
        'user_data': 'user_data'
    }

    def __init__(self, edit_type=None, clips=None, contcat=None, output_setting=None, image_watermark_settings=None, user_data=None):
        """CreateEditingJobReq - a model defined in huaweicloud sdk"""
        
        

        self._edit_type = None
        self._clips = None
        self._contcat = None
        self._output_setting = None
        self._image_watermark_settings = None
        self._user_data = None
        self.discriminator = None

        if edit_type is not None:
            self.edit_type = edit_type
        if clips is not None:
            self.clips = clips
        if contcat is not None:
            self.contcat = contcat
        if output_setting is not None:
            self.output_setting = output_setting
        if image_watermark_settings is not None:
            self.image_watermark_settings = image_watermark_settings
        if user_data is not None:
            self.user_data = user_data

    @property
    def edit_type(self):
        """Gets the edit_type of this CreateEditingJobReq.

        剪辑任务类型。取值如下：\"CLIP\",\"CONCAT\"。

        :return: The edit_type of this CreateEditingJobReq.
        :rtype: list[str]
        """
        return self._edit_type

    @edit_type.setter
    def edit_type(self, edit_type):
        """Sets the edit_type of this CreateEditingJobReq.

        剪辑任务类型。取值如下：\"CLIP\",\"CONCAT\"。

        :param edit_type: The edit_type of this CreateEditingJobReq.
        :type: list[str]
        """
        self._edit_type = edit_type

    @property
    def clips(self):
        """Gets the clips of this CreateEditingJobReq.

        剪切信息

        :return: The clips of this CreateEditingJobReq.
        :rtype: list[ClipInfo]
        """
        return self._clips

    @clips.setter
    def clips(self, clips):
        """Sets the clips of this CreateEditingJobReq.

        剪切信息

        :param clips: The clips of this CreateEditingJobReq.
        :type: list[ClipInfo]
        """
        self._clips = clips

    @property
    def contcat(self):
        """Gets the contcat of this CreateEditingJobReq.


        :return: The contcat of this CreateEditingJobReq.
        :rtype: ConcatInfo
        """
        return self._contcat

    @contcat.setter
    def contcat(self, contcat):
        """Sets the contcat of this CreateEditingJobReq.


        :param contcat: The contcat of this CreateEditingJobReq.
        :type: ConcatInfo
        """
        self._contcat = contcat

    @property
    def output_setting(self):
        """Gets the output_setting of this CreateEditingJobReq.


        :return: The output_setting of this CreateEditingJobReq.
        :rtype: OutputSetting
        """
        return self._output_setting

    @output_setting.setter
    def output_setting(self, output_setting):
        """Sets the output_setting of this CreateEditingJobReq.


        :param output_setting: The output_setting of this CreateEditingJobReq.
        :type: OutputSetting
        """
        self._output_setting = output_setting

    @property
    def image_watermark_settings(self):
        """Gets the image_watermark_settings of this CreateEditingJobReq.

        水印信息。

        :return: The image_watermark_settings of this CreateEditingJobReq.
        :rtype: list[ImageWatermarkSetting]
        """
        return self._image_watermark_settings

    @image_watermark_settings.setter
    def image_watermark_settings(self, image_watermark_settings):
        """Sets the image_watermark_settings of this CreateEditingJobReq.

        水印信息。

        :param image_watermark_settings: The image_watermark_settings of this CreateEditingJobReq.
        :type: list[ImageWatermarkSetting]
        """
        self._image_watermark_settings = image_watermark_settings

    @property
    def user_data(self):
        """Gets the user_data of this CreateEditingJobReq.

        用户自定义数据。

        :return: The user_data of this CreateEditingJobReq.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateEditingJobReq.

        用户自定义数据。

        :param user_data: The user_data of this CreateEditingJobReq.
        :type: str
        """
        self._user_data = user_data

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
        if not isinstance(other, CreateEditingJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
