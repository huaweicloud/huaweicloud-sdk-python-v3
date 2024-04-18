# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Create2dModelTrainingJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'contact': 'str',
        'command_message': 'str',
        'video_multipart_count': 'int',
        'is_background_replacement': 'bool',
        'batch_name': 'str',
        'tags': 'list[str]',
        'model_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'contact': 'contact',
        'command_message': 'command_message',
        'video_multipart_count': 'video_multipart_count',
        'is_background_replacement': 'is_background_replacement',
        'batch_name': 'batch_name',
        'tags': 'tags',
        'model_version': 'model_version'
    }

    def __init__(self, name=None, contact=None, command_message=None, video_multipart_count=None, is_background_replacement=None, batch_name=None, tags=None, model_version=None):
        """Create2dModelTrainingJobReq

        The model defined in huaweicloud sdk

        :param name: 分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。
        :type name: str
        :param contact: 分身数字人训练任务创建者联系方式，如手机或邮箱等。
        :type contact: str
        :param command_message: 命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO：上传视频
        :type command_message: str
        :param video_multipart_count: 训练视频上传分片数。
        :type video_multipart_count: int
        :param is_background_replacement: 分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。
        :type is_background_replacement: bool
        :param batch_name: 分身数字人训练任务的批次名称。
        :type batch_name: str
        :param tags: 分身数字人训练任务标签。
        :type tags: list[str]
        :param model_version: 分身数字人模型版本。默认是V3版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3.2：V3.2版本模型 &gt; * V2版本已废弃不用
        :type model_version: str
        """
        
        

        self._name = None
        self._contact = None
        self._command_message = None
        self._video_multipart_count = None
        self._is_background_replacement = None
        self._batch_name = None
        self._tags = None
        self._model_version = None
        self.discriminator = None

        self.name = name
        if contact is not None:
            self.contact = contact
        if command_message is not None:
            self.command_message = command_message
        if video_multipart_count is not None:
            self.video_multipart_count = video_multipart_count
        if is_background_replacement is not None:
            self.is_background_replacement = is_background_replacement
        if batch_name is not None:
            self.batch_name = batch_name
        if tags is not None:
            self.tags = tags
        if model_version is not None:
            self.model_version = model_version

    @property
    def name(self):
        """Gets the name of this Create2dModelTrainingJobReq.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :return: The name of this Create2dModelTrainingJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Create2dModelTrainingJobReq.

        分身数字人模型名称。该名称会作为资产库中分身数字人模型资产名称。

        :param name: The name of this Create2dModelTrainingJobReq.
        :type name: str
        """
        self._name = name

    @property
    def contact(self):
        """Gets the contact of this Create2dModelTrainingJobReq.

        分身数字人训练任务创建者联系方式，如手机或邮箱等。

        :return: The contact of this Create2dModelTrainingJobReq.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Create2dModelTrainingJobReq.

        分身数字人训练任务创建者联系方式，如手机或邮箱等。

        :param contact: The contact of this Create2dModelTrainingJobReq.
        :type contact: str
        """
        self._contact = contact

    @property
    def command_message(self):
        """Gets the command_message of this Create2dModelTrainingJobReq.

        命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO：上传视频

        :return: The command_message of this Create2dModelTrainingJobReq.
        :rtype: str
        """
        return self._command_message

    @command_message.setter
    def command_message(self, command_message):
        """Sets the command_message of this Create2dModelTrainingJobReq.

        命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO：上传视频

        :param command_message: The command_message of this Create2dModelTrainingJobReq.
        :type command_message: str
        """
        self._command_message = command_message

    @property
    def video_multipart_count(self):
        """Gets the video_multipart_count of this Create2dModelTrainingJobReq.

        训练视频上传分片数。

        :return: The video_multipart_count of this Create2dModelTrainingJobReq.
        :rtype: int
        """
        return self._video_multipart_count

    @video_multipart_count.setter
    def video_multipart_count(self, video_multipart_count):
        """Sets the video_multipart_count of this Create2dModelTrainingJobReq.

        训练视频上传分片数。

        :param video_multipart_count: The video_multipart_count of this Create2dModelTrainingJobReq.
        :type video_multipart_count: int
        """
        self._video_multipart_count = video_multipart_count

    @property
    def is_background_replacement(self):
        """Gets the is_background_replacement of this Create2dModelTrainingJobReq.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :return: The is_background_replacement of this Create2dModelTrainingJobReq.
        :rtype: bool
        """
        return self._is_background_replacement

    @is_background_replacement.setter
    def is_background_replacement(self, is_background_replacement):
        """Sets the is_background_replacement of this Create2dModelTrainingJobReq.

        分身数字人是否需要背景替换。需要背景替换的分身数字人训练视频需要绿幕拍摄。

        :param is_background_replacement: The is_background_replacement of this Create2dModelTrainingJobReq.
        :type is_background_replacement: bool
        """
        self._is_background_replacement = is_background_replacement

    @property
    def batch_name(self):
        """Gets the batch_name of this Create2dModelTrainingJobReq.

        分身数字人训练任务的批次名称。

        :return: The batch_name of this Create2dModelTrainingJobReq.
        :rtype: str
        """
        return self._batch_name

    @batch_name.setter
    def batch_name(self, batch_name):
        """Sets the batch_name of this Create2dModelTrainingJobReq.

        分身数字人训练任务的批次名称。

        :param batch_name: The batch_name of this Create2dModelTrainingJobReq.
        :type batch_name: str
        """
        self._batch_name = batch_name

    @property
    def tags(self):
        """Gets the tags of this Create2dModelTrainingJobReq.

        分身数字人训练任务标签。

        :return: The tags of this Create2dModelTrainingJobReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Create2dModelTrainingJobReq.

        分身数字人训练任务标签。

        :param tags: The tags of this Create2dModelTrainingJobReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def model_version(self):
        """Gets the model_version of this Create2dModelTrainingJobReq.

        分身数字人模型版本。默认是V3版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3.2：V3.2版本模型 > * V2版本已废弃不用

        :return: The model_version of this Create2dModelTrainingJobReq.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """Sets the model_version of this Create2dModelTrainingJobReq.

        分身数字人模型版本。默认是V3版本模型。 * V2: V2版本模型 * V3：V3版本模型 * V3.2：V3.2版本模型 > * V2版本已废弃不用

        :param model_version: The model_version of this Create2dModelTrainingJobReq.
        :type model_version: str
        """
        self._model_version = model_version

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
        if not isinstance(other, Create2dModelTrainingJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
