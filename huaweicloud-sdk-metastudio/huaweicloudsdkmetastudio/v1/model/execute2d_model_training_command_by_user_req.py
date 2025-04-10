# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Execute2dModelTrainingCommandByUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'command_message': 'str',
        'comment_data': 'CommentData'
    }

    attribute_map = {
        'command': 'command',
        'command_message': 'command_message',
        'comment_data': 'comment_data'
    }

    def __init__(self, command=None, command_message=None, comment_data=None):
        r"""Execute2dModelTrainingCommandByUserReq

        The model defined in huaweicloud sdk

        :param command: 命令类型。 * SUBMITVERIFYING: 提交审核 * CONFIRM_ACCEPT：用户确认训练效果 * CONFIRM_REJECT：用户驳回训练效果 * CONFIRM_ANSWER：用户答复 * CONFIRM_PENDING：用户挂起任务 * CONFIRM_ACTIVE：用户激活任务 * GET_MULTIPART_UPLOADED：获取训练视频已上传分片信息 * CONFIRM_REPAIR:用户发起优化模型请求 * CONFIRM_MULTIPART_UPLOADED：确认训练视频所有分片文件已上传 * GET_ACTION_VIDEO_MULTIPART_UPLOADED：获取动作编排视频分片上传地址 * CONFIRM_ACTION_VIDEO_MULTIPART_UPLOADED：确认动作编排视频所有分片文件已上传 &gt; * CONFIRM_ACCEPT、CONFIRM_REJECT、CONFIRM_ANSWER、CONFIRM_PENDING、CONFIRM_ACTIVE命令仅NA白名单用户可用。
        :type command: str
        :param command_message: 命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO: 上传视频 * CONFIRM_ACTION_VIDEO: 确认动作编排视频 * GET_ACTION_VIDEO_MULTIPART: 获取动作编排视频分片
        :type command_message: str
        :param comment_data: 
        :type comment_data: :class:`huaweicloudsdkmetastudio.v1.CommentData`
        """
        
        

        self._command = None
        self._command_message = None
        self._comment_data = None
        self.discriminator = None

        self.command = command
        if command_message is not None:
            self.command_message = command_message
        if comment_data is not None:
            self.comment_data = comment_data

    @property
    def command(self):
        r"""Gets the command of this Execute2dModelTrainingCommandByUserReq.

        命令类型。 * SUBMITVERIFYING: 提交审核 * CONFIRM_ACCEPT：用户确认训练效果 * CONFIRM_REJECT：用户驳回训练效果 * CONFIRM_ANSWER：用户答复 * CONFIRM_PENDING：用户挂起任务 * CONFIRM_ACTIVE：用户激活任务 * GET_MULTIPART_UPLOADED：获取训练视频已上传分片信息 * CONFIRM_REPAIR:用户发起优化模型请求 * CONFIRM_MULTIPART_UPLOADED：确认训练视频所有分片文件已上传 * GET_ACTION_VIDEO_MULTIPART_UPLOADED：获取动作编排视频分片上传地址 * CONFIRM_ACTION_VIDEO_MULTIPART_UPLOADED：确认动作编排视频所有分片文件已上传 > * CONFIRM_ACCEPT、CONFIRM_REJECT、CONFIRM_ANSWER、CONFIRM_PENDING、CONFIRM_ACTIVE命令仅NA白名单用户可用。

        :return: The command of this Execute2dModelTrainingCommandByUserReq.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this Execute2dModelTrainingCommandByUserReq.

        命令类型。 * SUBMITVERIFYING: 提交审核 * CONFIRM_ACCEPT：用户确认训练效果 * CONFIRM_REJECT：用户驳回训练效果 * CONFIRM_ANSWER：用户答复 * CONFIRM_PENDING：用户挂起任务 * CONFIRM_ACTIVE：用户激活任务 * GET_MULTIPART_UPLOADED：获取训练视频已上传分片信息 * CONFIRM_REPAIR:用户发起优化模型请求 * CONFIRM_MULTIPART_UPLOADED：确认训练视频所有分片文件已上传 * GET_ACTION_VIDEO_MULTIPART_UPLOADED：获取动作编排视频分片上传地址 * CONFIRM_ACTION_VIDEO_MULTIPART_UPLOADED：确认动作编排视频所有分片文件已上传 > * CONFIRM_ACCEPT、CONFIRM_REJECT、CONFIRM_ANSWER、CONFIRM_PENDING、CONFIRM_ACTIVE命令仅NA白名单用户可用。

        :param command: The command of this Execute2dModelTrainingCommandByUserReq.
        :type command: str
        """
        self._command = command

    @property
    def command_message(self):
        r"""Gets the command_message of this Execute2dModelTrainingCommandByUserReq.

        命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO: 上传视频 * CONFIRM_ACTION_VIDEO: 确认动作编排视频 * GET_ACTION_VIDEO_MULTIPART: 获取动作编排视频分片

        :return: The command_message of this Execute2dModelTrainingCommandByUserReq.
        :rtype: str
        """
        return self._command_message

    @command_message.setter
    def command_message(self, command_message):
        r"""Sets the command_message of this Execute2dModelTrainingCommandByUserReq.

        命令类型： * UPDATE_VIDEO: 更新视频 * UPLOAD_VIDEO: 上传视频 * CONFIRM_ACTION_VIDEO: 确认动作编排视频 * GET_ACTION_VIDEO_MULTIPART: 获取动作编排视频分片

        :param command_message: The command_message of this Execute2dModelTrainingCommandByUserReq.
        :type command_message: str
        """
        self._command_message = command_message

    @property
    def comment_data(self):
        r"""Gets the comment_data of this Execute2dModelTrainingCommandByUserReq.

        :return: The comment_data of this Execute2dModelTrainingCommandByUserReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CommentData`
        """
        return self._comment_data

    @comment_data.setter
    def comment_data(self, comment_data):
        r"""Sets the comment_data of this Execute2dModelTrainingCommandByUserReq.

        :param comment_data: The comment_data of this Execute2dModelTrainingCommandByUserReq.
        :type comment_data: :class:`huaweicloudsdkmetastudio.v1.CommentData`
        """
        self._comment_data = comment_data

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
        if not isinstance(other, Execute2dModelTrainingCommandByUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
