# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceConfigCommon:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'frame_interval': 'int',
        'categories': 'str',
        'text_categories': 'str',
        'use_sis': 'str',
        'use_ocr': 'str',
        'upload': 'str'
    }

    attribute_map = {
        'frame_interval': 'frame_interval',
        'categories': 'categories',
        'text_categories': 'text_categories',
        'use_sis': 'use_sis',
        'use_ocr': 'use_ocr',
        'upload': 'upload'
    }

    def __init__(self, frame_interval=None, categories=None, text_categories=None, use_sis=None, use_ocr=None, upload=None):
        """ServiceConfigCommon

        The model defined in huaweicloud sdk

        :param frame_interval: 截帧时间间隔，单位为秒/帧。 
        :type frame_interval: int
        :param categories: 视频检测场景。  politics：政治人物的检测。 terrorism：暴恐元素的检测。 porn：涉黄内容元素的检测。 可通过配置上述场景，来完成对应场景元素的检测。  说明： 如需配置多个检测场景，则将多个场景名称使用英文半角逗号拼接。例如，\&quot;categories\&quot;: \&quot;politics,terrorism,porn\&quot; 
        :type categories: str
        :param text_categories: 语音或文字审核服务的检测场景，目前主要支持以下几种：  politics：政治人物的检测。 porn：涉黄内容元素的检测。 ad：广告的检测。 abuse：辱骂内容元素的检测。 contraband：违禁品的检测 flood：灌水内容元素的检测。 当使用语音或文字检测服务时，这里应当设置出对应的场景。  说明： 如需配置多个检测场景，则将多个场景名称使用英文半角逗号拼接。例如，\&quot;text_categories\&quot;: \&quot;politics,porn\&quot;。 
        :type text_categories: str
        :param use_sis: 是否使用语音审核服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。 
        :type use_sis: str
        :param use_ocr: 是否使用文字审核服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。 
        :type use_ocr: str
        :param upload: 是否使用问题场景图片上传服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。  当使用该服务时，必须设置obs输出目录，否则图片无法上传。问题图片会自动上传至输出路径/task_id目录下。 
        :type upload: str
        """
        
        

        self._frame_interval = None
        self._categories = None
        self._text_categories = None
        self._use_sis = None
        self._use_ocr = None
        self._upload = None
        self.discriminator = None

        if frame_interval is not None:
            self.frame_interval = frame_interval
        if categories is not None:
            self.categories = categories
        if text_categories is not None:
            self.text_categories = text_categories
        if use_sis is not None:
            self.use_sis = use_sis
        if use_ocr is not None:
            self.use_ocr = use_ocr
        if upload is not None:
            self.upload = upload

    @property
    def frame_interval(self):
        """Gets the frame_interval of this ServiceConfigCommon.

        截帧时间间隔，单位为秒/帧。 

        :return: The frame_interval of this ServiceConfigCommon.
        :rtype: int
        """
        return self._frame_interval

    @frame_interval.setter
    def frame_interval(self, frame_interval):
        """Sets the frame_interval of this ServiceConfigCommon.

        截帧时间间隔，单位为秒/帧。 

        :param frame_interval: The frame_interval of this ServiceConfigCommon.
        :type frame_interval: int
        """
        self._frame_interval = frame_interval

    @property
    def categories(self):
        """Gets the categories of this ServiceConfigCommon.

        视频检测场景。  politics：政治人物的检测。 terrorism：暴恐元素的检测。 porn：涉黄内容元素的检测。 可通过配置上述场景，来完成对应场景元素的检测。  说明： 如需配置多个检测场景，则将多个场景名称使用英文半角逗号拼接。例如，\"categories\": \"politics,terrorism,porn\" 

        :return: The categories of this ServiceConfigCommon.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ServiceConfigCommon.

        视频检测场景。  politics：政治人物的检测。 terrorism：暴恐元素的检测。 porn：涉黄内容元素的检测。 可通过配置上述场景，来完成对应场景元素的检测。  说明： 如需配置多个检测场景，则将多个场景名称使用英文半角逗号拼接。例如，\"categories\": \"politics,terrorism,porn\" 

        :param categories: The categories of this ServiceConfigCommon.
        :type categories: str
        """
        self._categories = categories

    @property
    def text_categories(self):
        """Gets the text_categories of this ServiceConfigCommon.

        语音或文字审核服务的检测场景，目前主要支持以下几种：  politics：政治人物的检测。 porn：涉黄内容元素的检测。 ad：广告的检测。 abuse：辱骂内容元素的检测。 contraband：违禁品的检测 flood：灌水内容元素的检测。 当使用语音或文字检测服务时，这里应当设置出对应的场景。  说明： 如需配置多个检测场景，则将多个场景名称使用英文半角逗号拼接。例如，\"text_categories\": \"politics,porn\"。 

        :return: The text_categories of this ServiceConfigCommon.
        :rtype: str
        """
        return self._text_categories

    @text_categories.setter
    def text_categories(self, text_categories):
        """Sets the text_categories of this ServiceConfigCommon.

        语音或文字审核服务的检测场景，目前主要支持以下几种：  politics：政治人物的检测。 porn：涉黄内容元素的检测。 ad：广告的检测。 abuse：辱骂内容元素的检测。 contraband：违禁品的检测 flood：灌水内容元素的检测。 当使用语音或文字检测服务时，这里应当设置出对应的场景。  说明： 如需配置多个检测场景，则将多个场景名称使用英文半角逗号拼接。例如，\"text_categories\": \"politics,porn\"。 

        :param text_categories: The text_categories of this ServiceConfigCommon.
        :type text_categories: str
        """
        self._text_categories = text_categories

    @property
    def use_sis(self):
        """Gets the use_sis of this ServiceConfigCommon.

        是否使用语音审核服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。 

        :return: The use_sis of this ServiceConfigCommon.
        :rtype: str
        """
        return self._use_sis

    @use_sis.setter
    def use_sis(self, use_sis):
        """Sets the use_sis of this ServiceConfigCommon.

        是否使用语音审核服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。 

        :param use_sis: The use_sis of this ServiceConfigCommon.
        :type use_sis: str
        """
        self._use_sis = use_sis

    @property
    def use_ocr(self):
        """Gets the use_ocr of this ServiceConfigCommon.

        是否使用文字审核服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。 

        :return: The use_ocr of this ServiceConfigCommon.
        :rtype: str
        """
        return self._use_ocr

    @use_ocr.setter
    def use_ocr(self, use_ocr):
        """Sets the use_ocr of this ServiceConfigCommon.

        是否使用文字审核服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。 

        :param use_ocr: The use_ocr of this ServiceConfigCommon.
        :type use_ocr: str
        """
        self._use_ocr = use_ocr

    @property
    def upload(self):
        """Gets the upload of this ServiceConfigCommon.

        是否使用问题场景图片上传服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。  当使用该服务时，必须设置obs输出目录，否则图片无法上传。问题图片会自动上传至输出路径/task_id目录下。 

        :return: The upload of this ServiceConfigCommon.
        :rtype: str
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this ServiceConfigCommon.

        是否使用问题场景图片上传服务。  true：使用 false：不使用 当不设置该参数或参数为空时，默认为不使用。  当使用该服务时，必须设置obs输出目录，否则图片无法上传。问题图片会自动上传至输出路径/task_id目录下。 

        :param upload: The upload of this ServiceConfigCommon.
        :type upload: str
        """
        self._upload = upload

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
        if not isinstance(other, ServiceConfigCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
