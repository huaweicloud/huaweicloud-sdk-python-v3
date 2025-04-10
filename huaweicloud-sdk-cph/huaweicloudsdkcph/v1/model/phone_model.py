# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhoneModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_model_name': 'str',
        'phone_model_name': 'str',
        'status': 'int',
        'cpu': 'int',
        'memory': 'int',
        'disk': 'int',
        'resolution': 'str',
        'extend_spec': 'str',
        'spec_code': 'str',
        'phone_capacity': 'int',
        'image_label': 'str',
        'product_type': 'int',
        'phone_model_version': 'int',
        'dpi': 'int',
        'fps': 'str',
        'volume_mode': 'int',
        'render_fps': 'int',
        'stream_fps': 'int'
    }

    attribute_map = {
        'server_model_name': 'server_model_name',
        'phone_model_name': 'phone_model_name',
        'status': 'status',
        'cpu': 'cpu',
        'memory': 'memory',
        'disk': 'disk',
        'resolution': 'resolution',
        'extend_spec': 'extend_spec',
        'spec_code': 'spec_code',
        'phone_capacity': 'phone_capacity',
        'image_label': 'image_label',
        'product_type': 'product_type',
        'phone_model_version': 'phone_model_version',
        'dpi': 'dpi',
        'fps': 'fps',
        'volume_mode': 'volume_mode',
        'render_fps': 'render_fps',
        'stream_fps': 'stream_fps'
    }

    def __init__(self, server_model_name=None, phone_model_name=None, status=None, cpu=None, memory=None, disk=None, resolution=None, extend_spec=None, spec_code=None, phone_capacity=None, image_label=None, product_type=None, phone_model_version=None, dpi=None, fps=None, volume_mode=None, render_fps=None, stream_fps=None):
        r"""PhoneModel

        The model defined in huaweicloud sdk

        :param server_model_name: 云手机服务器的规格名称，不超过64个字节。
        :type server_model_name: str
        :param phone_model_name: 云手机的规格名称，不超过64个字节。
        :type phone_model_name: str
        :param status: 规格状态。 - 1 表示正常使用状态 - 0 表示已下线状态 已下线的规格不可用来购买云手机服务器
        :type status: int
        :param cpu: CPU核数。
        :type cpu: int
        :param memory: 内存大小，单位：MB。
        :type memory: int
        :param disk: 系统存储大小，单位：GiB。
        :type disk: int
        :param resolution: 分辨率，不超过16个字节。
        :type resolution: str
        :param extend_spec: 扩展描述，不超过512个字节。
        :type extend_spec: str
        :param spec_code: 规格名称，不超过64个字节。
        :type spec_code: str
        :param phone_capacity: 当前云手机规格包含的云手机个数。
        :type phone_capacity: int
        :param image_label: 镜像类型，只支持如下类型： - qemu_phone - cloud_phone - cloud_phone_1620 - cloud_game - cloud_game_1620
        :type image_label: str
        :param product_type: 产品类型。 - 0：云手机 - 1：云手游
        :type product_type: int
        :param phone_model_version: 规格版本： - 0：规格1.0 - 1：规格2.0
        :type phone_model_version: int
        :param dpi: 每英寸点数。
        :type dpi: int
        :param fps: 渲染帧率。
        :type fps: str
        :param volume_mode: 手机物理磁盘是否独立。 - 0：不独立 - 1：独立
        :type volume_mode: int
        :param render_fps: 渲染帧率。
        :type render_fps: int
        :param stream_fps: 出流帧率。
        :type stream_fps: int
        """
        
        

        self._server_model_name = None
        self._phone_model_name = None
        self._status = None
        self._cpu = None
        self._memory = None
        self._disk = None
        self._resolution = None
        self._extend_spec = None
        self._spec_code = None
        self._phone_capacity = None
        self._image_label = None
        self._product_type = None
        self._phone_model_version = None
        self._dpi = None
        self._fps = None
        self._volume_mode = None
        self._render_fps = None
        self._stream_fps = None
        self.discriminator = None

        if server_model_name is not None:
            self.server_model_name = server_model_name
        if phone_model_name is not None:
            self.phone_model_name = phone_model_name
        if status is not None:
            self.status = status
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if disk is not None:
            self.disk = disk
        if resolution is not None:
            self.resolution = resolution
        if extend_spec is not None:
            self.extend_spec = extend_spec
        if spec_code is not None:
            self.spec_code = spec_code
        if phone_capacity is not None:
            self.phone_capacity = phone_capacity
        if image_label is not None:
            self.image_label = image_label
        if product_type is not None:
            self.product_type = product_type
        if phone_model_version is not None:
            self.phone_model_version = phone_model_version
        if dpi is not None:
            self.dpi = dpi
        if fps is not None:
            self.fps = fps
        if volume_mode is not None:
            self.volume_mode = volume_mode
        if render_fps is not None:
            self.render_fps = render_fps
        if stream_fps is not None:
            self.stream_fps = stream_fps

    @property
    def server_model_name(self):
        r"""Gets the server_model_name of this PhoneModel.

        云手机服务器的规格名称，不超过64个字节。

        :return: The server_model_name of this PhoneModel.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        r"""Sets the server_model_name of this PhoneModel.

        云手机服务器的规格名称，不超过64个字节。

        :param server_model_name: The server_model_name of this PhoneModel.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def phone_model_name(self):
        r"""Gets the phone_model_name of this PhoneModel.

        云手机的规格名称，不超过64个字节。

        :return: The phone_model_name of this PhoneModel.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        r"""Sets the phone_model_name of this PhoneModel.

        云手机的规格名称，不超过64个字节。

        :param phone_model_name: The phone_model_name of this PhoneModel.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def status(self):
        r"""Gets the status of this PhoneModel.

        规格状态。 - 1 表示正常使用状态 - 0 表示已下线状态 已下线的规格不可用来购买云手机服务器

        :return: The status of this PhoneModel.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PhoneModel.

        规格状态。 - 1 表示正常使用状态 - 0 表示已下线状态 已下线的规格不可用来购买云手机服务器

        :param status: The status of this PhoneModel.
        :type status: int
        """
        self._status = status

    @property
    def cpu(self):
        r"""Gets the cpu of this PhoneModel.

        CPU核数。

        :return: The cpu of this PhoneModel.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this PhoneModel.

        CPU核数。

        :param cpu: The cpu of this PhoneModel.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this PhoneModel.

        内存大小，单位：MB。

        :return: The memory of this PhoneModel.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this PhoneModel.

        内存大小，单位：MB。

        :param memory: The memory of this PhoneModel.
        :type memory: int
        """
        self._memory = memory

    @property
    def disk(self):
        r"""Gets the disk of this PhoneModel.

        系统存储大小，单位：GiB。

        :return: The disk of this PhoneModel.
        :rtype: int
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this PhoneModel.

        系统存储大小，单位：GiB。

        :param disk: The disk of this PhoneModel.
        :type disk: int
        """
        self._disk = disk

    @property
    def resolution(self):
        r"""Gets the resolution of this PhoneModel.

        分辨率，不超过16个字节。

        :return: The resolution of this PhoneModel.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        r"""Sets the resolution of this PhoneModel.

        分辨率，不超过16个字节。

        :param resolution: The resolution of this PhoneModel.
        :type resolution: str
        """
        self._resolution = resolution

    @property
    def extend_spec(self):
        r"""Gets the extend_spec of this PhoneModel.

        扩展描述，不超过512个字节。

        :return: The extend_spec of this PhoneModel.
        :rtype: str
        """
        return self._extend_spec

    @extend_spec.setter
    def extend_spec(self, extend_spec):
        r"""Sets the extend_spec of this PhoneModel.

        扩展描述，不超过512个字节。

        :param extend_spec: The extend_spec of this PhoneModel.
        :type extend_spec: str
        """
        self._extend_spec = extend_spec

    @property
    def spec_code(self):
        r"""Gets the spec_code of this PhoneModel.

        规格名称，不超过64个字节。

        :return: The spec_code of this PhoneModel.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this PhoneModel.

        规格名称，不超过64个字节。

        :param spec_code: The spec_code of this PhoneModel.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def phone_capacity(self):
        r"""Gets the phone_capacity of this PhoneModel.

        当前云手机规格包含的云手机个数。

        :return: The phone_capacity of this PhoneModel.
        :rtype: int
        """
        return self._phone_capacity

    @phone_capacity.setter
    def phone_capacity(self, phone_capacity):
        r"""Sets the phone_capacity of this PhoneModel.

        当前云手机规格包含的云手机个数。

        :param phone_capacity: The phone_capacity of this PhoneModel.
        :type phone_capacity: int
        """
        self._phone_capacity = phone_capacity

    @property
    def image_label(self):
        r"""Gets the image_label of this PhoneModel.

        镜像类型，只支持如下类型： - qemu_phone - cloud_phone - cloud_phone_1620 - cloud_game - cloud_game_1620

        :return: The image_label of this PhoneModel.
        :rtype: str
        """
        return self._image_label

    @image_label.setter
    def image_label(self, image_label):
        r"""Sets the image_label of this PhoneModel.

        镜像类型，只支持如下类型： - qemu_phone - cloud_phone - cloud_phone_1620 - cloud_game - cloud_game_1620

        :param image_label: The image_label of this PhoneModel.
        :type image_label: str
        """
        self._image_label = image_label

    @property
    def product_type(self):
        r"""Gets the product_type of this PhoneModel.

        产品类型。 - 0：云手机 - 1：云手游

        :return: The product_type of this PhoneModel.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this PhoneModel.

        产品类型。 - 0：云手机 - 1：云手游

        :param product_type: The product_type of this PhoneModel.
        :type product_type: int
        """
        self._product_type = product_type

    @property
    def phone_model_version(self):
        r"""Gets the phone_model_version of this PhoneModel.

        规格版本： - 0：规格1.0 - 1：规格2.0

        :return: The phone_model_version of this PhoneModel.
        :rtype: int
        """
        return self._phone_model_version

    @phone_model_version.setter
    def phone_model_version(self, phone_model_version):
        r"""Sets the phone_model_version of this PhoneModel.

        规格版本： - 0：规格1.0 - 1：规格2.0

        :param phone_model_version: The phone_model_version of this PhoneModel.
        :type phone_model_version: int
        """
        self._phone_model_version = phone_model_version

    @property
    def dpi(self):
        r"""Gets the dpi of this PhoneModel.

        每英寸点数。

        :return: The dpi of this PhoneModel.
        :rtype: int
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        r"""Sets the dpi of this PhoneModel.

        每英寸点数。

        :param dpi: The dpi of this PhoneModel.
        :type dpi: int
        """
        self._dpi = dpi

    @property
    def fps(self):
        r"""Gets the fps of this PhoneModel.

        渲染帧率。

        :return: The fps of this PhoneModel.
        :rtype: str
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        r"""Sets the fps of this PhoneModel.

        渲染帧率。

        :param fps: The fps of this PhoneModel.
        :type fps: str
        """
        self._fps = fps

    @property
    def volume_mode(self):
        r"""Gets the volume_mode of this PhoneModel.

        手机物理磁盘是否独立。 - 0：不独立 - 1：独立

        :return: The volume_mode of this PhoneModel.
        :rtype: int
        """
        return self._volume_mode

    @volume_mode.setter
    def volume_mode(self, volume_mode):
        r"""Sets the volume_mode of this PhoneModel.

        手机物理磁盘是否独立。 - 0：不独立 - 1：独立

        :param volume_mode: The volume_mode of this PhoneModel.
        :type volume_mode: int
        """
        self._volume_mode = volume_mode

    @property
    def render_fps(self):
        r"""Gets the render_fps of this PhoneModel.

        渲染帧率。

        :return: The render_fps of this PhoneModel.
        :rtype: int
        """
        return self._render_fps

    @render_fps.setter
    def render_fps(self, render_fps):
        r"""Sets the render_fps of this PhoneModel.

        渲染帧率。

        :param render_fps: The render_fps of this PhoneModel.
        :type render_fps: int
        """
        self._render_fps = render_fps

    @property
    def stream_fps(self):
        r"""Gets the stream_fps of this PhoneModel.

        出流帧率。

        :return: The stream_fps of this PhoneModel.
        :rtype: int
        """
        return self._stream_fps

    @stream_fps.setter
    def stream_fps(self, stream_fps):
        r"""Sets the stream_fps of this PhoneModel.

        出流帧率。

        :param stream_fps: The stream_fps of this PhoneModel.
        :type stream_fps: int
        """
        self._stream_fps = stream_fps

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
        if not isinstance(other, PhoneModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
