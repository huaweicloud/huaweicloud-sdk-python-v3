# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskCheckSettingsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cfg_key': 'str',
        'status': 'str',
        'cfg_value': 'str'
    }

    attribute_map = {
        'cfg_key': 'cfg_key',
        'status': 'status',
        'cfg_value': 'cfg_value'
    }

    def __init__(self, cfg_key=None, status=None, cfg_value=None):
        r"""TaskCheckSettingsItem

        The model defined in huaweicloud sdk

        :param cfg_key: **参数解释:** 规则集对应的编译配置条件键。 **约束限制:** 不涉及。 **取值范围:** - compileTool：编译工具。 - buildToolVersion：编译工具版本。 - compileScriptCmd：编译命令。 **默认取值：** 不涉及。
        :type cfg_key: str
        :param status: **参数解释:** 当前检查参数key对应的开启状态，填写\&quot;on\&quot;即可。 **约束限制:** 不涉及。 **取值范围:** \&quot;on\&quot;。 **默认取值：** 不涉及。
        :type status: str
        :param cfg_value: **参数解释:** 规则集对应的编译配置值。 **约束限制:** cfg_key为compileTool、buildToolVersion时，cfg_value的值必填。 **取值范围:** - ant1.10.1-jdk1.8: ant镜像。 - ant1.10.13-jdk1.8: ant镜像。 - ant1.10.3-jdk1.8: ant镜像。 - ant1.9.4-jdk1.8: ant镜像。 - cmake2.8.12-gcc4.8.5: C++镜像。 - cmake2.8.12-gcc5.5.0: C++镜像。 - cmake2.8.12-gcc6.4.0: C++镜像。 - cmake2.8.12-gcc7.3.0: C++镜像。 - cmake3.10.1-gcc4.8.5: C++镜像。 - cmake3.10.1-gcc5.5.0: C++镜像。 - cmake3.10.1-gcc6.4.0: C++镜像。 - cmake3.10.1-gcc7.3.0: C++镜像。 - cmake3.15.5-gcc7.5.0: C++镜像。 - cmake3.15.5-gcc8.3.0: C++镜像。 - cmake3.16.0-gcc9.2.0: C++镜像。 - dotnetcore2.2: C#镜像。 - dotnetcore3.0: C#镜像。 - dotnetcore3.1: C#镜像。 - dotnetcore5.0: C#镜像。 - dotnetcore6.0: C#镜像。 - dotnetcore7.0: C#镜像。 - dotnetcore8.0: C#镜像。 - dotnetcore9.0: C#镜像。 - go-1.10.3: go镜像。 - go-1.11.6: go镜像。 - go-1.12.1: go镜像。 - go-1.23: go镜像。 - gradle2.13-jdk1.8: gradle镜像。 - gradle2.14.1-jdk1.8: gradle镜像。 - gradle3.3-jdk1.8: gradle镜像。 - gradle4.1-jdk1.8: gradle镜像。 - gradle4.2-jdk1.8: gradle镜像。 - gradle4.3-jdk1.8: gradle镜像。 - gradle4.4-jdk1.8: gradle镜像。 - gradle4.5-jdk1.8: gradle镜像。 - gradle4.6-jdk1.8: gradle镜像。 - gradle4.7-jdk1.8: gradle镜像。 - gradle4.8-jdk1.8: gradle镜像。 - gradle4.8-jdk1.9: gradle镜像。 - gradle4.9-jdk1.8: gradle镜像。 - gradle4.9-jdk1.9: gradle镜像。 - gradlew: gradle镜像。 - maven3.3.1-jdk7: maven镜像。 - maven3.5.3-jdk1.10: maven镜像。 - maven3.5.3-jdk1.11: maven镜像。 - maven3.5.3-jdk1.7: maven镜像。 - maven3.5.3-jdk1.8: maven镜像。 - maven3.5.3-jdk1.9: maven镜像。 - maven3.5.3-jdk7: maven镜像。 - maven3.5.3-jdk8-open: maven镜像。 - maven3.6.1-jdk10: maven镜像。 - maven3.6.1-jdk9: maven镜像。 - maven3.6.3-jdk11: maven镜像。 - maven3.8.5-jdk1.17: maven镜像。 - maven3.8.5-jdk17: maven镜像。 - maven3.9.5-jdk21: maven镜像。 - mono6-msbuild16-dotnetcoresdk2.1: C#镜像。 - mono6-msbuild16-dotnetcoresdk2.2: C#镜像。 - mono6-msbuild16-dotnetcoresdk3.0: C#镜像。 - mono6-msbuild16-dotnetcoresdk3.1: C#镜像。 - mono6-msbuild16-dotnetcoresdk5.0: C#镜像。 - mono6-msbuild16-dotnetcoresdk6.0: C#镜像。 - msbuild15-dotnetframework3.5: C#镜像。 - msbuild15-dotnetframework4.7.2: C#镜像。 - msbuild16-dotnetframework4.8: C#镜像。 **默认取值：** 不涉及。
        :type cfg_value: str
        """
        
        

        self._cfg_key = None
        self._status = None
        self._cfg_value = None
        self.discriminator = None

        if cfg_key is not None:
            self.cfg_key = cfg_key
        if status is not None:
            self.status = status
        if cfg_value is not None:
            self.cfg_value = cfg_value

    @property
    def cfg_key(self):
        r"""Gets the cfg_key of this TaskCheckSettingsItem.

        **参数解释:** 规则集对应的编译配置条件键。 **约束限制:** 不涉及。 **取值范围:** - compileTool：编译工具。 - buildToolVersion：编译工具版本。 - compileScriptCmd：编译命令。 **默认取值：** 不涉及。

        :return: The cfg_key of this TaskCheckSettingsItem.
        :rtype: str
        """
        return self._cfg_key

    @cfg_key.setter
    def cfg_key(self, cfg_key):
        r"""Sets the cfg_key of this TaskCheckSettingsItem.

        **参数解释:** 规则集对应的编译配置条件键。 **约束限制:** 不涉及。 **取值范围:** - compileTool：编译工具。 - buildToolVersion：编译工具版本。 - compileScriptCmd：编译命令。 **默认取值：** 不涉及。

        :param cfg_key: The cfg_key of this TaskCheckSettingsItem.
        :type cfg_key: str
        """
        self._cfg_key = cfg_key

    @property
    def status(self):
        r"""Gets the status of this TaskCheckSettingsItem.

        **参数解释:** 当前检查参数key对应的开启状态，填写\"on\"即可。 **约束限制:** 不涉及。 **取值范围:** \"on\"。 **默认取值：** 不涉及。

        :return: The status of this TaskCheckSettingsItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskCheckSettingsItem.

        **参数解释:** 当前检查参数key对应的开启状态，填写\"on\"即可。 **约束限制:** 不涉及。 **取值范围:** \"on\"。 **默认取值：** 不涉及。

        :param status: The status of this TaskCheckSettingsItem.
        :type status: str
        """
        self._status = status

    @property
    def cfg_value(self):
        r"""Gets the cfg_value of this TaskCheckSettingsItem.

        **参数解释:** 规则集对应的编译配置值。 **约束限制:** cfg_key为compileTool、buildToolVersion时，cfg_value的值必填。 **取值范围:** - ant1.10.1-jdk1.8: ant镜像。 - ant1.10.13-jdk1.8: ant镜像。 - ant1.10.3-jdk1.8: ant镜像。 - ant1.9.4-jdk1.8: ant镜像。 - cmake2.8.12-gcc4.8.5: C++镜像。 - cmake2.8.12-gcc5.5.0: C++镜像。 - cmake2.8.12-gcc6.4.0: C++镜像。 - cmake2.8.12-gcc7.3.0: C++镜像。 - cmake3.10.1-gcc4.8.5: C++镜像。 - cmake3.10.1-gcc5.5.0: C++镜像。 - cmake3.10.1-gcc6.4.0: C++镜像。 - cmake3.10.1-gcc7.3.0: C++镜像。 - cmake3.15.5-gcc7.5.0: C++镜像。 - cmake3.15.5-gcc8.3.0: C++镜像。 - cmake3.16.0-gcc9.2.0: C++镜像。 - dotnetcore2.2: C#镜像。 - dotnetcore3.0: C#镜像。 - dotnetcore3.1: C#镜像。 - dotnetcore5.0: C#镜像。 - dotnetcore6.0: C#镜像。 - dotnetcore7.0: C#镜像。 - dotnetcore8.0: C#镜像。 - dotnetcore9.0: C#镜像。 - go-1.10.3: go镜像。 - go-1.11.6: go镜像。 - go-1.12.1: go镜像。 - go-1.23: go镜像。 - gradle2.13-jdk1.8: gradle镜像。 - gradle2.14.1-jdk1.8: gradle镜像。 - gradle3.3-jdk1.8: gradle镜像。 - gradle4.1-jdk1.8: gradle镜像。 - gradle4.2-jdk1.8: gradle镜像。 - gradle4.3-jdk1.8: gradle镜像。 - gradle4.4-jdk1.8: gradle镜像。 - gradle4.5-jdk1.8: gradle镜像。 - gradle4.6-jdk1.8: gradle镜像。 - gradle4.7-jdk1.8: gradle镜像。 - gradle4.8-jdk1.8: gradle镜像。 - gradle4.8-jdk1.9: gradle镜像。 - gradle4.9-jdk1.8: gradle镜像。 - gradle4.9-jdk1.9: gradle镜像。 - gradlew: gradle镜像。 - maven3.3.1-jdk7: maven镜像。 - maven3.5.3-jdk1.10: maven镜像。 - maven3.5.3-jdk1.11: maven镜像。 - maven3.5.3-jdk1.7: maven镜像。 - maven3.5.3-jdk1.8: maven镜像。 - maven3.5.3-jdk1.9: maven镜像。 - maven3.5.3-jdk7: maven镜像。 - maven3.5.3-jdk8-open: maven镜像。 - maven3.6.1-jdk10: maven镜像。 - maven3.6.1-jdk9: maven镜像。 - maven3.6.3-jdk11: maven镜像。 - maven3.8.5-jdk1.17: maven镜像。 - maven3.8.5-jdk17: maven镜像。 - maven3.9.5-jdk21: maven镜像。 - mono6-msbuild16-dotnetcoresdk2.1: C#镜像。 - mono6-msbuild16-dotnetcoresdk2.2: C#镜像。 - mono6-msbuild16-dotnetcoresdk3.0: C#镜像。 - mono6-msbuild16-dotnetcoresdk3.1: C#镜像。 - mono6-msbuild16-dotnetcoresdk5.0: C#镜像。 - mono6-msbuild16-dotnetcoresdk6.0: C#镜像。 - msbuild15-dotnetframework3.5: C#镜像。 - msbuild15-dotnetframework4.7.2: C#镜像。 - msbuild16-dotnetframework4.8: C#镜像。 **默认取值：** 不涉及。

        :return: The cfg_value of this TaskCheckSettingsItem.
        :rtype: str
        """
        return self._cfg_value

    @cfg_value.setter
    def cfg_value(self, cfg_value):
        r"""Sets the cfg_value of this TaskCheckSettingsItem.

        **参数解释:** 规则集对应的编译配置值。 **约束限制:** cfg_key为compileTool、buildToolVersion时，cfg_value的值必填。 **取值范围:** - ant1.10.1-jdk1.8: ant镜像。 - ant1.10.13-jdk1.8: ant镜像。 - ant1.10.3-jdk1.8: ant镜像。 - ant1.9.4-jdk1.8: ant镜像。 - cmake2.8.12-gcc4.8.5: C++镜像。 - cmake2.8.12-gcc5.5.0: C++镜像。 - cmake2.8.12-gcc6.4.0: C++镜像。 - cmake2.8.12-gcc7.3.0: C++镜像。 - cmake3.10.1-gcc4.8.5: C++镜像。 - cmake3.10.1-gcc5.5.0: C++镜像。 - cmake3.10.1-gcc6.4.0: C++镜像。 - cmake3.10.1-gcc7.3.0: C++镜像。 - cmake3.15.5-gcc7.5.0: C++镜像。 - cmake3.15.5-gcc8.3.0: C++镜像。 - cmake3.16.0-gcc9.2.0: C++镜像。 - dotnetcore2.2: C#镜像。 - dotnetcore3.0: C#镜像。 - dotnetcore3.1: C#镜像。 - dotnetcore5.0: C#镜像。 - dotnetcore6.0: C#镜像。 - dotnetcore7.0: C#镜像。 - dotnetcore8.0: C#镜像。 - dotnetcore9.0: C#镜像。 - go-1.10.3: go镜像。 - go-1.11.6: go镜像。 - go-1.12.1: go镜像。 - go-1.23: go镜像。 - gradle2.13-jdk1.8: gradle镜像。 - gradle2.14.1-jdk1.8: gradle镜像。 - gradle3.3-jdk1.8: gradle镜像。 - gradle4.1-jdk1.8: gradle镜像。 - gradle4.2-jdk1.8: gradle镜像。 - gradle4.3-jdk1.8: gradle镜像。 - gradle4.4-jdk1.8: gradle镜像。 - gradle4.5-jdk1.8: gradle镜像。 - gradle4.6-jdk1.8: gradle镜像。 - gradle4.7-jdk1.8: gradle镜像。 - gradle4.8-jdk1.8: gradle镜像。 - gradle4.8-jdk1.9: gradle镜像。 - gradle4.9-jdk1.8: gradle镜像。 - gradle4.9-jdk1.9: gradle镜像。 - gradlew: gradle镜像。 - maven3.3.1-jdk7: maven镜像。 - maven3.5.3-jdk1.10: maven镜像。 - maven3.5.3-jdk1.11: maven镜像。 - maven3.5.3-jdk1.7: maven镜像。 - maven3.5.3-jdk1.8: maven镜像。 - maven3.5.3-jdk1.9: maven镜像。 - maven3.5.3-jdk7: maven镜像。 - maven3.5.3-jdk8-open: maven镜像。 - maven3.6.1-jdk10: maven镜像。 - maven3.6.1-jdk9: maven镜像。 - maven3.6.3-jdk11: maven镜像。 - maven3.8.5-jdk1.17: maven镜像。 - maven3.8.5-jdk17: maven镜像。 - maven3.9.5-jdk21: maven镜像。 - mono6-msbuild16-dotnetcoresdk2.1: C#镜像。 - mono6-msbuild16-dotnetcoresdk2.2: C#镜像。 - mono6-msbuild16-dotnetcoresdk3.0: C#镜像。 - mono6-msbuild16-dotnetcoresdk3.1: C#镜像。 - mono6-msbuild16-dotnetcoresdk5.0: C#镜像。 - mono6-msbuild16-dotnetcoresdk6.0: C#镜像。 - msbuild15-dotnetframework3.5: C#镜像。 - msbuild15-dotnetframework4.7.2: C#镜像。 - msbuild16-dotnetframework4.8: C#镜像。 **默认取值：** 不涉及。

        :param cfg_value: The cfg_value of this TaskCheckSettingsItem.
        :type cfg_value: str
        """
        self._cfg_value = cfg_value

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
        if not isinstance(other, TaskCheckSettingsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
