# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'name': 'str',
        'limit': 'int',
        'sort_key': 'str',
        'offset': 'int',
        'sort_dir': 'str',
        'status': 'str',
        'metadata': 'str',
        'availability_zone': 'str',
        'multiattach': 'bool',
        'service_type': 'str',
        'dedicated_storage_id': 'str',
        'dedicated_storage_name': 'str',
        'volume_type_id': 'str',
        'id': 'str',
        'ids': 'str',
        'enterprise_project_id': 'str',
        'server_id': 'str',
        'not_metadata': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'name': 'name',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'status': 'status',
        'metadata': 'metadata',
        'availability_zone': 'availability_zone',
        'multiattach': 'multiattach',
        'service_type': 'service_type',
        'dedicated_storage_id': 'dedicated_storage_id',
        'dedicated_storage_name': 'dedicated_storage_name',
        'volume_type_id': 'volume_type_id',
        'id': 'id',
        'ids': 'ids',
        'enterprise_project_id': 'enterprise_project_id',
        'server_id': 'server_id',
        'not_metadata': 'not_metadata'
    }

    def __init__(self, marker=None, name=None, limit=None, sort_key=None, offset=None, sort_dir=None, status=None, metadata=None, availability_zone=None, multiattach=None, service_type=None, dedicated_storage_id=None, dedicated_storage_name=None, volume_type_id=None, id=None, ids=None, enterprise_project_id=None, server_id=None, not_metadata=None):
        r"""ListVolumesRequest

        The model defined in huaweicloud sdk

        :param marker: 通过云硬盘ID进行分页查询。默认为查询第一页数据。
        :type marker: str
        :param name: 磁盘名称。
        :type name: str
        :param limit: 返回结果个数限制。默认值为1000。
        :type limit: int
        :param sort_key: 返回结果按该关键字排序，支持id，status，size，created_at等关键字，默认为“created_at”。
        :type sort_key: str
        :param offset: 偏移量（偏移量为一个大于0小于磁盘总个数的整数，表示查询该偏移量后面的所有的磁盘）。
        :type offset: int
        :param sort_dir: 返回结果按照降序或升序排列，默认为“desc”。 降序：desc 升序：asc
        :type sort_dir: str
        :param status: 云硬盘状态，取值可参考：\&quot;[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)\&quot;。
        :type status: str
        :param metadata: 云硬盘元数据。
        :type metadata: str
        :param availability_zone: 可用区信息。
        :type availability_zone: str
        :param multiattach: 是否为共享云硬盘。 true：表示为共享云硬盘。 false：表示为非共享云硬盘。
        :type multiattach: bool
        :param service_type: 服务类型，仅支持EVS、DSS、DESS。
        :type service_type: str
        :param dedicated_storage_id: 专属存储池ID，可过滤出该专属存储池下的所有云硬盘，必须精确匹配。
        :type dedicated_storage_id: str
        :param dedicated_storage_name: 专属存储池的名字，可过滤出该专属存储池下的所有云硬盘，支持模糊匹配。
        :type dedicated_storage_name: str
        :param volume_type_id: 云硬盘类型id。 通过\&quot;[查询云硬盘类型列表](https://support.huaweicloud.com/api-evs/evs_04_3035.html)\&quot;可以查到，即volume_types参数说明表格中的“id”
        :type volume_type_id: str
        :param id: 云硬盘ID。
        :type id: str
        :param ids: 云硬盘id列表，格式为ids&#x3D;[&#39;id1&#39;,&#39;id2&#39;,...,&#39;idx&#39;]，返回“ids”中有效id的云硬盘详情，无效的id会被忽略。 支持查询最多60个id对应的云硬盘详情。 如果“id”和“ids”查询参数同时存在，“id”会被忽略。
        :type ids: str
        :param enterprise_project_id: 指定企业项目id进行过滤。 传入“all_granted_eps”，代表查询权限范围内的所有企业项目下的云硬盘。 &gt; 说明： &gt;  &gt; 关于企业项目ID的获取及企业项目特性的详细信息，请参考：\&quot;[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\&quot;。
        :type enterprise_project_id: str
        :param server_id: 云服务器id。
        :type server_id: str
        :param not_metadata: 查询不包含所选元数据的云硬盘
        :type not_metadata: str
        """
        
        

        self._marker = None
        self._name = None
        self._limit = None
        self._sort_key = None
        self._offset = None
        self._sort_dir = None
        self._status = None
        self._metadata = None
        self._availability_zone = None
        self._multiattach = None
        self._service_type = None
        self._dedicated_storage_id = None
        self._dedicated_storage_name = None
        self._volume_type_id = None
        self._id = None
        self._ids = None
        self._enterprise_project_id = None
        self._server_id = None
        self._not_metadata = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if status is not None:
            self.status = status
        if metadata is not None:
            self.metadata = metadata
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if multiattach is not None:
            self.multiattach = multiattach
        if service_type is not None:
            self.service_type = service_type
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if dedicated_storage_name is not None:
            self.dedicated_storage_name = dedicated_storage_name
        if volume_type_id is not None:
            self.volume_type_id = volume_type_id
        if id is not None:
            self.id = id
        if ids is not None:
            self.ids = ids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if server_id is not None:
            self.server_id = server_id
        if not_metadata is not None:
            self.not_metadata = not_metadata

    @property
    def marker(self):
        r"""Gets the marker of this ListVolumesRequest.

        通过云硬盘ID进行分页查询。默认为查询第一页数据。

        :return: The marker of this ListVolumesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListVolumesRequest.

        通过云硬盘ID进行分页查询。默认为查询第一页数据。

        :param marker: The marker of this ListVolumesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        r"""Gets the name of this ListVolumesRequest.

        磁盘名称。

        :return: The name of this ListVolumesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListVolumesRequest.

        磁盘名称。

        :param name: The name of this ListVolumesRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListVolumesRequest.

        返回结果个数限制。默认值为1000。

        :return: The limit of this ListVolumesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVolumesRequest.

        返回结果个数限制。默认值为1000。

        :param limit: The limit of this ListVolumesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListVolumesRequest.

        返回结果按该关键字排序，支持id，status，size，created_at等关键字，默认为“created_at”。

        :return: The sort_key of this ListVolumesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListVolumesRequest.

        返回结果按该关键字排序，支持id，status，size，created_at等关键字，默认为“created_at”。

        :param sort_key: The sort_key of this ListVolumesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def offset(self):
        r"""Gets the offset of this ListVolumesRequest.

        偏移量（偏移量为一个大于0小于磁盘总个数的整数，表示查询该偏移量后面的所有的磁盘）。

        :return: The offset of this ListVolumesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVolumesRequest.

        偏移量（偏移量为一个大于0小于磁盘总个数的整数，表示查询该偏移量后面的所有的磁盘）。

        :param offset: The offset of this ListVolumesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListVolumesRequest.

        返回结果按照降序或升序排列，默认为“desc”。 降序：desc 升序：asc

        :return: The sort_dir of this ListVolumesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListVolumesRequest.

        返回结果按照降序或升序排列，默认为“desc”。 降序：desc 升序：asc

        :param sort_dir: The sort_dir of this ListVolumesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def status(self):
        r"""Gets the status of this ListVolumesRequest.

        云硬盘状态，取值可参考：\"[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)\"。

        :return: The status of this ListVolumesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVolumesRequest.

        云硬盘状态，取值可参考：\"[云硬盘状态](https://support.huaweicloud.com/api-evs/evs_04_0040.html)\"。

        :param status: The status of this ListVolumesRequest.
        :type status: str
        """
        self._status = status

    @property
    def metadata(self):
        r"""Gets the metadata of this ListVolumesRequest.

        云硬盘元数据。

        :return: The metadata of this ListVolumesRequest.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListVolumesRequest.

        云硬盘元数据。

        :param metadata: The metadata of this ListVolumesRequest.
        :type metadata: str
        """
        self._metadata = metadata

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListVolumesRequest.

        可用区信息。

        :return: The availability_zone of this ListVolumesRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListVolumesRequest.

        可用区信息。

        :param availability_zone: The availability_zone of this ListVolumesRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def multiattach(self):
        r"""Gets the multiattach of this ListVolumesRequest.

        是否为共享云硬盘。 true：表示为共享云硬盘。 false：表示为非共享云硬盘。

        :return: The multiattach of this ListVolumesRequest.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        r"""Sets the multiattach of this ListVolumesRequest.

        是否为共享云硬盘。 true：表示为共享云硬盘。 false：表示为非共享云硬盘。

        :param multiattach: The multiattach of this ListVolumesRequest.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def service_type(self):
        r"""Gets the service_type of this ListVolumesRequest.

        服务类型，仅支持EVS、DSS、DESS。

        :return: The service_type of this ListVolumesRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListVolumesRequest.

        服务类型，仅支持EVS、DSS、DESS。

        :param service_type: The service_type of this ListVolumesRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def dedicated_storage_id(self):
        r"""Gets the dedicated_storage_id of this ListVolumesRequest.

        专属存储池ID，可过滤出该专属存储池下的所有云硬盘，必须精确匹配。

        :return: The dedicated_storage_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        r"""Sets the dedicated_storage_id of this ListVolumesRequest.

        专属存储池ID，可过滤出该专属存储池下的所有云硬盘，必须精确匹配。

        :param dedicated_storage_id: The dedicated_storage_id of this ListVolumesRequest.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def dedicated_storage_name(self):
        r"""Gets the dedicated_storage_name of this ListVolumesRequest.

        专属存储池的名字，可过滤出该专属存储池下的所有云硬盘，支持模糊匹配。

        :return: The dedicated_storage_name of this ListVolumesRequest.
        :rtype: str
        """
        return self._dedicated_storage_name

    @dedicated_storage_name.setter
    def dedicated_storage_name(self, dedicated_storage_name):
        r"""Sets the dedicated_storage_name of this ListVolumesRequest.

        专属存储池的名字，可过滤出该专属存储池下的所有云硬盘，支持模糊匹配。

        :param dedicated_storage_name: The dedicated_storage_name of this ListVolumesRequest.
        :type dedicated_storage_name: str
        """
        self._dedicated_storage_name = dedicated_storage_name

    @property
    def volume_type_id(self):
        r"""Gets the volume_type_id of this ListVolumesRequest.

        云硬盘类型id。 通过\"[查询云硬盘类型列表](https://support.huaweicloud.com/api-evs/evs_04_3035.html)\"可以查到，即volume_types参数说明表格中的“id”

        :return: The volume_type_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._volume_type_id

    @volume_type_id.setter
    def volume_type_id(self, volume_type_id):
        r"""Sets the volume_type_id of this ListVolumesRequest.

        云硬盘类型id。 通过\"[查询云硬盘类型列表](https://support.huaweicloud.com/api-evs/evs_04_3035.html)\"可以查到，即volume_types参数说明表格中的“id”

        :param volume_type_id: The volume_type_id of this ListVolumesRequest.
        :type volume_type_id: str
        """
        self._volume_type_id = volume_type_id

    @property
    def id(self):
        r"""Gets the id of this ListVolumesRequest.

        云硬盘ID。

        :return: The id of this ListVolumesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVolumesRequest.

        云硬盘ID。

        :param id: The id of this ListVolumesRequest.
        :type id: str
        """
        self._id = id

    @property
    def ids(self):
        r"""Gets the ids of this ListVolumesRequest.

        云硬盘id列表，格式为ids=['id1','id2',...,'idx']，返回“ids”中有效id的云硬盘详情，无效的id会被忽略。 支持查询最多60个id对应的云硬盘详情。 如果“id”和“ids”查询参数同时存在，“id”会被忽略。

        :return: The ids of this ListVolumesRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ListVolumesRequest.

        云硬盘id列表，格式为ids=['id1','id2',...,'idx']，返回“ids”中有效id的云硬盘详情，无效的id会被忽略。 支持查询最多60个id对应的云硬盘详情。 如果“id”和“ids”查询参数同时存在，“id”会被忽略。

        :param ids: The ids of this ListVolumesRequest.
        :type ids: str
        """
        self._ids = ids

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVolumesRequest.

        指定企业项目id进行过滤。 传入“all_granted_eps”，代表查询权限范围内的所有企业项目下的云硬盘。 > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"。

        :return: The enterprise_project_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVolumesRequest.

        指定企业项目id进行过滤。 传入“all_granted_eps”，代表查询权限范围内的所有企业项目下的云硬盘。 > 说明： >  > 关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)\"。

        :param enterprise_project_id: The enterprise_project_id of this ListVolumesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ListVolumesRequest.

        云服务器id。

        :return: The server_id of this ListVolumesRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListVolumesRequest.

        云服务器id。

        :param server_id: The server_id of this ListVolumesRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def not_metadata(self):
        r"""Gets the not_metadata of this ListVolumesRequest.

        查询不包含所选元数据的云硬盘

        :return: The not_metadata of this ListVolumesRequest.
        :rtype: str
        """
        return self._not_metadata

    @not_metadata.setter
    def not_metadata(self, not_metadata):
        r"""Sets the not_metadata of this ListVolumesRequest.

        查询不包含所选元数据的云硬盘

        :param not_metadata: The not_metadata of this ListVolumesRequest.
        :type not_metadata: str
        """
        self._not_metadata = not_metadata

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
        if not isinstance(other, ListVolumesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
