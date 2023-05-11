# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'imagetype': 'str',
        'protected': 'str',
        'id': 'str',
        'visibility': 'str',
        'status': 'str',
        'name': 'str',
        'os_type': 'str',
        'virtual_env_type': 'str',
        'isregistered': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_ascend_310': 'str',
        'support_kvm_hi1822_hiovs': 'str',
        'support_arm': 'str',
        'support_gpu_t4': 'str'
    }

    attribute_map = {
        'imagetype': '__imagetype',
        'protected': 'protected',
        'id': 'id',
        'visibility': 'visibility',
        'status': 'status',
        'name': 'name',
        'os_type': '__os_type',
        'virtual_env_type': 'virtual_env_type',
        'isregistered': '__isregistered',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_ascend_310': '__support_kvm_ascend_310',
        'support_kvm_hi1822_hiovs': '__support_kvm_hi1822_hiovs',
        'support_arm': '__support_arm',
        'support_gpu_t4': '__support_gpu_t4'
    }

    def __init__(self, imagetype=None, protected=None, id=None, visibility=None, status=None, name=None, os_type=None, virtual_env_type=None, isregistered=None, limit=None, offset=None, sort_key=None, sort_dir=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_ascend_310=None, support_kvm_hi1822_hiovs=None, support_arm=None, support_gpu_t4=None):
        """ListImagesRequest

        The model defined in huaweicloud sdk

        :param imagetype: 镜像类型，目前支持以下类型：  - 公共镜像：gold  - 私有镜像：private
        :type imagetype: str
        :param protected: 镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。
        :type protected: str
        :param id: 镜像ID，精确匹配。
        :type id: str
        :param visibility: 是否被其他租户可见，取值如下：  - public：公共镜像  - private：私有镜像
        :type visibility: str
        :param status: 镜像状态。取值如下：  - saving：表示镜像正在上传文件到后端存储  - deleted：表示镜像已经删除  - killed：表示镜像上传错误  - active：表示镜像可以正常使用
        :type status: str
        :param name: 镜像名称，匹配规则为精确匹配。
        :type name: str
        :param os_type: 镜像系统类型，取值如下：  - Linux - Windows - Other
        :type os_type: str
        :param virtual_env_type: 镜像使用环境类型。  目前仅支持系统盘镜像，取值为：FusionCompute
        :type virtual_env_type: str
        :param isregistered: 镜像是否可用，取值为true/false。 &gt; 查询公共镜像时，该参数无效。
        :type isregistered: str
        :param limit: 用于分页，表示查询几条镜像记录，取值为正整数，最大（默认）取值为500
        :type limit: int
        :param offset: 用于分页，表示查询偏移量，表示从整个列表查询结果中的该位置向后进行查询，并非页数偏移，默认取值为0，表示查询第一页。
        :type offset: int
        :param sort_key: 用于排序，表示按照哪个字段排序，取值为镜像属性name、status、disk_format、created_at，默认取值为created_at。
        :type sort_key: str
        :param sort_dir: 用于排序，表示升序还是降序，取值为asc和desc，与sort_key一起组合使用，默认为降序desc。
        :type sort_dir: str
        :param support_kvm: 如果镜像支持KVM，取值为true，否则无该属性。
        :type support_kvm: str
        :param support_kvm_gpu_type: 如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。
        :type support_kvm_gpu_type: str
        :param support_kvm_ascend_310: 如果镜像支持AI加速，取值为true，否则无该属性。
        :type support_kvm_ascend_310: str
        :param support_kvm_hi1822_hiovs: 如果镜像支持计算增强，取值为true，否则无该属性。
        :type support_kvm_hi1822_hiovs: str
        :param support_arm: 如果镜像为ARM架构类型，取值为true，否则无该属性。
        :type support_arm: str
        :param support_gpu_t4: 如果镜像支持GPU T4，取值为true，否则无该属性。
        :type support_gpu_t4: str
        """
        
        

        self._imagetype = None
        self._protected = None
        self._id = None
        self._visibility = None
        self._status = None
        self._name = None
        self._os_type = None
        self._virtual_env_type = None
        self._isregistered = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_ascend_310 = None
        self._support_kvm_hi1822_hiovs = None
        self._support_arm = None
        self._support_gpu_t4 = None
        self.discriminator = None

        if imagetype is not None:
            self.imagetype = imagetype
        if protected is not None:
            self.protected = protected
        if id is not None:
            self.id = id
        if visibility is not None:
            self.visibility = visibility
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if os_type is not None:
            self.os_type = os_type
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if isregistered is not None:
            self.isregistered = isregistered
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if support_kvm is not None:
            self.support_kvm = support_kvm
        if support_kvm_gpu_type is not None:
            self.support_kvm_gpu_type = support_kvm_gpu_type
        if support_kvm_ascend_310 is not None:
            self.support_kvm_ascend_310 = support_kvm_ascend_310
        if support_kvm_hi1822_hiovs is not None:
            self.support_kvm_hi1822_hiovs = support_kvm_hi1822_hiovs
        if support_arm is not None:
            self.support_arm = support_arm
        if support_gpu_t4 is not None:
            self.support_gpu_t4 = support_gpu_t4

    @property
    def imagetype(self):
        """Gets the imagetype of this ListImagesRequest.

        镜像类型，目前支持以下类型：  - 公共镜像：gold  - 私有镜像：private

        :return: The imagetype of this ListImagesRequest.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this ListImagesRequest.

        镜像类型，目前支持以下类型：  - 公共镜像：gold  - 私有镜像：private

        :param imagetype: The imagetype of this ListImagesRequest.
        :type imagetype: str
        """
        self._imagetype = imagetype

    @property
    def protected(self):
        """Gets the protected of this ListImagesRequest.

        镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。

        :return: The protected of this ListImagesRequest.
        :rtype: str
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this ListImagesRequest.

        镜像是否是受保护，取值为true/false，一般查询公共镜像时候取值为true，查询私有镜像可以不指定。

        :param protected: The protected of this ListImagesRequest.
        :type protected: str
        """
        self._protected = protected

    @property
    def id(self):
        """Gets the id of this ListImagesRequest.

        镜像ID，精确匹配。

        :return: The id of this ListImagesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListImagesRequest.

        镜像ID，精确匹配。

        :param id: The id of this ListImagesRequest.
        :type id: str
        """
        self._id = id

    @property
    def visibility(self):
        """Gets the visibility of this ListImagesRequest.

        是否被其他租户可见，取值如下：  - public：公共镜像  - private：私有镜像

        :return: The visibility of this ListImagesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ListImagesRequest.

        是否被其他租户可见，取值如下：  - public：公共镜像  - private：私有镜像

        :param visibility: The visibility of this ListImagesRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def status(self):
        """Gets the status of this ListImagesRequest.

        镜像状态。取值如下：  - saving：表示镜像正在上传文件到后端存储  - deleted：表示镜像已经删除  - killed：表示镜像上传错误  - active：表示镜像可以正常使用

        :return: The status of this ListImagesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListImagesRequest.

        镜像状态。取值如下：  - saving：表示镜像正在上传文件到后端存储  - deleted：表示镜像已经删除  - killed：表示镜像上传错误  - active：表示镜像可以正常使用

        :param status: The status of this ListImagesRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this ListImagesRequest.

        镜像名称，匹配规则为精确匹配。

        :return: The name of this ListImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListImagesRequest.

        镜像名称，匹配规则为精确匹配。

        :param name: The name of this ListImagesRequest.
        :type name: str
        """
        self._name = name

    @property
    def os_type(self):
        """Gets the os_type of this ListImagesRequest.

        镜像系统类型，取值如下：  - Linux - Windows - Other

        :return: The os_type of this ListImagesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListImagesRequest.

        镜像系统类型，取值如下：  - Linux - Windows - Other

        :param os_type: The os_type of this ListImagesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this ListImagesRequest.

        镜像使用环境类型。  目前仅支持系统盘镜像，取值为：FusionCompute

        :return: The virtual_env_type of this ListImagesRequest.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this ListImagesRequest.

        镜像使用环境类型。  目前仅支持系统盘镜像，取值为：FusionCompute

        :param virtual_env_type: The virtual_env_type of this ListImagesRequest.
        :type virtual_env_type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def isregistered(self):
        """Gets the isregistered of this ListImagesRequest.

        镜像是否可用，取值为true/false。 > 查询公共镜像时，该参数无效。

        :return: The isregistered of this ListImagesRequest.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this ListImagesRequest.

        镜像是否可用，取值为true/false。 > 查询公共镜像时，该参数无效。

        :param isregistered: The isregistered of this ListImagesRequest.
        :type isregistered: str
        """
        self._isregistered = isregistered

    @property
    def limit(self):
        """Gets the limit of this ListImagesRequest.

        用于分页，表示查询几条镜像记录，取值为正整数，最大（默认）取值为500

        :return: The limit of this ListImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListImagesRequest.

        用于分页，表示查询几条镜像记录，取值为正整数，最大（默认）取值为500

        :param limit: The limit of this ListImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListImagesRequest.

        用于分页，表示查询偏移量，表示从整个列表查询结果中的该位置向后进行查询，并非页数偏移，默认取值为0，表示查询第一页。

        :return: The offset of this ListImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListImagesRequest.

        用于分页，表示查询偏移量，表示从整个列表查询结果中的该位置向后进行查询，并非页数偏移，默认取值为0，表示查询第一页。

        :param offset: The offset of this ListImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        """Gets the sort_key of this ListImagesRequest.

        用于排序，表示按照哪个字段排序，取值为镜像属性name、status、disk_format、created_at，默认取值为created_at。

        :return: The sort_key of this ListImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListImagesRequest.

        用于排序，表示按照哪个字段排序，取值为镜像属性name、status、disk_format、created_at，默认取值为created_at。

        :param sort_key: The sort_key of this ListImagesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListImagesRequest.

        用于排序，表示升序还是降序，取值为asc和desc，与sort_key一起组合使用，默认为降序desc。

        :return: The sort_dir of this ListImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListImagesRequest.

        用于排序，表示升序还是降序，取值为asc和desc，与sort_key一起组合使用，默认为降序desc。

        :param sort_dir: The sort_dir of this ListImagesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def support_kvm(self):
        """Gets the support_kvm of this ListImagesRequest.

        如果镜像支持KVM，取值为true，否则无该属性。

        :return: The support_kvm of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        """Sets the support_kvm of this ListImagesRequest.

        如果镜像支持KVM，取值为true，否则无该属性。

        :param support_kvm: The support_kvm of this ListImagesRequest.
        :type support_kvm: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        """Gets the support_kvm_gpu_type of this ListImagesRequest.

        如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。

        :return: The support_kvm_gpu_type of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        """Sets the support_kvm_gpu_type of this ListImagesRequest.

        如果镜像是支持KVM虚拟化平台下的GPU类型，取值为“V100_vGPU”或者“RTX5000”，否则无该属性。

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this ListImagesRequest.
        :type support_kvm_gpu_type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_ascend_310(self):
        """Gets the support_kvm_ascend_310 of this ListImagesRequest.

        如果镜像支持AI加速，取值为true，否则无该属性。

        :return: The support_kvm_ascend_310 of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_ascend_310

    @support_kvm_ascend_310.setter
    def support_kvm_ascend_310(self, support_kvm_ascend_310):
        """Sets the support_kvm_ascend_310 of this ListImagesRequest.

        如果镜像支持AI加速，取值为true，否则无该属性。

        :param support_kvm_ascend_310: The support_kvm_ascend_310 of this ListImagesRequest.
        :type support_kvm_ascend_310: str
        """
        self._support_kvm_ascend_310 = support_kvm_ascend_310

    @property
    def support_kvm_hi1822_hiovs(self):
        """Gets the support_kvm_hi1822_hiovs of this ListImagesRequest.

        如果镜像支持计算增强，取值为true，否则无该属性。

        :return: The support_kvm_hi1822_hiovs of this ListImagesRequest.
        :rtype: str
        """
        return self._support_kvm_hi1822_hiovs

    @support_kvm_hi1822_hiovs.setter
    def support_kvm_hi1822_hiovs(self, support_kvm_hi1822_hiovs):
        """Sets the support_kvm_hi1822_hiovs of this ListImagesRequest.

        如果镜像支持计算增强，取值为true，否则无该属性。

        :param support_kvm_hi1822_hiovs: The support_kvm_hi1822_hiovs of this ListImagesRequest.
        :type support_kvm_hi1822_hiovs: str
        """
        self._support_kvm_hi1822_hiovs = support_kvm_hi1822_hiovs

    @property
    def support_arm(self):
        """Gets the support_arm of this ListImagesRequest.

        如果镜像为ARM架构类型，取值为true，否则无该属性。

        :return: The support_arm of this ListImagesRequest.
        :rtype: str
        """
        return self._support_arm

    @support_arm.setter
    def support_arm(self, support_arm):
        """Sets the support_arm of this ListImagesRequest.

        如果镜像为ARM架构类型，取值为true，否则无该属性。

        :param support_arm: The support_arm of this ListImagesRequest.
        :type support_arm: str
        """
        self._support_arm = support_arm

    @property
    def support_gpu_t4(self):
        """Gets the support_gpu_t4 of this ListImagesRequest.

        如果镜像支持GPU T4，取值为true，否则无该属性。

        :return: The support_gpu_t4 of this ListImagesRequest.
        :rtype: str
        """
        return self._support_gpu_t4

    @support_gpu_t4.setter
    def support_gpu_t4(self, support_gpu_t4):
        """Sets the support_gpu_t4 of this ListImagesRequest.

        如果镜像支持GPU T4，取值为true，否则无该属性。

        :param support_gpu_t4: The support_gpu_t4 of this ListImagesRequest.
        :type support_gpu_t4: str
        """
        self._support_gpu_t4 = support_gpu_t4

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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
