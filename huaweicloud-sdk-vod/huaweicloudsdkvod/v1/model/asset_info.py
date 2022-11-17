# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'status': 'str',
        'description': 'str',
        'base_info': 'BaseInfo',
        'play_info_array': 'list[PlayInfo]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status',
        'description': 'description',
        'base_info': 'base_info',
        'play_info_array': 'play_info_array'
    }

    def __init__(self, asset_id=None, status=None, description=None, base_info=None, play_info_array=None):
        """AssetInfo

        The model defined in huaweicloud sdk

        :param asset_id: 媒资ID。
        :type asset_id: str
        :param status: 媒资状态。  取值如下： - UNCREATED：未创建（媒资ID不存在 ） - DELETED：已删除 - CANCELLED：上传取消 - SERVER_ERROR：上传失败（点播服务端故障） - UPLOAD_FAILED：上传失败（向OBS上传失败） - CREATING：创建中 - PUBLISHED：已发布 - WAITING_TRANSCODE：待发布（转码排队中） - TRANSCODING：待发布（转码中） - TRANSCODE_FAILED：待发布（转码失败） - TRANSCODE_SUCCEED：待发布（转码成功） - CREATED：待发布（未转码） - NO_ASSET：该媒资不存在 - DELETING：正在删除 - DELETE_FAILED：删除失败 - OBS_CREATING：OBS转存方式创建中 - OBS_CREATE_FAILED： OBS转存失败 - OBS_CREATE_SUCCESS： OBS转存成功
        :type status: str
        :param description: 媒资子状态或描述信息。 - 对于媒资异常场景，描述具体的异常原因。 - 对于正常场景，描述媒资的处理信息。
        :type description: str
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkvod.v1.BaseInfo`
        :param play_info_array: 转码文件的播放信息。 - HLS或DASH：此数组的成员个数为n+1，n为转码输出路数。 - MP4：此数组的成员个数为n，n为转码输出路数。
        :type play_info_array: list[:class:`huaweicloudsdkvod.v1.PlayInfo`]
        """
        
        

        self._asset_id = None
        self._status = None
        self._description = None
        self._base_info = None
        self._play_info_array = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if base_info is not None:
            self.base_info = base_info
        if play_info_array is not None:
            self.play_info_array = play_info_array

    @property
    def asset_id(self):
        """Gets the asset_id of this AssetInfo.

        媒资ID。

        :return: The asset_id of this AssetInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AssetInfo.

        媒资ID。

        :param asset_id: The asset_id of this AssetInfo.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        """Gets the status of this AssetInfo.

        媒资状态。  取值如下： - UNCREATED：未创建（媒资ID不存在 ） - DELETED：已删除 - CANCELLED：上传取消 - SERVER_ERROR：上传失败（点播服务端故障） - UPLOAD_FAILED：上传失败（向OBS上传失败） - CREATING：创建中 - PUBLISHED：已发布 - WAITING_TRANSCODE：待发布（转码排队中） - TRANSCODING：待发布（转码中） - TRANSCODE_FAILED：待发布（转码失败） - TRANSCODE_SUCCEED：待发布（转码成功） - CREATED：待发布（未转码） - NO_ASSET：该媒资不存在 - DELETING：正在删除 - DELETE_FAILED：删除失败 - OBS_CREATING：OBS转存方式创建中 - OBS_CREATE_FAILED： OBS转存失败 - OBS_CREATE_SUCCESS： OBS转存成功

        :return: The status of this AssetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssetInfo.

        媒资状态。  取值如下： - UNCREATED：未创建（媒资ID不存在 ） - DELETED：已删除 - CANCELLED：上传取消 - SERVER_ERROR：上传失败（点播服务端故障） - UPLOAD_FAILED：上传失败（向OBS上传失败） - CREATING：创建中 - PUBLISHED：已发布 - WAITING_TRANSCODE：待发布（转码排队中） - TRANSCODING：待发布（转码中） - TRANSCODE_FAILED：待发布（转码失败） - TRANSCODE_SUCCEED：待发布（转码成功） - CREATED：待发布（未转码） - NO_ASSET：该媒资不存在 - DELETING：正在删除 - DELETE_FAILED：删除失败 - OBS_CREATING：OBS转存方式创建中 - OBS_CREATE_FAILED： OBS转存失败 - OBS_CREATE_SUCCESS： OBS转存成功

        :param status: The status of this AssetInfo.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this AssetInfo.

        媒资子状态或描述信息。 - 对于媒资异常场景，描述具体的异常原因。 - 对于正常场景，描述媒资的处理信息。

        :return: The description of this AssetInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetInfo.

        媒资子状态或描述信息。 - 对于媒资异常场景，描述具体的异常原因。 - 对于正常场景，描述媒资的处理信息。

        :param description: The description of this AssetInfo.
        :type description: str
        """
        self._description = description

    @property
    def base_info(self):
        """Gets the base_info of this AssetInfo.

        :return: The base_info of this AssetInfo.
        :rtype: :class:`huaweicloudsdkvod.v1.BaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this AssetInfo.

        :param base_info: The base_info of this AssetInfo.
        :type base_info: :class:`huaweicloudsdkvod.v1.BaseInfo`
        """
        self._base_info = base_info

    @property
    def play_info_array(self):
        """Gets the play_info_array of this AssetInfo.

        转码文件的播放信息。 - HLS或DASH：此数组的成员个数为n+1，n为转码输出路数。 - MP4：此数组的成员个数为n，n为转码输出路数。

        :return: The play_info_array of this AssetInfo.
        :rtype: list[:class:`huaweicloudsdkvod.v1.PlayInfo`]
        """
        return self._play_info_array

    @play_info_array.setter
    def play_info_array(self, play_info_array):
        """Sets the play_info_array of this AssetInfo.

        转码文件的播放信息。 - HLS或DASH：此数组的成员个数为n+1，n为转码输出路数。 - MP4：此数组的成员个数为n，n为转码输出路数。

        :param play_info_array: The play_info_array of this AssetInfo.
        :type play_info_array: list[:class:`huaweicloudsdkvod.v1.PlayInfo`]
        """
        self._play_info_array = play_info_array

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
        if not isinstance(other, AssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
