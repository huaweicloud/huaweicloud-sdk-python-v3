# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckVoiceAssetResponse(SdkResponse):

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
        'asset_name': 'str',
        'asset_type': 'str',
        'asset_state': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'asset_extra_meta': 'TtscAssetExtraMeta',
        'files': 'list[TtscAssetFileInfo]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_name': 'asset_name',
        'asset_type': 'asset_type',
        'asset_state': 'asset_state',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'asset_extra_meta': 'asset_extra_meta',
        'files': 'files'
    }

    def __init__(self, asset_id=None, asset_name=None, asset_type=None, asset_state=None, create_time=None, update_time=None, asset_extra_meta=None, files=None):
        r"""CheckVoiceAssetResponse

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID。
        :type asset_id: str
        :param asset_name: 资产名称。
        :type asset_name: str
        :param asset_type: 资产类型。  公共资产类型： * VOICE_MODEL：音色模型
        :type asset_type: str
        :param asset_state: 资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。
        :type asset_state: str
        :param create_time: 资产创建时间。
        :type create_time: str
        :param update_time: 资产更新时间。
        :type update_time: str
        :param asset_extra_meta: 
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.TtscAssetExtraMeta`
        :param files: 资产下的文件。
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.TtscAssetFileInfo`]
        """
        
        super(CheckVoiceAssetResponse, self).__init__()

        self._asset_id = None
        self._asset_name = None
        self._asset_type = None
        self._asset_state = None
        self._create_time = None
        self._update_time = None
        self._asset_extra_meta = None
        self._files = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if asset_name is not None:
            self.asset_name = asset_name
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_state is not None:
            self.asset_state = asset_state
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if asset_extra_meta is not None:
            self.asset_extra_meta = asset_extra_meta
        if files is not None:
            self.files = files

    @property
    def asset_id(self):
        r"""Gets the asset_id of this CheckVoiceAssetResponse.

        资产ID。

        :return: The asset_id of this CheckVoiceAssetResponse.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this CheckVoiceAssetResponse.

        资产ID。

        :param asset_id: The asset_id of this CheckVoiceAssetResponse.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_name(self):
        r"""Gets the asset_name of this CheckVoiceAssetResponse.

        资产名称。

        :return: The asset_name of this CheckVoiceAssetResponse.
        :rtype: str
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, asset_name):
        r"""Sets the asset_name of this CheckVoiceAssetResponse.

        资产名称。

        :param asset_name: The asset_name of this CheckVoiceAssetResponse.
        :type asset_name: str
        """
        self._asset_name = asset_name

    @property
    def asset_type(self):
        r"""Gets the asset_type of this CheckVoiceAssetResponse.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型

        :return: The asset_type of this CheckVoiceAssetResponse.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this CheckVoiceAssetResponse.

        资产类型。  公共资产类型： * VOICE_MODEL：音色模型

        :param asset_type: The asset_type of this CheckVoiceAssetResponse.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def asset_state(self):
        r"""Gets the asset_state of this CheckVoiceAssetResponse.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。

        :return: The asset_state of this CheckVoiceAssetResponse.
        :rtype: str
        """
        return self._asset_state

    @asset_state.setter
    def asset_state(self, asset_state):
        r"""Sets the asset_state of this CheckVoiceAssetResponse.

        资产状态。 * CREATING：资产创建中，主文件尚未上传 * FAILED：主文件上传失败 * UNACTIVED：主文件上传成功，资产未激活，资产不可用于其他业务（用户可更新状态） * ACTIVED：主文件上传成功，资产激活，资产可用于其他业务（用户可更新状态） * DELETING：资产删除中，资产不可用，资产可恢复 * DELETED：资产文件已删除，资产不可用，资产不可恢复 * BLOCK: 资产被冻结，资产不可用，不可查看文件。

        :param asset_state: The asset_state of this CheckVoiceAssetResponse.
        :type asset_state: str
        """
        self._asset_state = asset_state

    @property
    def create_time(self):
        r"""Gets the create_time of this CheckVoiceAssetResponse.

        资产创建时间。

        :return: The create_time of this CheckVoiceAssetResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CheckVoiceAssetResponse.

        资产创建时间。

        :param create_time: The create_time of this CheckVoiceAssetResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CheckVoiceAssetResponse.

        资产更新时间。

        :return: The update_time of this CheckVoiceAssetResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CheckVoiceAssetResponse.

        资产更新时间。

        :param update_time: The update_time of this CheckVoiceAssetResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def asset_extra_meta(self):
        r"""Gets the asset_extra_meta of this CheckVoiceAssetResponse.

        :return: The asset_extra_meta of this CheckVoiceAssetResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.TtscAssetExtraMeta`
        """
        return self._asset_extra_meta

    @asset_extra_meta.setter
    def asset_extra_meta(self, asset_extra_meta):
        r"""Sets the asset_extra_meta of this CheckVoiceAssetResponse.

        :param asset_extra_meta: The asset_extra_meta of this CheckVoiceAssetResponse.
        :type asset_extra_meta: :class:`huaweicloudsdkmetastudio.v1.TtscAssetExtraMeta`
        """
        self._asset_extra_meta = asset_extra_meta

    @property
    def files(self):
        r"""Gets the files of this CheckVoiceAssetResponse.

        资产下的文件。

        :return: The files of this CheckVoiceAssetResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.TtscAssetFileInfo`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this CheckVoiceAssetResponse.

        资产下的文件。

        :param files: The files of this CheckVoiceAssetResponse.
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.TtscAssetFileInfo`]
        """
        self._files = files

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
        if not isinstance(other, CheckVoiceAssetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
