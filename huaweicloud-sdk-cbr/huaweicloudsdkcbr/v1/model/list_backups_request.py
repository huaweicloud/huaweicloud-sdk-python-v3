# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkpoint_id': 'str',
        'dec': 'bool',
        'end_time': 'str',
        'image_type': 'str',
        'limit': 'int',
        'marker': 'str',
        'name': 'str',
        'offset': 'int',
        'resource_az': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'sort': 'str',
        'start_time': 'str',
        'status': 'str',
        'vault_id': 'str',
        'enterprise_project_id': 'str',
        'own_type': 'str',
        'member_status': 'str',
        'parent_id': 'str',
        'used_percent': 'str',
        'show_replication': 'bool',
        'incremental': 'bool'
    }

    attribute_map = {
        'checkpoint_id': 'checkpoint_id',
        'dec': 'dec',
        'end_time': 'end_time',
        'image_type': 'image_type',
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'offset': 'offset',
        'resource_az': 'resource_az',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'sort': 'sort',
        'start_time': 'start_time',
        'status': 'status',
        'vault_id': 'vault_id',
        'enterprise_project_id': 'enterprise_project_id',
        'own_type': 'own_type',
        'member_status': 'member_status',
        'parent_id': 'parent_id',
        'used_percent': 'used_percent',
        'show_replication': 'show_replication',
        'incremental': 'incremental'
    }

    def __init__(self, checkpoint_id=None, dec=None, end_time=None, image_type=None, limit=None, marker=None, name=None, offset=None, resource_az=None, resource_id=None, resource_name=None, resource_type=None, sort=None, start_time=None, status=None, vault_id=None, enterprise_project_id=None, own_type=None, member_status=None, parent_id=None, used_percent=None, show_replication=None, incremental=None):
        """ListBackupsRequest

        The model defined in huaweicloud sdk

        :param checkpoint_id: 还原点ID
        :type checkpoint_id: str
        :param dec: 专属云 （专属云场景使用，非专属云场景不生效）
        :type dec: bool
        :param end_time: 备份产生时间范围的结束时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z
        :type end_time: str
        :param image_type: 备份类型
        :type image_type: str
        :param limit: 每页显示的条目数量，正整数
        :type limit: int
        :param marker: 上一次查询最后一条的id
        :type marker: str
        :param name: 名称
        :type name: str
        :param offset: 偏移值，正整数
        :type offset: int
        :param resource_az: 支持按az来过滤
        :type resource_az: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型: 云服务器: OS::Nova::Server, 云硬盘: OS::Cinder::Volume, 云桌面：OS::Workspace::DesktopV2
        :type resource_type: str
        :param sort: sort的内容为一组由逗号分隔的属性及可选排序方向组成，形如&lt;key1&gt;[:&lt;direction&gt;],&lt;key2&gt;[:&lt;direction&gt;],其中direction的取值为asc (升序) 或 desc (降序),如没有传入direction参数，默认为降序，sort内容的长度限制为255个字符。key取值范围:[created_at，updated_at，name，status，protected_at，id]
        :type sort: str
        :param start_time: 备份产生时间范围的开始时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z
        :type start_time: str
        :param status: 状态。 调用API时，支持通过传多个status值进行过滤。例如：status&#x3D;available&amp;status&#x3D;error
        :type status: str
        :param vault_id: 存储库ID
        :type vault_id: str
        :param enterprise_project_id: 企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id
        :type enterprise_project_id: str
        :param own_type: 持有类型，私有的private/共享的shared/全部all_granted，默认只查询private。
        :type own_type: str
        :param member_status: 共享状态
        :type member_status: str
        :param parent_id: 父备份ID
        :type parent_id: str
        :param used_percent: 根据存储库使用率过滤备份，取值范围 [1, 100]，含1和100。例如，used_percent&#x3D;80，表示筛选所属存储库使用率大于等于80%的所有备份。
        :type used_percent: str
        :param show_replication: 是否返回复制记录
        :type show_replication: bool
        :param incremental: 是否是增备
        :type incremental: bool
        """
        
        

        self._checkpoint_id = None
        self._dec = None
        self._end_time = None
        self._image_type = None
        self._limit = None
        self._marker = None
        self._name = None
        self._offset = None
        self._resource_az = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._sort = None
        self._start_time = None
        self._status = None
        self._vault_id = None
        self._enterprise_project_id = None
        self._own_type = None
        self._member_status = None
        self._parent_id = None
        self._used_percent = None
        self._show_replication = None
        self._incremental = None
        self.discriminator = None

        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        if dec is not None:
            self.dec = dec
        if end_time is not None:
            self.end_time = end_time
        if image_type is not None:
            self.image_type = image_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if resource_az is not None:
            self.resource_az = resource_az
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if sort is not None:
            self.sort = sort
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if vault_id is not None:
            self.vault_id = vault_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if own_type is not None:
            self.own_type = own_type
        if member_status is not None:
            self.member_status = member_status
        if parent_id is not None:
            self.parent_id = parent_id
        if used_percent is not None:
            self.used_percent = used_percent
        if show_replication is not None:
            self.show_replication = show_replication
        if incremental is not None:
            self.incremental = incremental

    @property
    def checkpoint_id(self):
        """Gets the checkpoint_id of this ListBackupsRequest.

        还原点ID

        :return: The checkpoint_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        """Sets the checkpoint_id of this ListBackupsRequest.

        还原点ID

        :param checkpoint_id: The checkpoint_id of this ListBackupsRequest.
        :type checkpoint_id: str
        """
        self._checkpoint_id = checkpoint_id

    @property
    def dec(self):
        """Gets the dec of this ListBackupsRequest.

        专属云 （专属云场景使用，非专属云场景不生效）

        :return: The dec of this ListBackupsRequest.
        :rtype: bool
        """
        return self._dec

    @dec.setter
    def dec(self, dec):
        """Sets the dec of this ListBackupsRequest.

        专属云 （专属云场景使用，非专属云场景不生效）

        :param dec: The dec of this ListBackupsRequest.
        :type dec: bool
        """
        self._dec = dec

    @property
    def end_time(self):
        """Gets the end_time of this ListBackupsRequest.

        备份产生时间范围的结束时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z

        :return: The end_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackupsRequest.

        备份产生时间范围的结束时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z

        :param end_time: The end_time of this ListBackupsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def image_type(self):
        """Gets the image_type of this ListBackupsRequest.

        备份类型

        :return: The image_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ListBackupsRequest.

        备份类型

        :param image_type: The image_type of this ListBackupsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def limit(self):
        """Gets the limit of this ListBackupsRequest.

        每页显示的条目数量，正整数

        :return: The limit of this ListBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackupsRequest.

        每页显示的条目数量，正整数

        :param limit: The limit of this ListBackupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListBackupsRequest.

        上一次查询最后一条的id

        :return: The marker of this ListBackupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListBackupsRequest.

        上一次查询最后一条的id

        :param marker: The marker of this ListBackupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListBackupsRequest.

        名称

        :return: The name of this ListBackupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackupsRequest.

        名称

        :param name: The name of this ListBackupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListBackupsRequest.

        偏移值，正整数

        :return: The offset of this ListBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackupsRequest.

        偏移值，正整数

        :param offset: The offset of this ListBackupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def resource_az(self):
        """Gets the resource_az of this ListBackupsRequest.

        支持按az来过滤

        :return: The resource_az of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_az

    @resource_az.setter
    def resource_az(self, resource_az):
        """Sets the resource_az of this ListBackupsRequest.

        支持按az来过滤

        :param resource_az: The resource_az of this ListBackupsRequest.
        :type resource_az: str
        """
        self._resource_az = resource_az

    @property
    def resource_id(self):
        """Gets the resource_id of this ListBackupsRequest.

        资源ID

        :return: The resource_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListBackupsRequest.

        资源ID

        :param resource_id: The resource_id of this ListBackupsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ListBackupsRequest.

        资源名称

        :return: The resource_name of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListBackupsRequest.

        资源名称

        :param resource_name: The resource_name of this ListBackupsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ListBackupsRequest.

        资源类型: 云服务器: OS::Nova::Server, 云硬盘: OS::Cinder::Volume, 云桌面：OS::Workspace::DesktopV2

        :return: The resource_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListBackupsRequest.

        资源类型: 云服务器: OS::Nova::Server, 云硬盘: OS::Cinder::Volume, 云桌面：OS::Workspace::DesktopV2

        :param resource_type: The resource_type of this ListBackupsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def sort(self):
        """Gets the sort of this ListBackupsRequest.

        sort的内容为一组由逗号分隔的属性及可选排序方向组成，形如<key1>[:<direction>],<key2>[:<direction>],其中direction的取值为asc (升序) 或 desc (降序),如没有传入direction参数，默认为降序，sort内容的长度限制为255个字符。key取值范围:[created_at，updated_at，name，status，protected_at，id]

        :return: The sort of this ListBackupsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListBackupsRequest.

        sort的内容为一组由逗号分隔的属性及可选排序方向组成，形如<key1>[:<direction>],<key2>[:<direction>],其中direction的取值为asc (升序) 或 desc (降序),如没有传入direction参数，默认为降序，sort内容的长度限制为255个字符。key取值范围:[created_at，updated_at，name，status，protected_at，id]

        :param sort: The sort of this ListBackupsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def start_time(self):
        """Gets the start_time of this ListBackupsRequest.

        备份产生时间范围的开始时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z

        :return: The start_time of this ListBackupsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListBackupsRequest.

        备份产生时间范围的开始时间，格式为%YYYY-%mm-%ddT%HH:%MM:%SSZ，例如2018-02-01T12:00:00Z

        :param start_time: The start_time of this ListBackupsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this ListBackupsRequest.

        状态。 调用API时，支持通过传多个status值进行过滤。例如：status=available&status=error

        :return: The status of this ListBackupsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBackupsRequest.

        状态。 调用API时，支持通过传多个status值进行过滤。例如：status=available&status=error

        :param status: The status of this ListBackupsRequest.
        :type status: str
        """
        self._status = status

    @property
    def vault_id(self):
        """Gets the vault_id of this ListBackupsRequest.

        存储库ID

        :return: The vault_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ListBackupsRequest.

        存储库ID

        :param vault_id: The vault_id of this ListBackupsRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListBackupsRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :return: The enterprise_project_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListBackupsRequest.

        企业项目id或all_granted_eps，all_granted_eps表示查询用户有权限的所有企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListBackupsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def own_type(self):
        """Gets the own_type of this ListBackupsRequest.

        持有类型，私有的private/共享的shared/全部all_granted，默认只查询private。

        :return: The own_type of this ListBackupsRequest.
        :rtype: str
        """
        return self._own_type

    @own_type.setter
    def own_type(self, own_type):
        """Sets the own_type of this ListBackupsRequest.

        持有类型，私有的private/共享的shared/全部all_granted，默认只查询private。

        :param own_type: The own_type of this ListBackupsRequest.
        :type own_type: str
        """
        self._own_type = own_type

    @property
    def member_status(self):
        """Gets the member_status of this ListBackupsRequest.

        共享状态

        :return: The member_status of this ListBackupsRequest.
        :rtype: str
        """
        return self._member_status

    @member_status.setter
    def member_status(self, member_status):
        """Sets the member_status of this ListBackupsRequest.

        共享状态

        :param member_status: The member_status of this ListBackupsRequest.
        :type member_status: str
        """
        self._member_status = member_status

    @property
    def parent_id(self):
        """Gets the parent_id of this ListBackupsRequest.

        父备份ID

        :return: The parent_id of this ListBackupsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListBackupsRequest.

        父备份ID

        :param parent_id: The parent_id of this ListBackupsRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def used_percent(self):
        """Gets the used_percent of this ListBackupsRequest.

        根据存储库使用率过滤备份，取值范围 [1, 100]，含1和100。例如，used_percent=80，表示筛选所属存储库使用率大于等于80%的所有备份。

        :return: The used_percent of this ListBackupsRequest.
        :rtype: str
        """
        return self._used_percent

    @used_percent.setter
    def used_percent(self, used_percent):
        """Sets the used_percent of this ListBackupsRequest.

        根据存储库使用率过滤备份，取值范围 [1, 100]，含1和100。例如，used_percent=80，表示筛选所属存储库使用率大于等于80%的所有备份。

        :param used_percent: The used_percent of this ListBackupsRequest.
        :type used_percent: str
        """
        self._used_percent = used_percent

    @property
    def show_replication(self):
        """Gets the show_replication of this ListBackupsRequest.

        是否返回复制记录

        :return: The show_replication of this ListBackupsRequest.
        :rtype: bool
        """
        return self._show_replication

    @show_replication.setter
    def show_replication(self, show_replication):
        """Sets the show_replication of this ListBackupsRequest.

        是否返回复制记录

        :param show_replication: The show_replication of this ListBackupsRequest.
        :type show_replication: bool
        """
        self._show_replication = show_replication

    @property
    def incremental(self):
        """Gets the incremental of this ListBackupsRequest.

        是否是增备

        :return: The incremental of this ListBackupsRequest.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this ListBackupsRequest.

        是否是增备

        :param incremental: The incremental of this ListBackupsRequest.
        :type incremental: bool
        """
        self._incremental = incremental

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
        if not isinstance(other, ListBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
