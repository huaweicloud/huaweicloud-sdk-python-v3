# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrustedIpAddressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'repository_id': 'int',
        'ip_range': 'str',
        'ip_type': 'int',
        'ip_start': 'str',
        'ip_end': 'str',
        'view_flag': 'int',
        'download_flag': 'int',
        'upload_flag': 'int',
        'remark': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'order_flag': 'int'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'ip_range': 'ip_range',
        'ip_type': 'ip_type',
        'ip_start': 'ip_start',
        'ip_end': 'ip_end',
        'view_flag': 'view_flag',
        'download_flag': 'download_flag',
        'upload_flag': 'upload_flag',
        'remark': 'remark',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'order_flag': 'order_flag'
    }

    def __init__(self, id=None, repository_id=None, ip_range=None, ip_type=None, ip_start=None, ip_end=None, view_flag=None, download_flag=None, upload_flag=None, remark=None, created_at=None, updated_at=None, order_flag=None):
        r"""UpdateTrustedIpAddressResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 白名单id。
        :type id: str
        :param repository_id: **参数解释：** 仓库id。
        :type repository_id: int
        :param ip_range: **参数解释：** ip范围。
        :type ip_range: str
        :param ip_type: **参数解释：** 格式类型。 - 0，表示指定ip。 - 1，表示ip范围。 - 2，表示CIDR。
        :type ip_type: int
        :param ip_start: **参数解释：** 起始ip。
        :type ip_start: str
        :param ip_end: **参数解释：** 结束ip。
        :type ip_end: str
        :param view_flag: **参数解释：** 是否允许访问代码仓库。 - 0，表示禁止访问。 - 1，表示允许访问。
        :type view_flag: int
        :param download_flag: **参数解释：** 是否允许下载代码。 - 0，表示禁止下载。 - 1，表示允许下载。
        :type download_flag: int
        :param upload_flag: **参数解释：** 是否允许提交代码。 - 0，表示禁止提交。 - 1，表示允许提交。
        :type upload_flag: int
        :param remark: **参数解释：** 备注。 **取值范围：** 字符串长度不少于0，不超过200。
        :type remark: str
        :param created_at: **参数解释：** 创建时间。 **参数解释：** MMM dd, yyyy hh:mm:ss a            
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **参数解释：** MMM dd, yyyy hh:mm:ss a
        :type updated_at: str
        :param order_flag: **参数解释：** 排序。 - 0，表示默认规则。 - 1，表示自定义规则。
        :type order_flag: int
        """
        
        super(UpdateTrustedIpAddressResponse, self).__init__()

        self._id = None
        self._repository_id = None
        self._ip_range = None
        self._ip_type = None
        self._ip_start = None
        self._ip_end = None
        self._view_flag = None
        self._download_flag = None
        self._upload_flag = None
        self._remark = None
        self._created_at = None
        self._updated_at = None
        self._order_flag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if ip_range is not None:
            self.ip_range = ip_range
        if ip_type is not None:
            self.ip_type = ip_type
        if ip_start is not None:
            self.ip_start = ip_start
        if ip_end is not None:
            self.ip_end = ip_end
        if view_flag is not None:
            self.view_flag = view_flag
        if download_flag is not None:
            self.download_flag = download_flag
        if upload_flag is not None:
            self.upload_flag = upload_flag
        if remark is not None:
            self.remark = remark
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if order_flag is not None:
            self.order_flag = order_flag

    @property
    def id(self):
        r"""Gets the id of this UpdateTrustedIpAddressResponse.

        **参数解释：** 白名单id。

        :return: The id of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateTrustedIpAddressResponse.

        **参数解释：** 白名单id。

        :param id: The id of this UpdateTrustedIpAddressResponse.
        :type id: str
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this UpdateTrustedIpAddressResponse.

        **参数解释：** 仓库id。

        :return: The repository_id of this UpdateTrustedIpAddressResponse.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this UpdateTrustedIpAddressResponse.

        **参数解释：** 仓库id。

        :param repository_id: The repository_id of this UpdateTrustedIpAddressResponse.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def ip_range(self):
        r"""Gets the ip_range of this UpdateTrustedIpAddressResponse.

        **参数解释：** ip范围。

        :return: The ip_range of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        r"""Sets the ip_range of this UpdateTrustedIpAddressResponse.

        **参数解释：** ip范围。

        :param ip_range: The ip_range of this UpdateTrustedIpAddressResponse.
        :type ip_range: str
        """
        self._ip_range = ip_range

    @property
    def ip_type(self):
        r"""Gets the ip_type of this UpdateTrustedIpAddressResponse.

        **参数解释：** 格式类型。 - 0，表示指定ip。 - 1，表示ip范围。 - 2，表示CIDR。

        :return: The ip_type of this UpdateTrustedIpAddressResponse.
        :rtype: int
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this UpdateTrustedIpAddressResponse.

        **参数解释：** 格式类型。 - 0，表示指定ip。 - 1，表示ip范围。 - 2，表示CIDR。

        :param ip_type: The ip_type of this UpdateTrustedIpAddressResponse.
        :type ip_type: int
        """
        self._ip_type = ip_type

    @property
    def ip_start(self):
        r"""Gets the ip_start of this UpdateTrustedIpAddressResponse.

        **参数解释：** 起始ip。

        :return: The ip_start of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._ip_start

    @ip_start.setter
    def ip_start(self, ip_start):
        r"""Sets the ip_start of this UpdateTrustedIpAddressResponse.

        **参数解释：** 起始ip。

        :param ip_start: The ip_start of this UpdateTrustedIpAddressResponse.
        :type ip_start: str
        """
        self._ip_start = ip_start

    @property
    def ip_end(self):
        r"""Gets the ip_end of this UpdateTrustedIpAddressResponse.

        **参数解释：** 结束ip。

        :return: The ip_end of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._ip_end

    @ip_end.setter
    def ip_end(self, ip_end):
        r"""Sets the ip_end of this UpdateTrustedIpAddressResponse.

        **参数解释：** 结束ip。

        :param ip_end: The ip_end of this UpdateTrustedIpAddressResponse.
        :type ip_end: str
        """
        self._ip_end = ip_end

    @property
    def view_flag(self):
        r"""Gets the view_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 是否允许访问代码仓库。 - 0，表示禁止访问。 - 1，表示允许访问。

        :return: The view_flag of this UpdateTrustedIpAddressResponse.
        :rtype: int
        """
        return self._view_flag

    @view_flag.setter
    def view_flag(self, view_flag):
        r"""Sets the view_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 是否允许访问代码仓库。 - 0，表示禁止访问。 - 1，表示允许访问。

        :param view_flag: The view_flag of this UpdateTrustedIpAddressResponse.
        :type view_flag: int
        """
        self._view_flag = view_flag

    @property
    def download_flag(self):
        r"""Gets the download_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 是否允许下载代码。 - 0，表示禁止下载。 - 1，表示允许下载。

        :return: The download_flag of this UpdateTrustedIpAddressResponse.
        :rtype: int
        """
        return self._download_flag

    @download_flag.setter
    def download_flag(self, download_flag):
        r"""Sets the download_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 是否允许下载代码。 - 0，表示禁止下载。 - 1，表示允许下载。

        :param download_flag: The download_flag of this UpdateTrustedIpAddressResponse.
        :type download_flag: int
        """
        self._download_flag = download_flag

    @property
    def upload_flag(self):
        r"""Gets the upload_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 是否允许提交代码。 - 0，表示禁止提交。 - 1，表示允许提交。

        :return: The upload_flag of this UpdateTrustedIpAddressResponse.
        :rtype: int
        """
        return self._upload_flag

    @upload_flag.setter
    def upload_flag(self, upload_flag):
        r"""Sets the upload_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 是否允许提交代码。 - 0，表示禁止提交。 - 1，表示允许提交。

        :param upload_flag: The upload_flag of this UpdateTrustedIpAddressResponse.
        :type upload_flag: int
        """
        self._upload_flag = upload_flag

    @property
    def remark(self):
        r"""Gets the remark of this UpdateTrustedIpAddressResponse.

        **参数解释：** 备注。 **取值范围：** 字符串长度不少于0，不超过200。

        :return: The remark of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this UpdateTrustedIpAddressResponse.

        **参数解释：** 备注。 **取值范围：** 字符串长度不少于0，不超过200。

        :param remark: The remark of this UpdateTrustedIpAddressResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateTrustedIpAddressResponse.

        **参数解释：** 创建时间。 **参数解释：** MMM dd, yyyy hh:mm:ss a            

        :return: The created_at of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateTrustedIpAddressResponse.

        **参数解释：** 创建时间。 **参数解释：** MMM dd, yyyy hh:mm:ss a            

        :param created_at: The created_at of this UpdateTrustedIpAddressResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateTrustedIpAddressResponse.

        **参数解释：** 更新时间。 **参数解释：** MMM dd, yyyy hh:mm:ss a

        :return: The updated_at of this UpdateTrustedIpAddressResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateTrustedIpAddressResponse.

        **参数解释：** 更新时间。 **参数解释：** MMM dd, yyyy hh:mm:ss a

        :param updated_at: The updated_at of this UpdateTrustedIpAddressResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def order_flag(self):
        r"""Gets the order_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 排序。 - 0，表示默认规则。 - 1，表示自定义规则。

        :return: The order_flag of this UpdateTrustedIpAddressResponse.
        :rtype: int
        """
        return self._order_flag

    @order_flag.setter
    def order_flag(self, order_flag):
        r"""Sets the order_flag of this UpdateTrustedIpAddressResponse.

        **参数解释：** 排序。 - 0，表示默认规则。 - 1，表示自定义规则。

        :param order_flag: The order_flag of this UpdateTrustedIpAddressResponse.
        :type order_flag: int
        """
        self._order_flag = order_flag

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
        if not isinstance(other, UpdateTrustedIpAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
