# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableVacuumInfoOpen:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vacuum_running_info': 'list[TableInfoOpen]',
        'vacuum_waiting_info': 'list[TableInfoOpen]',
        'vacuum_finished_info': 'list[TableInfoOpen]',
        'vacuum_canceled_info': 'list[TableInfoOpen]'
    }

    attribute_map = {
        'vacuum_running_info': 'vacuum_running_info',
        'vacuum_waiting_info': 'vacuum_waiting_info',
        'vacuum_finished_info': 'vacuum_finished_info',
        'vacuum_canceled_info': 'vacuum_canceled_info'
    }

    def __init__(self, vacuum_running_info=None, vacuum_waiting_info=None, vacuum_finished_info=None, vacuum_canceled_info=None):
        r"""TableVacuumInfoOpen

        The model defined in huaweicloud sdk

        :param vacuum_running_info: **参数解释**： 运行中的表信息。 **默认取值**： 不涉及
        :type vacuum_running_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        :param vacuum_waiting_info: **参数解释**： 等待中的表信息。 **默认取值**： 不涉及
        :type vacuum_waiting_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        :param vacuum_finished_info: **参数解释**： 已结束的表信息。 **默认取值**： 不涉及
        :type vacuum_finished_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        :param vacuum_canceled_info: **参数解释**： 取消的表信息。 **默认取值**： 不涉及
        :type vacuum_canceled_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        
        

        self._vacuum_running_info = None
        self._vacuum_waiting_info = None
        self._vacuum_finished_info = None
        self._vacuum_canceled_info = None
        self.discriminator = None

        if vacuum_running_info is not None:
            self.vacuum_running_info = vacuum_running_info
        if vacuum_waiting_info is not None:
            self.vacuum_waiting_info = vacuum_waiting_info
        if vacuum_finished_info is not None:
            self.vacuum_finished_info = vacuum_finished_info
        if vacuum_canceled_info is not None:
            self.vacuum_canceled_info = vacuum_canceled_info

    @property
    def vacuum_running_info(self):
        r"""Gets the vacuum_running_info of this TableVacuumInfoOpen.

        **参数解释**： 运行中的表信息。 **默认取值**： 不涉及

        :return: The vacuum_running_info of this TableVacuumInfoOpen.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        return self._vacuum_running_info

    @vacuum_running_info.setter
    def vacuum_running_info(self, vacuum_running_info):
        r"""Sets the vacuum_running_info of this TableVacuumInfoOpen.

        **参数解释**： 运行中的表信息。 **默认取值**： 不涉及

        :param vacuum_running_info: The vacuum_running_info of this TableVacuumInfoOpen.
        :type vacuum_running_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        self._vacuum_running_info = vacuum_running_info

    @property
    def vacuum_waiting_info(self):
        r"""Gets the vacuum_waiting_info of this TableVacuumInfoOpen.

        **参数解释**： 等待中的表信息。 **默认取值**： 不涉及

        :return: The vacuum_waiting_info of this TableVacuumInfoOpen.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        return self._vacuum_waiting_info

    @vacuum_waiting_info.setter
    def vacuum_waiting_info(self, vacuum_waiting_info):
        r"""Sets the vacuum_waiting_info of this TableVacuumInfoOpen.

        **参数解释**： 等待中的表信息。 **默认取值**： 不涉及

        :param vacuum_waiting_info: The vacuum_waiting_info of this TableVacuumInfoOpen.
        :type vacuum_waiting_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        self._vacuum_waiting_info = vacuum_waiting_info

    @property
    def vacuum_finished_info(self):
        r"""Gets the vacuum_finished_info of this TableVacuumInfoOpen.

        **参数解释**： 已结束的表信息。 **默认取值**： 不涉及

        :return: The vacuum_finished_info of this TableVacuumInfoOpen.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        return self._vacuum_finished_info

    @vacuum_finished_info.setter
    def vacuum_finished_info(self, vacuum_finished_info):
        r"""Sets the vacuum_finished_info of this TableVacuumInfoOpen.

        **参数解释**： 已结束的表信息。 **默认取值**： 不涉及

        :param vacuum_finished_info: The vacuum_finished_info of this TableVacuumInfoOpen.
        :type vacuum_finished_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        self._vacuum_finished_info = vacuum_finished_info

    @property
    def vacuum_canceled_info(self):
        r"""Gets the vacuum_canceled_info of this TableVacuumInfoOpen.

        **参数解释**： 取消的表信息。 **默认取值**： 不涉及

        :return: The vacuum_canceled_info of this TableVacuumInfoOpen.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        return self._vacuum_canceled_info

    @vacuum_canceled_info.setter
    def vacuum_canceled_info(self, vacuum_canceled_info):
        r"""Sets the vacuum_canceled_info of this TableVacuumInfoOpen.

        **参数解释**： 取消的表信息。 **默认取值**： 不涉及

        :param vacuum_canceled_info: The vacuum_canceled_info of this TableVacuumInfoOpen.
        :type vacuum_canceled_info: list[:class:`huaweicloudsdkdws.v2.TableInfoOpen`]
        """
        self._vacuum_canceled_info = vacuum_canceled_info

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
        if not isinstance(other, TableVacuumInfoOpen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
