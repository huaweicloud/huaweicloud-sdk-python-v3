# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MssPackageItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'stream_selection': 'list[StreamSelectionItem]',
        'segment_duration_seconds': 'int',
        'playlist_window_seconds': 'int',
        'encryption': 'Encryption',
        'ext_args': 'object',
        'delay_segment': 'int',
        'request_args': 'PackageRequestArgs',
        'enable_access': 'bool',
        'allow_all_ip_access': 'bool',
        'ip_whitelist': 'str',
        'cdn_identifier_header': 'HttpHeader',
        'origin_domain_master': 'str',
        'origin_domain_slave': 'str',
        'manifest_name': 'str',
        'slave_url': 'str'
    }

    attribute_map = {
        'url': 'url',
        'stream_selection': 'stream_selection',
        'segment_duration_seconds': 'segment_duration_seconds',
        'playlist_window_seconds': 'playlist_window_seconds',
        'encryption': 'encryption',
        'ext_args': 'ext_args',
        'delay_segment': 'delay_segment',
        'request_args': 'request_args',
        'enable_access': 'enable_access',
        'allow_all_ip_access': 'allow_all_ip_access',
        'ip_whitelist': 'ip_whitelist',
        'cdn_identifier_header': 'cdn_identifier_header',
        'origin_domain_master': 'origin_domain_master',
        'origin_domain_slave': 'origin_domain_slave',
        'manifest_name': 'manifest_name',
        'slave_url': 'slave_url'
    }

    def __init__(self, url=None, stream_selection=None, segment_duration_seconds=None, playlist_window_seconds=None, encryption=None, ext_args=None, delay_segment=None, request_args=None, enable_access=None, allow_all_ip_access=None, ip_whitelist=None, cdn_identifier_header=None, origin_domain_master=None, origin_domain_slave=None, manifest_name=None, slave_url=None):
        r"""MssPackageItem

        The model defined in huaweicloud sdk

        :param url: 客户自定义的拉流地址，包括方法、域名、路径
        :type url: str
        :param stream_selection: 从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。
        :type stream_selection: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        :param segment_duration_seconds: 频道输出分片的时长，为必选项  单位：秒。取值范围：1-10 &gt; 修改分片时长会影响已录制内容的时移和回看服务，请谨慎修改！
        :type segment_duration_seconds: int
        :param playlist_window_seconds: 频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）
        :type playlist_window_seconds: int
        :param encryption: 
        :type encryption: :class:`huaweicloudsdklive.v1.Encryption`
        :param ext_args: 其他额外参数
        :type ext_args: object
        :param delay_segment: 延播时长，单位秒
        :type delay_segment: int
        :param request_args: 
        :type request_args: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        :param enable_access: 当频道mode是ONLY_OS类型时，允许本输出可以直接从源站拉流，默认：false true：允许output访问 false：禁止output访问
        :type enable_access: bool
        :param allow_all_ip_access: 是否放通所有的IP访问，默认：false true：允许所有的IP地址访问，ip_whitelist配置不生效 false：不允许所有的IP地址访问，ip_whitelist生效，仅在ip_whitelist配置的ip地址才能访问
        :type allow_all_ip_access: bool
        :param ip_whitelist: 当频道类型mode是ONLY_OS类型时，允许直接从源站拉流的IP白名单
        :type ip_whitelist: str
        :param cdn_identifier_header: 
        :type cdn_identifier_header: :class:`huaweicloudsdklive.v1.HttpHeader`
        :param origin_domain_master: 源站分发域名-主region 跟CreateOttChannelInfoReq.region一致 满足正则：^(\\[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.){2,}[a-zA-Z]{2,16}$ 最大长度255
        :type origin_domain_master: str
        :param origin_domain_slave: 源站分发域名-备region 满足正则：^(\\[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.){2,}[a-zA-Z]{2,16}$ 最大长度255
        :type origin_domain_slave: str
        :param manifest_name: output的索引文件名字 默认：index 长度：0-128 字符集：大小写字母、数字、\&quot;-\&quot;、\&quot;.\&quot;、\&quot;_\&quot;，不能有/路径
        :type manifest_name: str
        :param slave_url: 客户自定义的拉流地址，包括方法、域名、路径
        :type slave_url: str
        """
        
        

        self._url = None
        self._stream_selection = None
        self._segment_duration_seconds = None
        self._playlist_window_seconds = None
        self._encryption = None
        self._ext_args = None
        self._delay_segment = None
        self._request_args = None
        self._enable_access = None
        self._allow_all_ip_access = None
        self._ip_whitelist = None
        self._cdn_identifier_header = None
        self._origin_domain_master = None
        self._origin_domain_slave = None
        self._manifest_name = None
        self._slave_url = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if stream_selection is not None:
            self.stream_selection = stream_selection
        self.segment_duration_seconds = segment_duration_seconds
        if playlist_window_seconds is not None:
            self.playlist_window_seconds = playlist_window_seconds
        if encryption is not None:
            self.encryption = encryption
        if ext_args is not None:
            self.ext_args = ext_args
        if delay_segment is not None:
            self.delay_segment = delay_segment
        if request_args is not None:
            self.request_args = request_args
        if enable_access is not None:
            self.enable_access = enable_access
        if allow_all_ip_access is not None:
            self.allow_all_ip_access = allow_all_ip_access
        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist
        if cdn_identifier_header is not None:
            self.cdn_identifier_header = cdn_identifier_header
        if origin_domain_master is not None:
            self.origin_domain_master = origin_domain_master
        if origin_domain_slave is not None:
            self.origin_domain_slave = origin_domain_slave
        if manifest_name is not None:
            self.manifest_name = manifest_name
        if slave_url is not None:
            self.slave_url = slave_url

    @property
    def url(self):
        r"""Gets the url of this MssPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径

        :return: The url of this MssPackageItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this MssPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径

        :param url: The url of this MssPackageItem.
        :type url: str
        """
        self._url = url

    @property
    def stream_selection(self):
        r"""Gets the stream_selection of this MssPackageItem.

        从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。

        :return: The stream_selection of this MssPackageItem.
        :rtype: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        """
        return self._stream_selection

    @stream_selection.setter
    def stream_selection(self, stream_selection):
        r"""Sets the stream_selection of this MssPackageItem.

        从全量流中过滤出一个码率在[min, max]区间的流。如果不需要码率过滤可不选。

        :param stream_selection: The stream_selection of this MssPackageItem.
        :type stream_selection: list[:class:`huaweicloudsdklive.v1.StreamSelectionItem`]
        """
        self._stream_selection = stream_selection

    @property
    def segment_duration_seconds(self):
        r"""Gets the segment_duration_seconds of this MssPackageItem.

        频道输出分片的时长，为必选项  单位：秒。取值范围：1-10 > 修改分片时长会影响已录制内容的时移和回看服务，请谨慎修改！

        :return: The segment_duration_seconds of this MssPackageItem.
        :rtype: int
        """
        return self._segment_duration_seconds

    @segment_duration_seconds.setter
    def segment_duration_seconds(self, segment_duration_seconds):
        r"""Sets the segment_duration_seconds of this MssPackageItem.

        频道输出分片的时长，为必选项  单位：秒。取值范围：1-10 > 修改分片时长会影响已录制内容的时移和回看服务，请谨慎修改！

        :param segment_duration_seconds: The segment_duration_seconds of this MssPackageItem.
        :type segment_duration_seconds: int
        """
        self._segment_duration_seconds = segment_duration_seconds

    @property
    def playlist_window_seconds(self):
        r"""Gets the playlist_window_seconds of this MssPackageItem.

        频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）

        :return: The playlist_window_seconds of this MssPackageItem.
        :rtype: int
        """
        return self._playlist_window_seconds

    @playlist_window_seconds.setter
    def playlist_window_seconds(self, playlist_window_seconds):
        r"""Sets the playlist_window_seconds of this MssPackageItem.

        频道直播返回分片的窗口长度，为频道输出分片的时长乘以数量后得到的值。实际返回的分片数不小于3个。  单位：秒。取值范围：0 - 86400（24小时转化成秒后的取值）

        :param playlist_window_seconds: The playlist_window_seconds of this MssPackageItem.
        :type playlist_window_seconds: int
        """
        self._playlist_window_seconds = playlist_window_seconds

    @property
    def encryption(self):
        r"""Gets the encryption of this MssPackageItem.

        :return: The encryption of this MssPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.Encryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        r"""Sets the encryption of this MssPackageItem.

        :param encryption: The encryption of this MssPackageItem.
        :type encryption: :class:`huaweicloudsdklive.v1.Encryption`
        """
        self._encryption = encryption

    @property
    def ext_args(self):
        r"""Gets the ext_args of this MssPackageItem.

        其他额外参数

        :return: The ext_args of this MssPackageItem.
        :rtype: object
        """
        return self._ext_args

    @ext_args.setter
    def ext_args(self, ext_args):
        r"""Sets the ext_args of this MssPackageItem.

        其他额外参数

        :param ext_args: The ext_args of this MssPackageItem.
        :type ext_args: object
        """
        self._ext_args = ext_args

    @property
    def delay_segment(self):
        r"""Gets the delay_segment of this MssPackageItem.

        延播时长，单位秒

        :return: The delay_segment of this MssPackageItem.
        :rtype: int
        """
        return self._delay_segment

    @delay_segment.setter
    def delay_segment(self, delay_segment):
        r"""Sets the delay_segment of this MssPackageItem.

        延播时长，单位秒

        :param delay_segment: The delay_segment of this MssPackageItem.
        :type delay_segment: int
        """
        self._delay_segment = delay_segment

    @property
    def request_args(self):
        r"""Gets the request_args of this MssPackageItem.

        :return: The request_args of this MssPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        return self._request_args

    @request_args.setter
    def request_args(self, request_args):
        r"""Sets the request_args of this MssPackageItem.

        :param request_args: The request_args of this MssPackageItem.
        :type request_args: :class:`huaweicloudsdklive.v1.PackageRequestArgs`
        """
        self._request_args = request_args

    @property
    def enable_access(self):
        r"""Gets the enable_access of this MssPackageItem.

        当频道mode是ONLY_OS类型时，允许本输出可以直接从源站拉流，默认：false true：允许output访问 false：禁止output访问

        :return: The enable_access of this MssPackageItem.
        :rtype: bool
        """
        return self._enable_access

    @enable_access.setter
    def enable_access(self, enable_access):
        r"""Sets the enable_access of this MssPackageItem.

        当频道mode是ONLY_OS类型时，允许本输出可以直接从源站拉流，默认：false true：允许output访问 false：禁止output访问

        :param enable_access: The enable_access of this MssPackageItem.
        :type enable_access: bool
        """
        self._enable_access = enable_access

    @property
    def allow_all_ip_access(self):
        r"""Gets the allow_all_ip_access of this MssPackageItem.

        是否放通所有的IP访问，默认：false true：允许所有的IP地址访问，ip_whitelist配置不生效 false：不允许所有的IP地址访问，ip_whitelist生效，仅在ip_whitelist配置的ip地址才能访问

        :return: The allow_all_ip_access of this MssPackageItem.
        :rtype: bool
        """
        return self._allow_all_ip_access

    @allow_all_ip_access.setter
    def allow_all_ip_access(self, allow_all_ip_access):
        r"""Sets the allow_all_ip_access of this MssPackageItem.

        是否放通所有的IP访问，默认：false true：允许所有的IP地址访问，ip_whitelist配置不生效 false：不允许所有的IP地址访问，ip_whitelist生效，仅在ip_whitelist配置的ip地址才能访问

        :param allow_all_ip_access: The allow_all_ip_access of this MssPackageItem.
        :type allow_all_ip_access: bool
        """
        self._allow_all_ip_access = allow_all_ip_access

    @property
    def ip_whitelist(self):
        r"""Gets the ip_whitelist of this MssPackageItem.

        当频道类型mode是ONLY_OS类型时，允许直接从源站拉流的IP白名单

        :return: The ip_whitelist of this MssPackageItem.
        :rtype: str
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        r"""Sets the ip_whitelist of this MssPackageItem.

        当频道类型mode是ONLY_OS类型时，允许直接从源站拉流的IP白名单

        :param ip_whitelist: The ip_whitelist of this MssPackageItem.
        :type ip_whitelist: str
        """
        self._ip_whitelist = ip_whitelist

    @property
    def cdn_identifier_header(self):
        r"""Gets the cdn_identifier_header of this MssPackageItem.

        :return: The cdn_identifier_header of this MssPackageItem.
        :rtype: :class:`huaweicloudsdklive.v1.HttpHeader`
        """
        return self._cdn_identifier_header

    @cdn_identifier_header.setter
    def cdn_identifier_header(self, cdn_identifier_header):
        r"""Sets the cdn_identifier_header of this MssPackageItem.

        :param cdn_identifier_header: The cdn_identifier_header of this MssPackageItem.
        :type cdn_identifier_header: :class:`huaweicloudsdklive.v1.HttpHeader`
        """
        self._cdn_identifier_header = cdn_identifier_header

    @property
    def origin_domain_master(self):
        r"""Gets the origin_domain_master of this MssPackageItem.

        源站分发域名-主region 跟CreateOttChannelInfoReq.region一致 满足正则：^(\\[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.){2,}[a-zA-Z]{2,16}$ 最大长度255

        :return: The origin_domain_master of this MssPackageItem.
        :rtype: str
        """
        return self._origin_domain_master

    @origin_domain_master.setter
    def origin_domain_master(self, origin_domain_master):
        r"""Sets the origin_domain_master of this MssPackageItem.

        源站分发域名-主region 跟CreateOttChannelInfoReq.region一致 满足正则：^(\\[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.){2,}[a-zA-Z]{2,16}$ 最大长度255

        :param origin_domain_master: The origin_domain_master of this MssPackageItem.
        :type origin_domain_master: str
        """
        self._origin_domain_master = origin_domain_master

    @property
    def origin_domain_slave(self):
        r"""Gets the origin_domain_slave of this MssPackageItem.

        源站分发域名-备region 满足正则：^(\\[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.){2,}[a-zA-Z]{2,16}$ 最大长度255

        :return: The origin_domain_slave of this MssPackageItem.
        :rtype: str
        """
        return self._origin_domain_slave

    @origin_domain_slave.setter
    def origin_domain_slave(self, origin_domain_slave):
        r"""Sets the origin_domain_slave of this MssPackageItem.

        源站分发域名-备region 满足正则：^(\\[a-zA-Z0-9]([a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?\\.){2,}[a-zA-Z]{2,16}$ 最大长度255

        :param origin_domain_slave: The origin_domain_slave of this MssPackageItem.
        :type origin_domain_slave: str
        """
        self._origin_domain_slave = origin_domain_slave

    @property
    def manifest_name(self):
        r"""Gets the manifest_name of this MssPackageItem.

        output的索引文件名字 默认：index 长度：0-128 字符集：大小写字母、数字、\"-\"、\".\"、\"_\"，不能有/路径

        :return: The manifest_name of this MssPackageItem.
        :rtype: str
        """
        return self._manifest_name

    @manifest_name.setter
    def manifest_name(self, manifest_name):
        r"""Sets the manifest_name of this MssPackageItem.

        output的索引文件名字 默认：index 长度：0-128 字符集：大小写字母、数字、\"-\"、\".\"、\"_\"，不能有/路径

        :param manifest_name: The manifest_name of this MssPackageItem.
        :type manifest_name: str
        """
        self._manifest_name = manifest_name

    @property
    def slave_url(self):
        r"""Gets the slave_url of this MssPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径

        :return: The slave_url of this MssPackageItem.
        :rtype: str
        """
        return self._slave_url

    @slave_url.setter
    def slave_url(self, slave_url):
        r"""Sets the slave_url of this MssPackageItem.

        客户自定义的拉流地址，包括方法、域名、路径

        :param slave_url: The slave_url of this MssPackageItem.
        :type slave_url: str
        """
        self._slave_url = slave_url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MssPackageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
