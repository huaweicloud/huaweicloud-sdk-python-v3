# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionTemplateRequest:

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
        'maxitems': 'str',
        'ispublic': 'str',
        'runtime': 'str',
        'scene': 'str',
        'service': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'maxitems': 'maxitems',
        'ispublic': 'ispublic',
        'runtime': 'runtime',
        'scene': 'scene',
        'service': 'service'
    }

    def __init__(self, marker=None, maxitems=None, ispublic=None, runtime=None, scene=None, service=None):
        r"""ListFunctionTemplateRequest

        The model defined in huaweicloud sdk

        :param marker: 本次查询起始位置，默认值0
        :type marker: str
        :param maxitems: 每次查询获取的最大模板数量。
        :type maxitems: str
        :param ispublic: 是否为公开模板
        :type ispublic: str
        :param runtime: 指定运行时模板
        :type runtime: str
        :param scene: 指定场景模板
        :type scene: str
        :param service: 指定云服务模板
        :type service: str
        """
        
        

        self._marker = None
        self._maxitems = None
        self._ispublic = None
        self._runtime = None
        self._scene = None
        self._service = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if maxitems is not None:
            self.maxitems = maxitems
        if ispublic is not None:
            self.ispublic = ispublic
        if runtime is not None:
            self.runtime = runtime
        if scene is not None:
            self.scene = scene
        if service is not None:
            self.service = service

    @property
    def marker(self):
        r"""Gets the marker of this ListFunctionTemplateRequest.

        本次查询起始位置，默认值0

        :return: The marker of this ListFunctionTemplateRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFunctionTemplateRequest.

        本次查询起始位置，默认值0

        :param marker: The marker of this ListFunctionTemplateRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def maxitems(self):
        r"""Gets the maxitems of this ListFunctionTemplateRequest.

        每次查询获取的最大模板数量。

        :return: The maxitems of this ListFunctionTemplateRequest.
        :rtype: str
        """
        return self._maxitems

    @maxitems.setter
    def maxitems(self, maxitems):
        r"""Sets the maxitems of this ListFunctionTemplateRequest.

        每次查询获取的最大模板数量。

        :param maxitems: The maxitems of this ListFunctionTemplateRequest.
        :type maxitems: str
        """
        self._maxitems = maxitems

    @property
    def ispublic(self):
        r"""Gets the ispublic of this ListFunctionTemplateRequest.

        是否为公开模板

        :return: The ispublic of this ListFunctionTemplateRequest.
        :rtype: str
        """
        return self._ispublic

    @ispublic.setter
    def ispublic(self, ispublic):
        r"""Sets the ispublic of this ListFunctionTemplateRequest.

        是否为公开模板

        :param ispublic: The ispublic of this ListFunctionTemplateRequest.
        :type ispublic: str
        """
        self._ispublic = ispublic

    @property
    def runtime(self):
        r"""Gets the runtime of this ListFunctionTemplateRequest.

        指定运行时模板

        :return: The runtime of this ListFunctionTemplateRequest.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ListFunctionTemplateRequest.

        指定运行时模板

        :param runtime: The runtime of this ListFunctionTemplateRequest.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def scene(self):
        r"""Gets the scene of this ListFunctionTemplateRequest.

        指定场景模板

        :return: The scene of this ListFunctionTemplateRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListFunctionTemplateRequest.

        指定场景模板

        :param scene: The scene of this ListFunctionTemplateRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def service(self):
        r"""Gets the service of this ListFunctionTemplateRequest.

        指定云服务模板

        :return: The service of this ListFunctionTemplateRequest.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this ListFunctionTemplateRequest.

        指定云服务模板

        :param service: The service of this ListFunctionTemplateRequest.
        :type service: str
        """
        self._service = service

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
        if not isinstance(other, ListFunctionTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
